import glm

class Light:
    def __init__(self, position=(3, 3, -3), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        # Light intensity
        self.Ia = 0.1 * self.color # Ambient
        self.Id = 0.8 * self.color # Diffuse
        self.Is = 1.0 * self.color # Specular