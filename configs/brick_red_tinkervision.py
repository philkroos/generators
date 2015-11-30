# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Tinkervision additions for the RED Brick communication config

packets = []

# This must match TV_STRING_SIZE, e.g. size(api.c:VisionString)
string_size = 30

packets.append({
'type': 'function',
'name': ('VisionIsValid', 'vision_is_valid'),
'elements': [('result', 'int16', 1, 'out')],
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
'name': ('VisionCameraAvailable', 'vision_camera_available'),
'elements': [('result', 'int16', 1, 'out')],
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
'name': ('VisionGetFramesize', 'vision_get_framesize'),
'elements': [('result', 'int16', 1, 'out'),
             ('width', 'uint16', 1, 'out'),
             ('height', 'uint16', 1, 'out')],
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
'elements': [('width', 'uint16', 1, 'in'),
             ('height', 'uint16', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'elements': [('result', 'int16', 1, 'out')],
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
'name': ('VisionRequestFrameperiod', 'vision_request_frameperiod'),
'elements': [('milliseconds', 'uint32', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'name': ('VisionGetFrameperiod', 'vision_get_frameperiod'),
'elements': [('result', 'int16', 1, 'out'),
             ('milliseconds', 'uint32', 1, 'out')],
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
'elements': [('result', 'int16', 1, 'out')],
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
'elements': [('result', 'int16', 1, 'out')],
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
'name': ('VisionNumericalParameterSet', 'vision_numerical_parameter_set'),
'elements': [('id', 'int8', 1, 'in'),
             ('parameter', 'string', string_size, 'in'),
             ('value', 'int32', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'name': ('VisionNumericalParameterGet', 'vision_numerical_parameter_get'),
'elements': [('id', 'int8', 1, 'in'),
             ('parameter', 'string', string_size, 'in'),
              ('result', 'int16', 1, 'out'),
              ('value', 'int32', 1, 'out')],
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
'name': ('VisionStringParameterSet', 'vision_string_parameter_set'),
'elements': [('id', 'int8', 1, 'in'),
             ('parameter', 'string', string_size, 'in'),
             ('value', 'string', string_size, 'in'),
             ('result', 'int16', 1, 'out')],
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
'name': ('VisionStringParameterGet', 'vision_string_parameter_get'),
'elements': [('id', 'int8', 1, 'in'),
             ('parameter', 'string', string_size, 'in'),
             ('result', 'int16', 1, 'out'),
             ('value', 'string', string_size, 'out')],
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
'elements': [('name', 'string', string_size, 'in'),
             ('result', 'int16', 1, 'out'),
             ('id', 'int8', 1, 'out')],
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
'elements': [('id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'elements': [('id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'elements': [('id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'elements': [('id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('name', 'string', string_size, 'out')],
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
'name': ('VisionModuleGetID', 'vision_module_get_id'),
'elements': [('library', 'int16', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('id', 'int8', 1, 'out')],
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
'name': ('VisionModuleIsActive', 'vision_module_is_active'),
'elements': [('id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('active', 'uint8', 1, 'out')],
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
'elements': [('result', 'int16', 1, 'out'),
             ('count', 'uint16', 1, 'out')],
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
'name': ('VisionLibsLoadedCount', 'vision_libs_loaded_count'),
'elements': [('result', 'int16', 1, 'out'),
             ('count', 'uint16', 1, 'out')],
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
'elements': [('number', 'uint16', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('name', 'string', string_size, 'out'),
             ('path', 'string', string_size, 'out')],
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
'name': ('VisionLibParametersCount', 'vision_lib_parameters_count'),
'elements': [('lib', 'string', string_size, 'in'),
             ('result', 'int16', 1, 'out'),
             ('count', 'uint16', 1, 'out')],
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
'elements': [('libname', 'string', string_size, 'in'),
             ('parameter', 'uint16', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('name', 'string', string_size, 'out'),
             ('type', 'uint8', 1, 'out'),
             ('min', 'int32', 1, 'out'),
             ('max', 'int32', 1, 'out'),
             ('default', 'int32', 1, 'out')],
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
'name': ('VisionLibGetUserPrefix', 'vision_lib_get_user_prefix'),
'elements': [('result', 'int16', 1, 'out'),
             ('path', 'string', string_size, 'out')],
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
'name': ('VisionLibSetUserPrefix', 'vision_lib_set_user_prefix'),
'elements': [('path', 'string', string_size, 'in'),
             ('result', 'int16', 1, 'out')],
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
'name': ('VisionLibGetSystemLoadPath', 'vision_lib_get_system_load_path'),
'elements': [('result', 'int16', 1, 'out'),
             ('path', 'string', string_size, 'out')],
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
'elements': [('result', 'int16', 1, 'out')],
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
'elements': [('module_id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('x', 'int32', 1, 'out'),
             ('y', 'int32', 1, 'out'),
             ('width', 'int32', 1, 'out'),
             ('height', 'int32', 1, 'out'),
             ('string', 'string', string_size, 'out')],
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
'elements': [('scene_id', 'int16', 1, 'in'),
             ('module_id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'elements': [('scene_id', 'int16', 1, 'in'),
             ('result', 'int16', 1, 'out')],
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
'name': ('VisionGetErrorDescription', 'vision_get_error_description'),
'elements': [('code', 'int16', 1, 'in'),
             ('description', 'string', string_size, 'out')],
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
'elements': [('id', 'int8', 1, 'out'),
             ('x', 'int32', 1, 'out'),
             ('y', 'int32', 1, 'out'),
             ('width', 'int32', 1, 'out'),
             ('height', 'int32', 1, 'out'),
             ('string', 'string', string_size, 'out')],
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
'elements': [('name', 'string', string_size, 'out'),
             ('path', 'string', string_size, 'out'),
             ('status', 'int8', 1, 'out')],
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
