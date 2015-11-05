# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Tinkervision additions for the RED Brick communication config

packets = []

id_t = 'int8'
result_t = 'int16'
scene_t = 'int16'
parameter_t = 'int32'
size_t = 'uint16'
value_t = 'int32'
time_t = 'uint32'
string_t = 'string'
# This must match tv::TV_CHAR_ARRAY_SIZE, e.g. size(api.c:VisionString)
string_size = 24;

packets.append({
'type': 'function',
'name': ('VisionCameraAvailable', 'vision_camera_available'),
'elements': [('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionSetFramesize', 'vision_set_framesize'),
'elements': [('width', size_t, 1, 'in'),
             ('height', size_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionStartIdle', 'vision_start_idle'),
'elements': [('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionSetLatency', 'vision_set_latency'),
'elements': [('milliseconds', time_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionGetInvFramerate', 'vision_get_inv_framerate'),
'elements': [('result', result_t, 1, 'out'),
             ('milliseconds', time_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionGetResolution', 'vision_get_resolution'),
'elements': [('result', result_t, 1, 'out'),
             ('width', size_t, 1, 'out'),
             ('height', size_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionStop', 'vision_stop'),
'elements': [('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionRestart', 'vision_restart'),
'elements': [('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionParameterSet', 'vision_parameter_set'),
'elements': [('id', id_t, 1, 'in'),
             ('parameter', string_t, string_size, 'in'),
             ('value', parameter_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionParameterGet', 'vision_parameter_get'),
'elements': [('id', id_t, 1, 'in'),
             ('parameter', string_t, string_size, 'in'),
             ('result', result_t, 1, 'out'),
             ('value', parameter_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionModuleStart', 'vision_module_start'),
'elements': [('name', string_t, string_size, 'in'),
             ('result', result_t, 1, 'out'),
             ('id', id_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionModuleStop', 'vision_module_stop'),
'elements': [('id', id_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionModuleRestart', 'vision_module_restart'),
'elements': [('id', id_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionModuleRemove', 'vision_module_remove'),
'elements': [('id', id_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionModuleGetName', 'vision_module_get_name'),
'elements': [('id', id_t, 1, 'in'),
             ('result', result_t, 1, 'out'),
             ('name', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibsCount', 'vision_libs_count'),
'elements': [('result', result_t, 1, 'out'),
             ('count', size_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibNamePath', 'vision_lib_name_path'),
'elements': [('number', size_t, 1, 'in'),
             ('result', result_t, 1, 'out'),
             ('name', string_t, string_size, 'out'),
             ('path', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibParameterCount', 'vision_lib_parameter_count'),
'elements': [('lib', string_t, string_size, 'in'),
             ('result', result_t, 1, 'out'),
             ('count', size_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibParameterDescribe', 'vision_lib_parameter_describe'),
'elements': [('lib', string_t, string_size, 'in'),
             ('count', size_t, 1, 'in'),
             ('name', string_t, string_size, 'in'),
             ('result', result_t, 1, 'out'),
             ('min', parameter_t, 1, 'out'),
             ('max', parameter_t, 1, 'out'),
             ('default', parameter_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibUserLoadPath', 'vision_lib_user_load_path'),
'elements': [('result', result_t, 1, 'out'),
             ('path', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibSystemLoadPath', 'vision_lib_system_load_path'),
'elements': [('result', result_t, 1, 'out'),
             ('path', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionSetLibUserLoadPath', 'vision_set_lib_user_load_path'),
'elements': [('result', result_t, 1, 'out'),
             ('path', string_t, string_size, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionRemoveAllModules', 'vision_remove_all_modules'),
'elements': [('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionLibUserLoadPath', 'vision_lib_user_load_path'),
'elements': [('result', result_t, 1, 'out'),
             ('path', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionModuleResult', 'vision_module_result'),
'elements': [('module_id', id_t, 1, 'in'),
             ('result', result_t, 1, 'out'),
             ('x', value_t, 1, 'out'),
             ('y', value_t, 1, 'out'),
             ('width', value_t, 1, 'out'),
             ('height', value_t, 1, 'out'),
             ('string', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionSceneAdd', 'vision_scene_add'),
'elements': [('scene_id', scene_t, 1, 'in'),
             ('module_id', id_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionSceneRemove', 'vision_scene_remove'),
'elements': [('scene_id', scene_t, 1, 'in'),
             ('result', result_t, 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'callback',
'name': ('VisionModule', 'vision_module'),
'elements': [('id', id_t, 1, 'out'),
             ('x', value_t, 1, 'out'),
             ('y', value_t, 1, 'out'),
             ('width', value_t, 1, 'out'),
             ('height', value_t, 1, 'out'),
             ('string', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
""",
'de':
"""
"""
}]
})

packets.append({
'type': 'callback',
'name': ('VisionLibraries', 'vision_libraries'),
'elements': [('name', string_t, string_size, 'out'),
             ('path', string_t, string_size, 'out'),
             ('status', string_t, string_size, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
""",
'de':
"""
"""
}]
})
