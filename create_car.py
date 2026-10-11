import bpy
import bmesh
import math

def create_car():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    mesh = bpy.data.meshes.new("CarBodyMesh")
    obj = bpy.data.objects.new("CarBody", mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    bm = bmesh.new()
    verts = [
        (0.0, -2.3, 0.1), (0.7, -2.2, 0.1), (0.9, -2.1, 0.1),
        (0.0, -2.2, 0.3), (0.7, -2.1, 0.35), (0.85, -2.0, 0.4),
        (0.0, -1.2, 0.55), (0.7, -1.2, 0.6), (0.9, -1.0, 0.65),
        (0.0, -0.2, 1.05), (0.6, -0.2, 1.0), (0.8, -0.1, 0.9),
        (0.0, 0.6, 1.1), (0.55, 0.6, 1.05), (0.75, 0.6, 0.95),
        (0.0, 1.5, 0.8), (0.5, 1.5, 0.8), (0.75, 1.5, 0.8),
        (0.0, 2.3, 0.5), (0.8, 2.2, 0.5), (0.95, 2.1, 0.5),
        (0.0, 2.4, 0.2), (0.8, 2.3, 0.2), (0.9, 2.2, 0.2),
        (1.0, -0.8, 0.15), (1.05, 0.0, 0.15), (1.0, 1.2, 0.15),
        (1.0, -0.8, 0.5), (1.05, 0.0, 0.55), (1.0, 1.2, 0.6),
        (0.0, 2.2, 1.2), (0.8, 2.1, 1.2), (0.9, 2.0, 1.15),
        (0.8, 2.1, 0.8)
    ]

    bm_verts = []
    for v in verts:
        bm_verts.append(bm.verts.new(v))

    faces = [
        (0, 1, 4, 3), (1, 2, 5, 4),
        (3, 4, 7, 6), (4, 5, 8, 7),
        (6, 7, 10, 9), (7, 8, 11, 10),
        (9, 10, 13, 12), (10, 11, 14, 13),
        (12, 13, 16, 15), (13, 14, 17, 16),
        (15, 16, 19, 18), (16, 17, 20, 19),
        (18, 19, 22, 21), (19, 20, 23, 22),
        (2, 24, 25, 5), (5, 25, 28, 8),
        (8, 28, 29, 11), (11, 29, 26, 14),
        (14, 26, 20, 17),
        (2, 24, 27, 1), (24, 25, 28, 27),
        (25, 26, 29, 28), (26, 23, 22, 29),
        (19, 20, 33, 19),
        (30, 31, 32, 30)
    ]

    for f in faces:
        try:
            unique_verts = []
            for idx in f:
                if bm_verts[idx] not in unique_verts:
                    unique_verts.append(bm_verts[idx])
            if len(unique_verts) >= 3:
                bm.faces.new(unique_verts)
        except Exception as e:
            pass

    bm.to_mesh(mesh)
    bm.free()

    mirror_mod = obj.modifiers.new(name="Mirror", type='MIRROR')
    mirror_mod.use_axis[0] = True
    mirror_mod.use_clip = True
    subsurf_mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
    subsurf_mod.levels = 3
    subsurf_mod.render_levels = 3

    for p in mesh.polygons:
        p.use_smooth = True

    bpy.ops.object.modifier_apply(modifier="Mirror")
    bpy.ops.object.modifier_apply(modifier="Subdivision")

    wheel_positions = [
        (0.9, -1.4, 0.35),
        (-0.9, -1.4, 0.35),
        (0.9, 1.4, 0.38),
        (-0.9, 1.4, 0.38)
    ]

    for i, pos in enumerate(wheel_positions):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.35 if "Front" in ["Front", "Rear"][i//2] else 0.38,
            depth=0.3,
            location=pos,
            rotation=(math.pi/2, 0, 0)
        )
        wheel = bpy.context.active_object
        wheel.name = f"Wheel_{i}"
        for p in wheel.data.polygons:
            p.use_smooth = True
        wheel.select_set(True)

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.join()
    bpy.ops.wm.obj_export(filepath="jesko_car.obj", export_selected_objects=True)

if __name__ == "__main__":
    create_car()
