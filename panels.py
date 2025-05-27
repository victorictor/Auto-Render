import bpy
from .render_logic import timer

# PANEL
class VIEW3D_PT_AutoRender(bpy.types.Panel):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_category    = "Auto Render"
    bl_label       = "settings"

    def draw(self, context):
        layout = self.layout
        scn  = context.scene

        # DIRECTORY 
        layout.prop(scn, "prop_render_dir")

        # CAMERA
        layout.prop(scn, "prop_render_cam")

        # INTERVAL 
        split = layout.split(factor=0.22)
        split.label(text="Interval:")
        split.prop(scn, "prop_render_interval")
        
        row = layout.row()
        row.scale_y = 3.5

        # START   
        is_running = timer._is_running      # RENDER INTERVAL TIMER RUNNING               
        layout.operator("wm.auto_render_operator",
            text="Stop" if is_running else "Start Auto Render",
            depress= is_running)
        
classes = (VIEW3D_PT_AutoRender,)