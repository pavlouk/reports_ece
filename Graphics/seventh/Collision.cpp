#include "Collision.h"
#include "Box.h"
#include "Sphere.h"
using namespace glm;

void handleBoxSphereCollision(Box& box, Sphere& sphere);
bool checkForBoxSphereCollision(glm::vec3& pos, const float& r,
    const float& size, glm::vec3& n);

void handleBoxSphereCollision(Box& box, Sphere& sphere) {
    vec3 n; //trick me by reference sthn apo katw function 
    if (checkForBoxSphereCollision(sphere.x, sphere.r, box.size, n)) {
        // Task 2b: define the velocity of the sphere after the collision
		sphere.P = sphere.P - 2.0f * dot(sphere.P, n) * n; //me mono to v den kanei kroush akrivws
    }
}

bool checkForBoxSphereCollision(vec3& pos, const float& r, const float& size, vec3& n) {
    if (pos.x - r <= 0) {
        //correction
        float dis = -(pos.x - r);
        pos = pos + vec3(dis, 0, 0);

        n = vec3(-1, 0, 0);
    } else if (pos.x + r >= size) {
        //correction
        float dis = size - (pos.x + r);
        pos = pos + vec3(dis, 0, 0);

        n = vec3(1, 0, 0);
    } else if (pos.y - r <= 0) {
        //correction
        float dis = -(pos.y - r);
        pos = pos + vec3(0, dis, 0);

        n = vec3(0, -1, 0);
    } else if (pos.y + r >= size) {
        //correction
        float dis = size - (pos.y + r);
        pos = pos + vec3(0, dis, 0);

        n = vec3(0, 1, 0);
    } else if (pos.z - r <= 0) {
        //correction
        float dis = -(pos.z - r);
        pos = pos + vec3(0, 0, dis);

        n = vec3(0, 0, -1);
    } else if (pos.z + r >= size) {
        //correction
        float dis = size - (pos.z + r);
        pos = pos + vec3(0, 0, dis);

        n = vec3(0, 0, 1);
    } else {
        return false;
    }
    return true;
}