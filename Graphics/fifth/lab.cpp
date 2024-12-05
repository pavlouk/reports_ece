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
#define TITLE "Lab 05"

// Global variables
GLFWwindow* window;
Camera* camera;
GLuint shaderProgram;
GLuint projectionMatrixLocation, viewMatrixLocation, modelMatrixLocation;
GLuint Kambient, Kdiffusion, Kspecular, Nspec;
GLuint Lambient, Ldiffusion, Lspecular;
GLuint lightLocation;
GLuint diffuceColorSampler, specularColorSampler;
GLuint diffuseTexture, specularTexture;
GLuint objVAO, triangleVAO;
GLuint objVerticiesVBO, objUVVBO, objNormalsVBO;
GLuint triangleVerticesVBO, triangleNormalsVBO;
std::vector<vec3> objVertices, objNormals;
std::vector<vec2> objUVs;

#define RENDER_TRIANGLE 0

float add_factor = 0.0;
float move_light_pos = 0.0;
glm::vec3 lightPos = glm::vec3(0, 0, 1.8);

vec3 Kaa = vec3(0.1, 0.18725, 0.1745);
vec3 Kdd = vec3(0.396, 0.74151, 0.69102);
vec3 Kss = vec3(0.297254, 0.30829, 0.306678);
float Nss = 12.8;

void createContext()
{
	// Create and compile our GLSL program from the shaders
	shaderProgram = loadShaders(
		"StandardShading.vertexshader",
		"StandardShading.fragmentshader");

	// load obj
	loadOBJWithTiny("suzanne.obj", objVertices, objUVs, objNormals);
	//loadOBJWithTiny("earth.obj", objVertices, objUVs, objNormals);

	// Homework 4: implement flat shading by transforming the normals of the model.

	// Task 6.2: load diffuse and specular texture maps
	diffuseTexture = loadSOIL("suzanne_diffuse.bmp");
	specularTexture = loadSOIL("suzanne_specular.bmp");
	//diffuseTexture = loadSOIL("earth_diffuse.jpg");

	// Task 6.3: get a pointer to the texture samplers (diffuseColorSampler, specularColorSampler)
	diffuceColorSampler = glGetUniformLocation(shaderProgram, "diffuceColorSampler");
	specularColorSampler = glGetUniformLocation(shaderProgram, "specularColorSampler");

	// get pointers to the uniform variables
	projectionMatrixLocation = glGetUniformLocation(shaderProgram, "P");
	viewMatrixLocation = glGetUniformLocation(shaderProgram, "V");
	modelMatrixLocation = glGetUniformLocation(shaderProgram, "M");
	lightLocation = glGetUniformLocation(shaderProgram, "light_position_worldspace");

	// Homework 2

	Kambient = glGetUniformLocation(shaderProgram, "Ka");
	Kdiffusion = glGetUniformLocation(shaderProgram, "Kd");
	Kspecular = glGetUniformLocation(shaderProgram, "Ks");
	Nspec = glGetUniformLocation(shaderProgram, "Ns");

	// Homework 3

	Lambient = glGetUniformLocation(shaderProgram, "La");
	Ldiffusion = glGetUniformLocation(shaderProgram, "Ld");
	Lspecular = glGetUniformLocation(shaderProgram, "Ls");

	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

	// triangle
	// Task 1.1: bind vertex positions to attribute 0 and object normals to
	// attribute 1
	glGenVertexArrays(1, &triangleVAO);
	glBindVertexArray(triangleVAO);

	glGenBuffers(1, &triangleVerticesVBO);    // given
	glBindBuffer(GL_ARRAY_BUFFER, triangleVerticesVBO);
	const GLfloat tirangleVertices[] =
	{
		-1.5, -1.5, 0.0,
		0.0, 1.5, 0.0,
		1.5, -1.5, 0.0
	};
	glBufferData(GL_ARRAY_BUFFER, sizeof(tirangleVertices),
		&tirangleVertices[0], GL_STATIC_DRAW);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);
	glEnableVertexAttribArray(0);

	// define object normals VBO
	glGenBuffers(1, &triangleNormalsVBO);    // given
	glBindBuffer(GL_ARRAY_BUFFER, triangleNormalsVBO);

	const GLfloat tirangleNormals[] =
	{
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0
	};


	glBufferData(GL_ARRAY_BUFFER, sizeof(tirangleNormals),
		&tirangleNormals[0], GL_STATIC_DRAW);
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, NULL);
	glEnableVertexAttribArray(1);

	// obj
	// Task 6.1: bind object vertex positions to attribute 0, UV coordinates
	// to attribute 1 and normals to attribute 2
	//*/
	glGenVertexArrays(1, &objVAO);
	glBindVertexArray(objVAO);

	// vertex VBO
	glGenBuffers(1, &objVerticiesVBO);
	glBindBuffer(GL_ARRAY_BUFFER, objVerticiesVBO);
	glBufferData(GL_ARRAY_BUFFER, objVertices.size() * sizeof(glm::vec3),
		&objVertices[0], GL_STATIC_DRAW);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);
	glEnableVertexAttribArray(0);

	// Homework 1: were the model normals not given, how would you compute them?
	glGenBuffers(1, &objNormalsVBO);
	glBindBuffer(GL_ARRAY_BUFFER, objNormalsVBO);
	glBufferData(GL_ARRAY_BUFFER, objNormals.size() * sizeof(glm::vec3),
		&objNormals[0], GL_STATIC_DRAW);
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, NULL);
	glEnableVertexAttribArray(1);

	// uvs VBO
	glGenBuffers(1, &objUVVBO);
	glBindBuffer(GL_ARRAY_BUFFER, objUVVBO);
	glBufferData(GL_ARRAY_BUFFER, objUVs.size() * sizeof(glm::vec2),
		&objUVs[0], GL_STATIC_DRAW);
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, NULL);
	glEnableVertexAttribArray(2);
	//*/
}

