import bpy, os, tempfile, subprocess
from .utils import timestamp, blend_name

_temp_blend = None
# MAKE THE RENDER FROM TEMP .blend ON BACKGROUND
def _spawn_background_render():
    global _temp_blend
    scn = bpy.context.scene

    # TEMP .blend
    if _temp_blend is None:
        _temp_blend = tempfile.mktemp(suffix=".blend")           # save temp .blend, and
                                                                 # keeps render updated
    bpy.ops.wm.save_as_mainfile(filepath=_temp_blend, copy=True) # rename old temp

    # OUTPUT DIRECTORY
    raw_dir = scn.prop_render_dir       # input dir
    out_dir = bpy.path.abspath(raw_dir) # readable input dir
    os.makedirs(out_dir, exist_ok=True)
    file_out = os.path.join(
        out_dir, f"{blend_name()}_{timestamp()}.png") # file name

    # OPEN TERMINAL AND RENDER IT 
    cmd = [
        bpy.app.binary_path,                     # blender.exe 
        "-b", _temp_blend,                       # open temp .blend without UI
        "--factory-startup",                     # fast inicialize, without add-ons
        "-P", os.path.join(os.path.dirname(__file__), "render_worker.py"),
        "--", scn.prop_render_cam.name, file_out # render the temp .blend scene
    ]

    # seting low priority on windows
    creation = getattr(subprocess, "BELOW_NORMAL_PRIORITY_CLASS", 0)
    subprocess.Popen(cmd, creationflags=creation)
