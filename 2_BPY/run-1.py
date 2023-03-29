import bpy
for k in range(5):
    for j in range(5):
        for i in range(5):
            bpy.ops.mesh.primitive_cube_add(size = 0.5, enter_editmode=False, align='WORLD', location=(i, j, k), scale=(1, 1, 1))