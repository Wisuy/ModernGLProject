from model import *

class Scene :
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # Skybox
        self.skybox = AdvancedSkyBox(app)

    def add_objects(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_objects
        # add(Cube(app))
        # add(Cube(app, tex_id=1, pos=(-2.5, 0, 0), rot=(45, 0, 0), scale=(1, 2, 1)))
        # add(Cube(app, tex_id=2, pos=(2.5, 0, 0), rot=(0, 0, 45), scale=(1, 1, 2)))
        
        # Street
        for i in range(20):
            add(Cube(app, pos=(-i * 2, 0, 0), tex_id='asphalt'))
            add(Cube(app, pos=(-i * 2, 0, -2), tex_id='asphalt'))
            add(Cube(app, pos=(-i * 2, 0, -4), tex_id='asphalt'))
            add(Cube(app, pos=(i * 2, 0, 0), tex_id='asphalt'))
            add(Cube(app, pos=(i * 2, 0, -2), tex_id='asphalt'))
            add(Cube(app, pos=(i * 2, 0, -4), tex_id='asphalt'))
        for i in range(20):
            add(Cube(app, pos=(-i * 2, 0, -40), tex_id='asphalt'))
            add(Cube(app, pos=(-i * 2, 0, -42), tex_id='asphalt'))
            add(Cube(app, pos=(-i * 2, 0, -44), tex_id='asphalt'))
            add(Cube(app, pos=(i * 2, 0, -40), tex_id='asphalt'))
            add(Cube(app, pos=(i * 2, 0, -42), tex_id='asphalt'))
            add(Cube(app, pos=(i * 2, 0, -44), tex_id='asphalt'))
        for i in range(23):
            add(Cube(app, pos=(-40, 0, -i * 2), tex_id='asphalt'))
            add(Cube(app, pos=(-42, 0, -i * 2), tex_id='asphalt'))
            add(Cube(app, pos=(-44, 0, -i * 2), tex_id='asphalt'))
        for i in range(23):
            add(Cube(app, pos=(40, 0, -i * 2), tex_id='asphalt'))
            add(Cube(app, pos=(42, 0, -i * 2), tex_id='asphalt'))
            add(Cube(app, pos=(44, 0, -i * 2), tex_id='asphalt'))
            
        # Buildings
        for i in range(7):
            add(Cube(app, pos=(30, i * 2, 7), tex_id='building'))
            add(Cube(app, pos=(-30, i * 2, 7), tex_id='building'))
            add(Cube(app, pos=(-5, i * 2, -55), tex_id='building'))
            add(Cube(app, pos=(6, i * 2, -24), tex_id='building'))
        for i in range(3):
            add(Cube(app, pos=(18, i * 2, -30), tex_id='building'))
            add(Cube(app, pos=(-30, i * 2, 7), tex_id='building'))
            add(Cube(app, pos=(-4, i * 2, -30), tex_id='building'))
            add(Cube(app, pos=(-36, i * 2, -20), tex_id='building'))
        for i in range(5):
            add(Cube(app, pos=(6, i * 2, -14), tex_id='building'))
            add(Cube(app, pos=(-30, i * 2, -32), tex_id='building'))


        n, s = 60, 2
        # Grass
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # Columns
        for i in range(15):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))
            
        # Cat
        add(Cat(app, pos=(0, -1, -10)))
        
        # Moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(1, 1, 1), tex_id=1)
        add(self.moving_cube)

         

        #def render(self):
        #    for obj in self.objects:
        #        obj.render() 
            # Must be rendered last to achieve better performance
        #    self.skybox.render()

    def update(self):
        self.moving_cube.rot.xyz = self.app.time