// Include C++ headers
#include <iostream>
#include <string>
#include <map>
// Include GLEW
#include <GL/glew.h>
// Include GLFW
#include <glfw3.h>
// Include GLM
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
// Shader loading utilities and other
#include <common/shader.h>
#include <common/util.h>
#include <common/camera.h>
#include <common/model.h>
#include <common/skeleton.h>
using namespace std;
using namespace glm;
// Function prototypes
void initialize();
void createContext();
void mainLoop();
void free();
struct Light;
struct Material;
void uploadMaterial(const Material& mtl);
void uploadLight(const Light& light);
map<int, mat4> calculateModelPoseFromCoordinates(map<int, float> q);
vector<mat4> calculateSkinningTransformations(map<int, float> q);
vector<float> calculateSkinningIndices();
#define W_WIDTH 1024
#define W_HEIGHT 768
#define TITLE "Lab 06"
// global variables
GLFWwindow* window;
Camera* camera;
GLuint shaderProgram;
GLuint projectionMatrixLocation, viewMatrixLocation, modelMatrixLocation;
// light properties
GLuint LaLocation, LdLocation, LsLocation, lightPositionLocation, lightPowerLocation;
// material properties
GLuint KdLocation, KsLocation, KaLocation, NsLocation;
GLuint surfaceVAO, surfaceVerticesVBO, surfacesBoneIndicesVBO, maleBoneIndicesVBO;
Drawable *segment, *skeletonSkin;
GLuint useSkinningLocation, boneTransformationsLocation;
Skeleton* skeleton;

struct Light {
	glm::vec4 La;
	glm::vec4 Ld;
	glm::vec4 Ls;
	glm::vec3 lightPosition_worldspace;
	float power;
};

struct Material {
	glm::vec4 Ka;
	glm::vec4 Kd;
	glm::vec4 Ks;
	float Ns;
};

const Material boneMaterial{
	vec4{ 0.1, 0.1, 0.1, 1 },
	vec4{ 1.0, 1.0, 1.0, 1 },
	vec4{ 0.3, 0.3, 0.3, 1 },
	0.1f
};

Light light{
	vec4{ 1, 1, 1, 1 },
	vec4{ 1, 1, 1, 1 },
	vec4{ 1, 1, 1, 1 },
	vec3{ 0, 4, 4 },
	20.0f
};

// Coordinate names for mnemonic indexing
enum CoordinateName {
	PELVIS_TRA_X = 0, PELVIS_TRA_Y, PELVIS_TRA_Z,
	PELVIS_ROT_X, PELVIS_ROT_Y, PELVIS_ROT_Z,
	HIP_R_FLEX, HIP_R_ADD, HIP_R_ROT, KNEE_R_FLEX, ANKLE_R_FLEX, MTP_R_FLEX,
	HIP_L_FLEX, HIP_L_ADD, HIP_L_ROT, KNEE_L_FLEX, ANKLE_L_FLEX, MTP_L_FLEX,
	LUMBAR_FLEX, LUMBAR_BEND, LUMBAR_ROT, DOFS
};
// Joint names for mnemonic indexing
enum JointName {
	BASE = 0,
	HIP_R, KNEE_R, ANKLE_R, SUBTALAR_R, MTP_R,
	BACK,
	HIP_L, KNEE_L, ANKLE_L, SUBTALAR_L, MTP_L,
	JOINTS
};
// Body names for mnemonic indexing
enum BodyName {
	PELVIS = 0,
	FEMUR_R, TIBIA_R, TALUS_R, CALCN_R, TOES_R,
	TORSO, BODIES,
	FEMUR_L, TIBIA_L, TALUS_L, CALCN_L, TOES_L
};

