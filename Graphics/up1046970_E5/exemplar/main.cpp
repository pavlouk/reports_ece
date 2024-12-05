// Include C++ headers
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
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
#include <common/texture.h>
using namespace std;
using namespace glm;
// Function prototypes
void initialize();
void createContext();
void mainLoop();
void free();
#define W_WIDTH 1024
#define W_HEIGHT 768
#define SHADOW_WIDTH 1024
#define SHADOW_HEIGHT 1024
#define TITLE "Tree Simulation"
// Global variables
GLFWwindow* window;
Camera* camera;
Drawable* branches;
Drawable* leaves;
Drawable* plane;
// Shader references 
GLuint standardProgram, depthProgram;
// Matrices locations 
GLuint projectionMatrixLocation, viewMatrixLocation, modelMatrixLocation;
// Samplers pointers
GLuint diffuseColorSampler, specularColorSampler;
// tree texture
GLuint diffuseTreeTexture, specularTreeTexture;
// leaves texture
GLuint diffuseLeavesTexture, specularLeavesTexture;
// horizontal plane texture
GLuint diffuseFloorTexture, specularFloorTexture;
// Tree data extracted from the .obj model file
std::vector<vec3> TreeVertices, TreeNormals;
std::vector<vec2> TreeUVs;
// Leaves data extracted from the .obj model file
std::vector<vec3> LeavesVertices, LeavesNormals;
std::vector<vec2> LeavesUVs;
// Plane data extracted from the .obj model file
std::vector<vec3> PlaneVertices, PlaneNormals;
std::vector<vec2> PlaneUVs;
GLuint depthMapFBO;
GLuint depthMap;
//pointers to depth shader
GLuint lightSpaceMatrixLocation;
GLuint model_shadow;

void createContext() {
	// Create and compile our GLSL program from the shaders
	standardProgram = loadShaders(
		"StandardShading.vertexshader",
		"StandardShading.fragmentshader");
	depthProgram = loadShaders(
		"depth.vertexshader",
		"depth.fragmentshader");
	// load tree, leaves and floor obj data 
	loadOBJWithTiny("jap_branches.obj", TreeVertices, TreeUVs, TreeNormals);
	loadOBJWithTiny("jap_leaves.obj", LeavesVertices, LeavesUVs, LeavesNormals);
	loadOBJWithTiny("plane.obj", PlaneVertices, PlaneUVs, PlaneNormals);
	// assign aquired obj data to the objects
	branches = new Drawable(TreeVertices, TreeUVs, TreeNormals);
	leaves = new Drawable(LeavesVertices, LeavesUVs, LeavesNormals);
	plane = new Drawable(PlaneVertices, PlaneUVs, PlaneNormals);
	// texture images
	diffuseTreeTexture = loadSOIL("wood_t.jpg");
	diffuseLeavesTexture = loadSOIL("leaves_t.jpg");
	specularTreeTexture = loadSOIL("perlin_noise.jpg");
	specularLeavesTexture = specularTreeTexture;
	diffuseFloorTexture = loadSOIL("chess.jpg");
	specularFloorTexture = specularTreeTexture;
	// get a pointer to the texture samplers (diffuseColorSampler, specularColorSampler)
	diffuseColorSampler = glGetUniformLocation(standardProgram, "diffuseColorSampler");
	specularColorSampler = glGetUniformLocation(standardProgram, "specularColorSampler");
	// get pointers to the uniform variables of the standard shader
	projectionMatrixLocation = glGetUniformLocation(standardProgram, "P");
	viewMatrixLocation = glGetUniformLocation(standardProgram, "V");
	modelMatrixLocation = glGetUniformLocation(standardProgram, "M");
	// get pointers to the uniform variables of the depth shader
	lightSpaceMatrixLocation = glGetUniformLocation(depthProgram, "lightSpaceMatrix");
	model_shadow = glGetUniformLocation(depthProgram, "model");
	// configure depth map FBO
	glGenFramebuffers(1, &depthMapFBO);
	// create depth texture
	glGenTextures(1, &depthMap);
	glBindTexture(GL_TEXTURE_2D, depthMap);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, SHADOW_WIDTH, SHADOW_HEIGHT, 0, GL_DEPTH_COMPONENT, GL_FLOAT, NULL);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER);
	float borderColor[] = { 1.0, 1.0, 1.0, 1.0 };
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, borderColor);
	// attach depth texture as FBO's depth buffer
	glBindFramebuffer(GL_FRAMEBUFFER, depthMapFBO);
	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, depthMap, 0);
	glDrawBuffer(GL_NONE);
	glReadBuffer(GL_NONE);
	glBindFramebuffer(GL_FRAMEBUFFER, 0);
}

