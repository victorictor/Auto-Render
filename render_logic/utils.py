import os, bpy
from datetime import datetime

'''' # CANCELED
# return DIRECTORY OF A .BLEND FILE IF ITS SAVED
def default_dir():
    if bpy.data.is_saved:
        blend_dir = os.path.dirname(bpy.data.filepath)
        return os.path.join(blend_dir, "render images")
    return ''
'''

# return TIME AND DATE IN STRING
def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")

# return NAME OF .BLEND FILE
def blend_name():
    path = bpy.data.filepath
    if path:
        return os.path.splitext(os.path.basename(path))[0] 
    else: "Untitled"