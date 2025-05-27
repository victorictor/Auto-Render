import bpy
from bpy.props import StringProperty, FloatProperty, PointerProperty

# GET CAMERA 
def _cam_poll(self, obj):
    return obj.type == 'CAMERA'

def register_props():
    # DIRECTORY PROP
    bpy.types.Scene.prop_render_dir = StringProperty(
        name        = "Directory",
        description = "set the location where the images will be saved",
        subtype     = 'DIR_PATH',
        default     = '')

    # INTEVAL PROP
    bpy.types.Scene.prop_render_interval = FloatProperty(
        name        = "",
        description = "Time (in seconds) between each automatic render.",
        default     = 10,
        min         = 1,    
        subtype     = 'TIME_ABSOLUTE',  
        unit        = 'TIME_ABSOLUTE')

    # CAMERA PROP
    bpy.types.Scene.prop_render_cam = PointerProperty(
        name        = "Camera",
        description = "set the camera used in the render",
        type        = bpy.types.Object,   
        poll        = _cam_poll) 

def unregister_props():
    del bpy.types.Scene.prop_render_cam
    del bpy.types.Scene.prop_render_interval
    del bpy.types.Scene.prop_render_dir