void mainLoop() {
	glm::vec3 lightPos(0, 4, 4);
	do {
		glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		float near_plane = 1.0f, far_plane = 7.5f;
		glm::mat4 lightProjection = glm::ortho(-10.0f, 10.0f, -10.0f, 10.0f, near_plane, far_plane);
		glm::mat4 lightView = glm::lookAt(lightPos, glm::vec3(0.0f), glm::vec3(0.0, 1.0, 0.0));
		glm::mat4 lightSpaceMatrix = lightProjection * lightView;
		// the model matrix should be common
		mat4 modelMatrix = glm::mat4(1.0);
		glUniformMatrix4fv(lightSpaceMatrixLocation, 1, GL_FALSE, &lightSpaceMatrix[0][0]);
		glUniformMatrix4fv(model_shadow, 1, GL_FALSE, &modelMatrix[0][0]);
		//glUseProgram(depthProgram);

		//glViewport(0, 0, SHADOW_WIDTH, SHADOW_HEIGHT);
		//glBindFramebuffer(GL_FRAMEBUFFER, depthMapFBO);
		//	glClear(GL_DEPTH_BUFFER_BIT);
		//	glActiveTexture(GL_TEXTURE2);
		//	glBindTexture(GL_TEXTURE_2D, diffuseFloorTexture);
		//	glUniform1i(depthMap, 2);
		//glBindFramebuffer(GL_FRAMEBUFFER, 0);
		//// reset viewport
		//glViewport(0, 0, W_WIDTH, W_HEIGHT);
		//glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// camera
		camera->update();
		mat4 projectionMatrix = camera->projectionMatrix;
		mat4 viewMatrix = camera->viewMatrix;
		// transfer M, V, P uniforms to GPU
		glUniformMatrix4fv(projectionMatrixLocation, 1, GL_FALSE, &projectionMatrix[0][0]);
		glUniformMatrix4fv(viewMatrixLocation, 1, GL_FALSE, &viewMatrix[0][0]);
		glUniformMatrix4fv(modelMatrixLocation, 1, GL_FALSE, &modelMatrix[0][0]);
		glUseProgram(standardProgram);

		// bind textures, transmit diffuse & specular maps and draw the floor
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, diffuseFloorTexture);
		glUniform1i(diffuseColorSampler, 0);
		glActiveTexture(GL_TEXTURE1);
		glBindTexture(GL_TEXTURE_2D, specularFloorTexture);
		glUniform1i(specularColorSampler, 1);
		glUniformMatrix4fv(modelMatrixLocation, 1, GL_FALSE, &modelMatrix[0][0]);
		plane->bind();
		plane->draw();
		// bind textures, transmit diffuse & specular maps and draw the branches
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, diffuseTreeTexture);
		glUniform1i(diffuseColorSampler, 0);
		glActiveTexture(GL_TEXTURE1);
		glBindTexture(GL_TEXTURE_2D, specularTreeTexture);
		glUniform1i(specularColorSampler, 1);
		glUniformMatrix4fv(modelMatrixLocation, 1, GL_FALSE, &modelMatrix[0][0]);
		branches->bind();
		branches->draw();
		// bind textures, transmit diffuse & specular maps and draw the leaves
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, diffuseLeavesTexture);
		glUniform1i(diffuseColorSampler, 0);
		glActiveTexture(GL_TEXTURE1);
		glBindTexture(GL_TEXTURE_2D, specularLeavesTexture);
		glUniform1i(specularColorSampler, 1);
		glUniformMatrix4fv(modelMatrixLocation, 1, GL_FALSE, &modelMatrix[0][0]);
		leaves->bind();
		leaves->draw();
		glfwSwapBuffers(window);
		glfwPollEvents();
	} while (glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS &&
				glfwWindowShouldClose(window) == 0);
}

void pollKeyboard(GLFWwindow* window, int key, int scancode, int action, int mods) {
	// if (key == GLFW_KEY_U)
		// add_factor += 0.1;
	// if (key == GLFW_KEY_O)
	// if (key == GLFW_KEY_L)
		// add_factor -= 0.1;
		// move_light_pos += 0.1;
	// if (key == GLFW_KEY_J)
		// move_light_pos -= 0.1;
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
	// Enable asynchronous keyboard events
	glfwSetKeyCallback(window, pollKeyboard);
	// Enable depth test
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	glDepthFunc(GL_LESS);
	// Enable blending
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	// Enable textures
	glEnable(GL_TEXTURE_2D);
	// Log
	logGLParameters();
	// Create camera
	camera = new Camera(window);
}

void free() {
	delete branches;
	delete leaves;
	delete plane;
	glDeleteTextures(1, &diffuseTreeTexture);
	glDeleteTextures(1, &diffuseLeavesTexture);
	glDeleteTextures(1, &specularTreeTexture);
	glDeleteTextures(1, &specularLeavesTexture);
	glDeleteProgram(standardProgram);
	glDeleteProgram(depthProgram);
	glfwTerminate();
}

int main(void) {
	try {
		initialize();
		createContext();
		mainLoop();
		free();
	} catch (exception& ex) {
		cout << ex.what() << endl;
		getchar();
		free();
		return -1;
	}
	return 0;
}