import bpy
from .render_logic.timer import toggle_timer

class OT_AutoRender(bpy.types.Operator):
    bl_idname      = "wm.auto_render_operator"
    bl_label       = "Start / Stop Auto Render"
    bl_description = "Turn on automatic rendering"
    
    def execute(self, context):
        scn = context.scene
        # caso nao tenha camera
        if not scn.prop_render_cam: 
            self.report(
                {'ERROR'},
                "No camera defined.\nSelect one in the 'Camera' field.")
            return {'CANCELLED'}
        
        # caso nao tenha pasta
        if not scn.prop_render_dir: 
            self.report(
                {'ERROR'},
                "No directory defined.\nSave the .blend file or "
                "choose a folder in the 'Directory' box. \n")
            return {'CANCELLED'}
        
        toggle_timer() 
        return{'FINISHED'}

classes = (OT_AutoRender,)