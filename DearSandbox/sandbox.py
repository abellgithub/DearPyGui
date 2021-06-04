import dearpygui.core as dpg
import dearpygui.simple as smpl
import dearpygui.contexts as cxt

def event_handler(sender, data):
    print(sender, "\t", data)

with cxt.handler_registry(show=False):

    dpg.add_key_down_handler(dpg.mvKey_A, callback=event_handler)
    dpg.add_key_release_handler(dpg.mvKey_B, callback=event_handler)
    dpg.add_key_press_handler(dpg.mvKey_C, callback=event_handler)
    dpg.add_mouse_wheel_handler(callback=event_handler)
    dpg.add_mouse_click_handler(-1, callback=event_handler)
    dpg.add_mouse_double_click_handler(-1, callback=event_handler)
    dpg.add_mouse_release_handler(-1, callback=event_handler)
    dpg.add_mouse_drag_handler(0, 10.0, callback=event_handler)
    dpg.add_mouse_down_handler(-1, callback=event_handler)
    dpg.add_mouse_move_handler(callback=event_handler)
    

dpg.add_font("google", "../../Resources/NotoSerifCJKjp-Medium.otf", 20)
dpg.set_font("google", 20)

dpg.add_texture_container(id="mvTextureContainer")
dpg.add_static_texture(100, 100, [], parent="mvTextureContainer", file="INTERNAL_DPG_FONT_ATLAS", id="INTERNAL_DPG_FONT_ATLAS")

# temporary, just to ensure the font atlas is ready
# for the demo.
import dearpygui.demo as demo

demo.show_demo()

with cxt.window(label="Drag Drop Testing"):

    def drag_callback(sender, data):
        dpg.set_value("source name", sender)

    def drop_callback(sender, data):
        print(sender, "\t", data)

    b1 = dpg.add_button(label="Source Button", drag_callback=drag_callback)
    b2 = dpg.add_button(label="Target1 Button", drop_callback=drop_callback)
    b3 = dpg.add_button(label="Target2 Button", drop_callback=drop_callback, payload_type="fishy")
    
    with cxt.drag_payload(parent=b1, payload_type="fishy", drag_data=5):
        dpg.add_text("none", label="Source: ", id="source name")

smpl.start_dearpygui()