// default pose used for binding the skeleton and the mesh
static const map<int, float> bindingPose = {
	{ CoordinateName::PELVIS_TRA_X,  0.0 },
{ CoordinateName::PELVIS_TRA_Y, 0.0 },
{ CoordinateName::PELVIS_TRA_Z, 0 },
{ CoordinateName::PELVIS_ROT_X, 0 },
{ CoordinateName::PELVIS_ROT_Y, 0 },
{ CoordinateName::PELVIS_ROT_Z, 0 },
{ CoordinateName::HIP_R_FLEX, 3 },
{ CoordinateName::HIP_R_ADD, -5 },
{ CoordinateName::HIP_R_ROT, 0 },
{ CoordinateName::KNEE_R_FLEX, -15 },
{ CoordinateName::ANKLE_R_FLEX, 15 },
{ CoordinateName::MTP_R_FLEX, 0 },
{ CoordinateName::LUMBAR_FLEX, 0 },
{ CoordinateName::LUMBAR_BEND, 0 },
{ CoordinateName::LUMBAR_ROT, 0 },
{ CoordinateName::HIP_L_FLEX, 3 },
{ CoordinateName::HIP_L_ADD, 5 },
{ CoordinateName::HIP_L_ROT, 0 },
{ CoordinateName::KNEE_L_FLEX, -15 },
{ CoordinateName::ANKLE_L_FLEX, 15 },
{ CoordinateName::MTP_L_FLEX, 0 }
};

void uploadMaterial(const Material& mtl) {
	glUniform4f(KaLocation, mtl.Ka.r, mtl.Ka.g, mtl.Ka.b, mtl.Ka.a);
	glUniform4f(KdLocation, mtl.Kd.r, mtl.Kd.g, mtl.Kd.b, mtl.Kd.a);
	glUniform4f(KsLocation, mtl.Ks.r, mtl.Ks.g, mtl.Ks.b, mtl.Ks.a);
	glUniform1f(NsLocation, mtl.Ns);
}

void uploadLight(const Light& light) {
	glUniform4f(LaLocation, light.La.r, light.La.g, light.La.b, light.La.a);
	glUniform4f(LdLocation, light.Ld.r, light.Ld.g, light.Ld.b, light.Ld.a);
	glUniform4f(LsLocation, light.Ls.r, light.Ls.g, light.Ls.b, light.Ls.a);
	glUniform3f(lightPositionLocation, light.lightPosition_worldspace.x,
		light.lightPosition_worldspace.y, light.lightPosition_worldspace.z);
	glUniform1f(lightPowerLocation, light.power);
}

