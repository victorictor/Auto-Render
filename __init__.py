bl_info = {
    "name":        "Auto Render",
    "author":      "Valfredo Victor",
    "version":     (1, 3, 0),
    "blender":     (4, 4, 0),
    "location":    "3D View · Sidebar",
    "description": "This addon creates a render by the scene camera every set second",
    "category":    "Render",
}

import bpy
from .operators import classes as _op
from .panels    import classes as _ui
from .props     import register_props, unregister_props
from .render_logic.timer import stop_timer_on_disable

_classes = (*_op, *_ui)

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    register_props()

def unregister():
    stop_timer_on_disable()         #RESTART THE TIMER
    unregister_props()
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
    
if __name__ == "__main__":
    register()