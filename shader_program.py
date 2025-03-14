class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['default'] = self.get_program('default')
        self.programs['skybox'] = self.get_program('skybox')
        self.programs['advanced_skybox'] = self.get_program('advanced_skybox')

    def get_program(self, shader_program_name):
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        try:
            program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        except Exception as e:
            print("Shader compilation error:", e)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]