map<int, mat4> calculateModelPoseFromCoordinates(map<int, float> q) {
	map<int, mat4> jointLocalTransformations;
	// base / pelvis joint
	mat4 pelvisTra = translate(mat4(), vec3(
		q[CoordinateName::PELVIS_TRA_X],
		q[CoordinateName::PELVIS_TRA_Y],
		q[CoordinateName::PELVIS_TRA_Z]));
	mat4 pelvisRot = mat4(1.0);
	jointLocalTransformations[JointName::BASE] = pelvisTra * pelvisRot;
	// right hip joint
	vec3 hipROffset = vec3(-0.072, -0.068, 0.086);
	mat4 hipRTra = translate(mat4(), hipROffset);
	mat4 hipRRotX = rotate(mat4(), radians(q[CoordinateName::HIP_R_ADD]), vec3(1, 0, 0));
	mat4 hipRRotY = rotate(mat4(), radians(q[CoordinateName::HIP_R_ROT]), vec3(0, 1, 0));
	mat4 hipRRotZ = rotate(mat4(), radians(q[CoordinateName::HIP_R_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::HIP_R] = hipRTra * hipRRotX * hipRRotY * hipRRotZ;
	// left hip joint
	vec3 hipLOffset = vec3(-0.072, -0.068, -0.086);
	mat4 hipLTra = translate(mat4(), hipLOffset);
	mat4 hipLRotX = rotate(mat4(), radians(q[CoordinateName::HIP_L_ADD]), vec3(1, 0, 0));
	mat4 hipLRotY = rotate(mat4(), radians(q[CoordinateName::HIP_L_ROT]), vec3(0, 1, 0));
	mat4 hipLRotZ = rotate(mat4(), radians(q[CoordinateName::HIP_L_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::HIP_L] = hipLTra * hipLRotX * hipLRotY * hipLRotZ;
	// right knee joint
	vec3 kneeROffset = vec3(0.0, -0.40, 0.0);
	mat4 kneeRTra = translate(mat4(1.0), kneeROffset);
	mat4 kneeRRotZ = rotate(mat4(), radians(q[CoordinateName::KNEE_R_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::KNEE_R] = kneeRTra * kneeRRotZ;
	// left knee joint
	vec3 kneeLOffset = vec3(0.0, -0.40, 0.0);
	mat4 kneeLTra = translate(mat4(1.0), kneeLOffset);
	mat4 kneeLRotZ = rotate(mat4(), radians(q[CoordinateName::KNEE_L_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::KNEE_L] = kneeLTra * kneeLRotZ;
	// right ankle joint
	vec3 ankleROffset = vec3(0, -0.430, 0);
	mat4 ankleRTra = translate(mat4(1.0), ankleROffset);
	mat4 ankleRRotZ = rotate(mat4(), radians(q[CoordinateName::ANKLE_R_FLEX]), vec3(0, 0, 1));
	mat4 talusRModelMatrix = ankleRRotZ;
	jointLocalTransformations[JointName::ANKLE_R] = ankleRTra * ankleRRotZ;
	// left ankle joint
	vec3 ankleLOffset = vec3(-0., -0.430, 0);
	mat4 ankleLTra = translate(mat4(1.0), ankleLOffset);
	mat4 ankleLRotZ = rotate(mat4(), radians(q[CoordinateName::ANKLE_L_FLEX]), vec3(0, 0, 1));
	mat4 talusLModelMatrix = ankleLRotZ;
	jointLocalTransformations[JointName::ANKLE_L] = ankleLTra * ankleLRotZ;
	// right calcn joint
	vec3 calcnROffset = vec3(-0.062, -0.053, 0.010);
	mat4 calcnRTra = translate(mat4(1.0), calcnROffset);
	jointLocalTransformations[JointName::SUBTALAR_R] = calcnRTra;
	// left calcn joint
	vec3 calcnLOffset = vec3(-0.062, -0.053, 0.010);
	mat4 calcnLTra = translate(mat4(1.0), calcnLOffset);
	jointLocalTransformations[JointName::SUBTALAR_L] = calcnLTra;
	// right mtp joint
	vec3 toesROffset = vec3(0.184, -0.002, 0.001);
	mat4 mtpRTra = translate(mat4(1.0), toesROffset);
	mat4 mtpRRotZ = rotate(mat4(), radians(q[CoordinateName::MTP_R_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::MTP_R] = mtpRTra * mtpRRotZ;
	// left mtp joint
	vec3 toesLOffset = vec3(0.184, -0.002, 0.001);
	mat4 mtpLTra = translate(mat4(1.0), toesLOffset);
	mat4 mtpLRotZ = rotate(mat4(), radians(q[CoordinateName::MTP_L_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::MTP_L] = mtpLTra * mtpLRotZ;
	// back joint
	vec3 backOffset = vec3(-0.103, 0.09, 0.0);
	mat4 lumbarTra = translate(mat4(1.0), backOffset);
	mat4 lumbarRotX = rotate(mat4(), radians(q[CoordinateName::LUMBAR_BEND]), vec3(1, 0, 0));
	mat4 lumbarRotY = rotate(mat4(), radians(q[CoordinateName::LUMBAR_ROT]), vec3(0, 1, 0));
	mat4 lumbarRotZ = rotate(mat4(), radians(q[CoordinateName::LUMBAR_FLEX]), vec3(0, 0, 1));
	jointLocalTransformations[JointName::BACK] = lumbarTra * lumbarRotX * lumbarRotY * lumbarRotZ;
	return jointLocalTransformations;
}

vector<mat4> calculateSkinningTransformations(map<int, float> q) {
	auto jointLocalTransformationsBinding = calculateModelPoseFromCoordinates(bindingPose);
	skeleton->setPose(jointLocalTransformationsBinding);
	auto bindingWorldTransformations = skeleton->getJointWorldTransformations();
	auto jointLocalTransformationsCurrent = calculateModelPoseFromCoordinates(q);
	skeleton->setPose(jointLocalTransformationsCurrent);
	auto currentWorldTransformations = skeleton->getJointWorldTransformations();
	vector<mat4> skinningTransformations(JointName::JOINTS);
	for (auto joint : bindingWorldTransformations) {
		mat4 BInvWorld = glm::inverse(joint.second);
		mat4 JWorld = currentWorldTransformations[joint.first];
		skinningTransformations[joint.first] = JWorld * BInvWorld;
	}
	return skinningTransformations;
}

vector<float> calculateSkinningIndices() {
	// Task 4.3: assign a body index for each vertex in the model (skin) based
	// on its proximity to a body part (e.g. tight)
	vector<float> indices;
	for (auto v : skeletonSkin->indexedVertices) {
		// dummy
		//indices.push_back(1.0);
		if (v.y <= -0.07 && v.y >= -0.5 && v.z > 0.00 && v.z < 0.25) {
			indices.push_back(JointName::HIP_R);
		}
		else if (v.y <= -0.07 && v.y >= -0.5 && v.z < 0.00 && v.z > -0.25) {
			indices.push_back(JointName::HIP_L);
		}
		else if (v.y < -0.5 && v.y > -0.85 && v.z > 0.00 &&  v.z < 0.25) {
			indices.push_back(JointName::KNEE_R);
		}
		else if (v.y < -0.5 && v.y > -0.85 && v.z < 0.00 &&  v.z >-0.25) {
			indices.push_back(JointName::KNEE_L);
		}
		else if (v.y <= -0.85 && v.y >= -1.0 && v.z > 0.00 && v.z < 0.25 && v.x > -1 && v.x < 0) {
			indices.push_back(JointName::ANKLE_R);
		}
		else if (v.y <= -0.85 && v.y >= -1.0 && v.z < 0.00 && v.z >-0.25 && v.x > -1 && v.x < 0) {
			indices.push_back(JointName::ANKLE_L);
		}
		else if (v.y <= -0.85 && v.y >= -1.0 && v.z > 0.00 && v.z < 0.25 &&  v.x > 0) {
			indices.push_back(JointName::MTP_R);
		}
		else if (v.y <= -0.85 && v.y >= -1.0 && v.z < 0.00 && v.z >-0.25 &&  v.x > 0) {
			indices.push_back(JointName::MTP_L);
		}
		else if (v.y > 0.0 || v.y > -0.4 && v.z > 0.25 || v.y > -0.4 && v.z < -0.25) {
			indices.push_back(JointName::BACK);
		}
		else {
			indices.push_back(JointName::BASE);
		}
	}
	return indices;
}

void createContext() {
	// shader
	shaderProgram = loadShaders(
		"StandardShading.vertexshader",
		"StandardShading.fragmentshader");
	// get pointers to uniforms
	modelMatrixLocation = glGetUniformLocation(shaderProgram, "M");
	viewMatrixLocation = glGetUniformLocation(shaderProgram, "V");
	projectionMatrixLocation = glGetUniformLocation(shaderProgram, "P");
	KaLocation = glGetUniformLocation(shaderProgram, "mtl.Ka");
	KdLocation = glGetUniformLocation(shaderProgram, "mtl.Kd");
	KsLocation = glGetUniformLocation(shaderProgram, "mtl.Ks");
	NsLocation = glGetUniformLocation(shaderProgram, "mtl.Ns");
	LaLocation = glGetUniformLocation(shaderProgram, "light.La");
	LdLocation = glGetUniformLocation(shaderProgram, "light.Ld");
	LsLocation = glGetUniformLocation(shaderProgram, "light.Ls");
	lightPositionLocation = glGetUniformLocation(shaderProgram, "light.lightPosition_worldspace");
	lightPowerLocation = glGetUniformLocation(shaderProgram, "light.power");
	useSkinningLocation = glGetUniformLocation(shaderProgram, "useSkinning");
	boneTransformationsLocation = glGetUniformLocation(shaderProgram, "boneTransformations");
	// Task 3.1a: define the relations between the bodies and the joints
	// A skeleton is a collection of joints and bodies. Each body is independent
	// of each other (conceptually). Furthermore, each body can  have many
	// drawables (geometries) attached. The joints are related to each other
	// and form a parent child relations. A joint is attached on a body.
	skeleton = new Skeleton(modelMatrixLocation, viewMatrixLocation, projectionMatrixLocation);
	// pelvis
	Joint* baseJoint = new Joint(); // creates a joint
	baseJoint->parent = NULL; // assigns the parent joint (NULL -> no parent)
	skeleton->joints[JointName::BASE] = baseJoint; // adds the joint in the skeleton's dictionary
	Body* pelvisBody = new Body(); // creates a body
	pelvisBody->drawables.push_back(new Drawable("models/sacrum.vtp")); // append 3 geometries
	pelvisBody->drawables.push_back(new Drawable("models/pelvis.vtp"));
	pelvisBody->drawables.push_back(new Drawable("models/l_pelvis.vtp"));
	pelvisBody->joint = baseJoint; // relates to a joint
	skeleton->bodies[BodyName::PELVIS] = pelvisBody; // adds the body in the skeleton's dictionary
													 // right hip
	Joint* hipR = new Joint();
	hipR->parent = baseJoint;
	skeleton->joints[JointName::HIP_R] = hipR;
	Body* femurR = new Body();
	femurR->drawables.push_back(new Drawable("models/femur.vtp"));
	femurR->joint = hipR;
	skeleton->bodies[BodyName::FEMUR_R] = femurR;
	// right tibia
	Joint* kneeR = new Joint();
	kneeR->parent = hipR;
	skeleton->joints[JointName::KNEE_R] = kneeR;
	Body* tibiaR = new Body();
	tibiaR->drawables.push_back(new Drawable("models/tibia.vtp"));
	tibiaR->drawables.push_back(new Drawable("models/fibula.vtp"));
	tibiaR->joint = kneeR;
	skeleton->bodies[BodyName::TIBIA_R] = tibiaR;
	// right talus
	Joint* ankleR = new Joint();
	ankleR->parent = kneeR;
	skeleton->joints[JointName::ANKLE_R] = ankleR;
	Body* talusR = new Body();
	talusR->drawables.push_back(new Drawable("models/talus.vtp"));
	talusR->joint = ankleR;
	skeleton->bodies[BodyName::TALUS_R] = talusR;
	// right calcn
	Joint* subtalarR = new Joint();
	subtalarR->parent = ankleR;
	skeleton->joints[JointName::SUBTALAR_R] = subtalarR;
	Body* calcnR = new Body();
	calcnR->drawables.push_back(new Drawable("models/foot.vtp"));
	calcnR->joint = subtalarR;
	skeleton->bodies[BodyName::CALCN_R] = calcnR;
	//right toes
	Joint* mtpR = new Joint();
	mtpR->parent = subtalarR;
	skeleton->joints[JointName::MTP_R] = mtpR;
	Body* toesR = new Body();
	toesR->drawables.push_back(new Drawable("models/bofoot.vtp"));
	toesR->joint = mtpR;
	skeleton->bodies[BodyName::TOES_R] = toesR;
	// torso
	Joint* back = new Joint();
	back->parent = baseJoint;
	skeleton->joints[JointName::BACK] = back;
	Body* torso = new Body();
	torso->drawables.push_back(new Drawable("models/hat_spine.vtp"));
	torso->drawables.push_back(new Drawable("models/hat_jaw.vtp"));
	torso->drawables.push_back(new Drawable("models/hat_skull.vtp"));
	torso->drawables.push_back(new Drawable("models/hat_ribs.vtp"));
	torso->joint = back;
	skeleton->bodies[BodyName::TORSO] = torso;
	// Homework 1: construct the left leg (similar to the right). The
	// corresponding geometries are located in the models folder.
	// left hip
	Joint* hipL = new Joint();
	hipL->parent = baseJoint;
	skeleton->joints[JointName::HIP_L] = hipL;
	// left femur
	Body* femurL = new Body();
	femurL->drawables.push_back(new Drawable("models/l_femur.vtp"));
	femurL->joint = hipL;
	skeleton->bodies[BodyName::FEMUR_L] = femurL;
	// left knee
	Joint* kneeL = new Joint();
	kneeL->parent = hipL;
	skeleton->joints[JointName::KNEE_L] = kneeL;
	// left tibia
	Body* tibiaL = new Body();
	tibiaL->drawables.push_back(new Drawable("models/l_tibia.vtp"));
	tibiaL->drawables.push_back(new Drawable("models/l_fibula.vtp"));
	tibiaL->joint = kneeL;
	skeleton->bodies[BodyName::TIBIA_L] = tibiaL;
	// left talus
	Joint* ankleL = new Joint();
	ankleL->parent = kneeL;
	skeleton->joints[JointName::ANKLE_L] = ankleL;
	Body* talusL = new Body();
	talusL->drawables.push_back(new Drawable("models/l_talus.vtp"));
	talusL->joint = ankleL;
	skeleton->bodies[BodyName::TALUS_L] = talusL;
	// left calcn
	Joint* subtalarL = new Joint();
	subtalarL->parent = ankleL;
	skeleton->joints[JointName::SUBTALAR_L] = subtalarL;
	Body* calcnL = new Body();
	calcnL->drawables.push_back(new Drawable("models/l_foot.vtp"));
	calcnL->joint = subtalarL;
	skeleton->bodies[BodyName::CALCN_L] = calcnL;
	// left toes
	Joint* mtpL = new Joint();
	mtpL->parent = subtalarL;
	skeleton->joints[JointName::MTP_L] = mtpL;
	Body* toesL = new Body();
	toesL->drawables.push_back(new Drawable("models/l_bofoot.vtp"));
	toesL->joint = mtpL;
	skeleton->bodies[BodyName::TOES_L] = toesL;
	// skin
	skeletonSkin = new Drawable("models/male.obj");
	auto maleBoneIndices = calculateSkinningIndices();
	glGenBuffers(1, &maleBoneIndicesVBO);
	glBindBuffer(GL_ARRAY_BUFFER, maleBoneIndicesVBO);
	glBufferData(GL_ARRAY_BUFFER, maleBoneIndices.size() * sizeof(float),
		&maleBoneIndices[0], GL_STATIC_DRAW);
	glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 0, NULL);
	glEnableVertexAttribArray(3);
}

void mainLoop() {
	camera->position = vec3(0, 0, 2.5);
	float t = 0.0f;
	do {
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		glUseProgram(shaderProgram);
		// camera
		camera->update();
		mat4 projectionMatrix = camera->projectionMatrix;
		mat4 viewMatrix = camera->viewMatrix;
		// light
		uploadLight(light);
		t += 0.005f;
		glUniform1i(useSkinningLocation, 0);
		uploadMaterial(boneMaterial);
		skeleton->draw(viewMatrix, projectionMatrix);
		// Task 3.2: assign values to the generalized coordinates and correct
		// the transformations in calculateModelPoseFromCoordinates()
		// Homework 2: add 3 rotational DoFs for the pelvis and the necessary
		// DoFs for left leg.
		// Task 3.3: make the skeleton walk (approximately)
		// Homework 3: model Michael Jackson's Moonwalk .
		map<int, float> q;
		q[CoordinateName::PELVIS_TRA_X] = 0;
		q[CoordinateName::PELVIS_TRA_Y] = 0;
		q[CoordinateName::PELVIS_TRA_Z] = 0;
		q[CoordinateName::PELVIS_ROT_X] = 0;
		q[CoordinateName::PELVIS_ROT_Y] = 0;
		q[CoordinateName::PELVIS_ROT_Z] = 0;
		q[CoordinateName::HIP_R_FLEX] = -15 * sin(t);
		q[CoordinateName::HIP_R_ADD] = 0;
		q[CoordinateName::HIP_R_ROT] = 0;
		q[CoordinateName::KNEE_R_FLEX] = -20 * sin(t) - 20;
		q[CoordinateName::ANKLE_R_FLEX] = -30 * sin(t);
		q[CoordinateName::MTP_R_FLEX] = 30 * sin(t) + 30;
		q[CoordinateName::LUMBAR_FLEX] = -25;
		q[CoordinateName::LUMBAR_BEND] = 0;
		q[CoordinateName::LUMBAR_ROT] = 0;
		q[CoordinateName::HIP_L_FLEX] = 15 * sin(t);
		q[CoordinateName::HIP_L_ADD] = 0;
		q[CoordinateName::HIP_L_ROT] = 0;
		q[CoordinateName::KNEE_L_FLEX] = -20 * sin(t) - 20;
		q[CoordinateName::ANKLE_L_FLEX] = 30 * sin(t);
		q[CoordinateName::MTP_L_FLEX] = 30 * sin(t) + 30;
		auto jointLocalTransformations = calculateModelPoseFromCoordinates(q);
		skeleton->setPose(jointLocalTransformations);
		glUniform1i(useSkinningLocation, 0);
		uploadMaterial(boneMaterial);
		skeleton->draw(viewMatrix, projectionMatrix);
		// Task 4.1: draw the skin using wireframe mode
		skeletonSkin->bind();
		mat4 maleModelMatrix = mat4(1);
		glUniformMatrix4fv(modelMatrixLocation, 1,
			GL_FALSE, &maleModelMatrix[0][0]);
		glUniformMatrix4fv(viewMatrixLocation, 1,
			GL_FALSE, &viewMatrix[0][0]);
		glUniformMatrix4fv(projectionMatrixLocation, 1,
			GL_FALSE, &projectionMatrix[0][0]);
		// Task 4.2: calculate the bone transformations
		auto T = calculateSkinningTransformations(q);
		glUniformMatrix4fv(boneTransformationsLocation, T.size(),
			GL_FALSE, &T[0][0][0]);
		glUniform1i(useSkinningLocation, 1);
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
		skeletonSkin->draw();
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
		glfwSwapBuffers(window);
		glfwPollEvents();
	} while (glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS &&
		glfwWindowShouldClose(window) == 0);
}

void free() {
	delete segment;
	// the skeleton owns the bodies and joints so memory is freed when skeleton
	// is deleted
	delete skeleton;
	delete skeletonSkin;
	glDeleteBuffers(1, &surfaceVAO);
	glDeleteVertexArrays(1, &surfaceVerticesVBO);
	glDeleteVertexArrays(1, &surfacesBoneIndicesVBO);
	glDeleteVertexArrays(1, &maleBoneIndicesVBO);
	glDeleteProgram(shaderProgram);
	glfwTerminate();
}

void initialize() {
	// Initialize GLFW
	if (!glfwInit())
		throw runtime_error("Failed to initialize GLFW\n");
	glfwWindowHint(GLFW_SAMPLES, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	// Open a window and create its OpenGL context
	window = glfwCreateWindow(W_WIDTH, W_HEIGHT, TITLE, NULL, NULL);
	if (window == NULL) {
		glfwTerminate();
		throw runtime_error(string(string("Failed to open GLFW window.") +
			" If you have an Intel GPU, they are not 3.3 compatible." +
			"Try the 2.1 version.\n"));
	}
	glfwMakeContextCurrent(window);
	// Start GLEW extension handler
	glewExperimental = GL_TRUE;
	// Initialize GLEW
	if (glewInit() != GLEW_OK) {
		glfwTerminate();
		throw runtime_error("Failed to initialize GLEW\n");
	}
	// Ensure we can capture the escape key being pressed below
	glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);
	// Hide the mouse and enable unlimited movement
	glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
	// Set the mouse at the center of the screen
	glfwPollEvents();
	glfwSetCursorPos(window, W_WIDTH / 2, W_HEIGHT / 2);
	// Gray background color
	glClearColor(0.5f, 0.5f, 0.5f, 0.0f);
	// Enable depth test
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	glDepthFunc(GL_LESS);
	// Cull triangles which normal is not towards the camera
	//glEnable(GL_CULL_FACE);
	// enable point size when drawing points
	glEnable(GL_PROGRAM_POINT_SIZE);
	// Log
	logGLParameters();
	// Create camera
	camera = new Camera(window);
}

int main(void) {
	try {
		initialize();
		createContext();
		mainLoop();
		free();
	}
	catch (exception& ex) {
		cout << ex.what() << endl;
		getchar();
		free();
		return -1;
	}
	return 0;
}