void free()
{
	glDeleteBuffers(1, &triangleVerticesVBO);
	glDeleteBuffers(1, &triangleNormalsVBO);
	glDeleteVertexArrays(1, &triangleVAO);

	glDeleteBuffers(1, &objVerticiesVBO);
	glDeleteBuffers(1, &objUVVBO);
	glDeleteBuffers(1, &objNormalsVBO);
	glDeleteVertexArrays(1, &objVAO);

	glDeleteTextures(1, &diffuseTexture);
	glDeleteProgram(shaderProgram);
	glfwTerminate();
}

void mainLoop()
{
	
	do
	{
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		glUseProgram(shaderProgram);

		// camera
		camera->update();

		// bind
#if RENDER_TRIANGLE == 1
		glBindVertexArray(triangleVAO);
#else
		glBindVertexArray(objVAO);
#endif
		mat4 projectionMatrix = camera->projectionMatrix;
		mat4 viewMatrix = camera->viewMatrix;
		glm::mat4 modelMatrix = glm::mat4(1.0);

		// Homework 3
		// Move the position of the light source
		//lightPos.x += move_light_pos;

		// Task 1.4c: transfer uniforms to GPU
		glUniformMatrix4fv(projectionMatrixLocation, 1, GL_FALSE, &projectionMatrix[0][0]);
		glUniformMatrix4fv(viewMatrixLocation, 1, GL_FALSE, &viewMatrix[0][0]);
		glUniformMatrix4fv(modelMatrixLocation, 1, GL_FALSE, &modelMatrix[0][0]);
		glUniform3f(lightLocation, lightPos.x, lightPos.y, lightPos.z); // light

		// Homework 2
		// Material : Turquoise
		/*vec3 Kaa = vec3(0.1, 0.18725, 0.1745);
		vec3 Kdd = vec3(0.396, 0.74151, 0.69102);
		vec3 Kss = vec3(0.297254, 0.30829, 0.306678);
		float Nss = 12.8;
		*/
		glUniform3f(Kambient, Kaa.x, Kaa.y, Kaa.z);
		glUniform3f(Kdiffusion, Kdd.x, Kdd.y, Kdd.z);
		glUniform3f(Kspecular, Kss.x, Kss.y, Kdd.z);
		glUniform1f(Nspec, Nss);

		// Homework 3
		// Control the intensity of light with the keys U and O
		vec3 Laa = vec3(1, 1, 1) + add_factor;
		vec3 Ldd = vec3(1, 1, 1) + 2 * add_factor;
		vec3 Lss = vec3(1, 1, 1) + 3 * add_factor;

		glUniform3f(Lambient, Laa.x, Laa.y, Laa.z);
		glUniform3f(Ldiffusion, Ldd.x, Ldd.y, Ldd.z);
		glUniform3f(Lspecular, Lss.x, Lss.y, Ldd.z);

		// Task 6.4: bind textures and transmit diffuse and specular maps to the GPU
		//*/
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, diffuseTexture);
		glUniform1i(diffuceColorSampler, 0);

		glActiveTexture(GL_TEXTURE1);
		glBindTexture(GL_TEXTURE_2D, specularTexture);
		glUniform1i(specularColorSampler, 1);
		//*/

		// draw
#if RENDER_TRIANGLE == 1
		glDrawArrays(GL_TRIANGLES, 0, 3);
#else
		glDrawArrays(GL_TRIANGLES, 0, objVertices.size());
#endif

		glfwSwapBuffers(window);

		glfwPollEvents();
	} while (glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS &&
		glfwWindowShouldClose(window) == 0);
}

