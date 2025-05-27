import bpy, sys

cam_name, out_path = sys.argv[-2:]

scene = bpy.context.scene
scene.camera = bpy.data.objects[cam_name]

scene.render.filepath = out_path
scene.render.image_settings.file_format = 'PNG'    

bpy.ops.render.render(write_still=True)
