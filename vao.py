from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # Cube vao
        self.vaos['cube'] = self.get_vao(program=self.program.programs['default'], vbo = self.vbo.vbos['cube'])
        # Cat vao
        self.vaos['cat'] = self.get_vao(program=self.program.programs['default'], vbo = self.vbo.vbos['cat'])
        # Skybox vao
        self.vaos['skybox'] = self.get_vao(program=self.program.programs['skybox'], vbo = self.vbo.vbos['skybox'])
        # Advanced_Skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(program=self.program.programs['advanced_skybox'], vbo = self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()