void pollKeyboard(GLFWwindow* window, int key, int scancode, int action, int mods) {
	if (key == GLFW_KEY_U) {
		add_factor += 0.1;
	}
	if (key == GLFW_KEY_O) {
		add_factor -= 0.1;
	}
	if (key == GLFW_KEY_L) {
		lightPos.x += 0.25;
	}
	if (key == GLFW_KEY_J) {
		lightPos.x -= 0.25;
	}
	if (key == GLFW_KEY_I) {
		lightPos.y += 0.25;
	}
	if (key == GLFW_KEY_K) {
		lightPos.y -= 0.25;
	}
	if (key == GLFW_KEY_G) {					// Change material to gold
		Kaa = vec3(0.628281, 0.555802, 0.366065);
		Kdd = vec3(0.75164, 0.60648, 0.22648);
		Kss = vec3(0.24725, 0.24725, 0.0745);
		Nss = 51.2;
	}
	if (key == GLFW_KEY_T) {					// Change material to turqoise
		Kaa = vec3(0.1, 0.18725, 0.1745);
		Kdd = vec3(0.396, 0.74151, 0.69102);
		Kss = vec3(0.297254, 0.30829, 0.306678);
		Nss = 12.8;
	}
	if (key == GLFW_KEY_P) {					// Change material to pearl	(change the w coordinate)
		Kaa = vec3(0.25, 0.20725, 0.20725);
		Kdd = vec3(1, 0.829, 0.829);
		Kss = vec3(11.264);
		Nss = 12.8;
	}
}

void initialize()
{
	// Initialize GLFW
	if (!glfwInit())
	{
		throw runtime_error("Failed to initialize GLFW\n");
	}

	glfwWindowHint(GLFW_SAMPLES, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	// Open a window and create its OpenGL context
	window = glfwCreateWindow(W_WIDTH, W_HEIGHT, TITLE, NULL, NULL);
	if (window == NULL)
	{
		glfwTerminate();
		throw runtime_error(string(string("Failed to open GLFW window.") +
			" If you have an Intel GPU, they are not 3.3 compatible." +
			"Try the 2.1 version.\n"));
	}
	glfwMakeContextCurrent(window);

	// Start GLEW extension handler
	glewExperimental = GL_TRUE;

	// Initialize GLEW
	if (glewInit() != GLEW_OK)
	{
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

	glfwSetKeyCallback(window, pollKeyboard);

	// Enable depth test
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	glDepthFunc(GL_LESS);

	// enable blending
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

	// enable textures
	glEnable(GL_TEXTURE_2D);

	// Log
	logGLParameters();

	// Create camera
	camera = new Camera(window);
}

int main(void)
{
	try
	{
		initialize();
		createContext();
		mainLoop();
		free();
	}
	catch (exception& ex)
	{
		cout << ex.what() << endl;
		getchar();
		free();
		return -1;
	}

	return 0;
}