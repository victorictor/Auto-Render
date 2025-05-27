import bpy
from .render import _spawn_background_render

_is_running = False

# RENDER AT TIME
def _timer():
    if not _is_running:
        return None
    _spawn_background_render() #do render
    return bpy.context.scene.prop_render_interval

# ON/OFF OF TIMER
def toggle_timer():
    global _is_running
    if _is_running:
        _is_running = False
    else:
        _is_running = True
        bpy.app.timers.register(_timer, first_interval=0)

# RESTART TIMER ON unregister
def stop_timer_on_disable():
    global _is_running
    _is_running = False  
