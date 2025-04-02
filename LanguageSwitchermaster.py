import bpy

bl_info = {
    "name": "Language Switcher",
    "author": "Modified by @iemon_kun",
    "version": (1, 0),
    "blender": (4, 3, 2),
    "description": "Switch between selected UI languages in Blender.",
    "location": "Shortcut: F19 key",
    "category": "System"
}

class LanguageSwitcherPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    available_languages = [
        ("en_US", "English", ""),
        ("ja_JP", "Japanese", ""),
        ("ca_AD", "Catala", ""),
        ("es", "Spanish", ""),
        ("fr_FR", "French", ""),
        ("sk_SK", "Slovencina", ""),
        ("de_DE", "German", ""),
        ("zh_HANS", "Chinese (Simplified)", ""),
        ("ko_KR", "Korean", "")
    ]

    lang_A: bpy.props.EnumProperty(
        name="Primary Language",
        description="First language for switching",
        items=available_languages,
        default="ja_JP"
    )

    lang_B: bpy.props.EnumProperty(
        name="Secondary Language",
        description="Second language for switching",
        items=available_languages,
        default="en_US"
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Select UI languages for switching:")
        layout.prop(self, "lang_A")
        layout.prop(self, "lang_B")

class OBJECT_OT_language_switch(bpy.types.Operator):
    """Switch between selected UI languages"""
    bl_idname = "object.language_switch"
    bl_label = "Switch UI Language"

    def execute(self, context):
        prefs = bpy.context.preferences.view
        addon_prefs = bpy.context.preferences.addons[__name__].preferences

        lang_A = addon_prefs.lang_A
        lang_B = addon_prefs.lang_B
        current_lang = prefs.language

        if current_lang == lang_A:
            prefs.language = lang_B
        elif current_lang == lang_B:
            prefs.language = lang_A
        else:
            self.report({'WARNING'}, f"Unsupported language: {current_lang}. Set to {lang_A} or {lang_B} first.")
            return {'CANCELLED'}
        
        prefs.use_translate_interface = True
        prefs.use_translate_tooltips = True
        return {'FINISHED'}

def register():
    bpy.utils.register_class(LanguageSwitcherPreferences)
    bpy.utils.register_class(OBJECT_OT_language_switch)
    
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Window", space_type="EMPTY")
        km.keymap_items.new('object.language_switch', 'F19', 'PRESS')

def unregister():
    bpy.utils.unregister_class(LanguageSwitcherPreferences)
    bpy.utils.unregister_class(OBJECT_OT_language_switch)
    
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["Window"]
        for kmi in km.keymap_items:
            if kmi.idname == 'object.language_switch':
                km.keymap_items.remove(kmi)
                break

if __name__ == "__main__":
    register()
