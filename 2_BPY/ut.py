import bpy

#Select objects by name
def select(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select = True

def select(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select = True

class sel:
    #function class for selected objects
    def translate(v):
        bpy.ops.transform.translate(value = v, constraint_axis=(True, True, True))
    
    def scale(v):
        bpy.ops.transform.resize(value = v, constraint_axis=(True, True, True))
    
    def rotate_x(v):
        bpy.ops.transform.rotate(value = v, axis=(1, 0, 0))

    def rotate_y(v):
        bpy.ops.transform.rotate(value = v, axis=(0, 1, 0))

    def rotate_z(v):
        bpy.ops.transform.rotate(value = v, axis=(0, 0, 1))

class act:
    
    def location(v):
        bpy.context.object.location = v
    
    def scale(v):
        bpy.context.object.scale = v
    
    def rotation(v):
        bpy.context.object.rotation_euler = v
    
    def rename(objName):
        bpy.context.object.name = objName

class spec:
    
    def scale(objName, v):
        bpy.data.objects[objName].scale = v
    
    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v

class create:
    
    def cube(objName):
        bpy.ops.mesh.primitive_cube_add(size = 0.5, location=(0, 0, 0))
        act.rename(objName)
    
    def sphere(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(size = 0.5, location=(0, 0, 0))
        act.rename(objName)

    def cone(objName):
        bpy.ops.mesh.primitive_cone_add(radius1 = 0.5, location=(0, 0, 0))
        act.rename(objName)
    
    def delete(objName):
        select(objName)
        bpy.ops.object.delete(use_global = False)

    def delete_all(objName):
        if(len(bpy.data.objects) != 0):
            bpy.ops.object.select_all(action = 'SELECT')
            bpy.ops.object.delete(use_global = False)
            
if __name__ = "__main__":
    create.cube('perfectcube')