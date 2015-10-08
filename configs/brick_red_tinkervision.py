# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Tinkervision additions for the RED Brick communication config

packets = []

id_t = 'int8'
result_t = 'int16'
scene_t = 'int16'
parameter_t = 'int16'
size_t = 'uint16'
value_t = 'uint16'
coord_t = 'uint16'
big_t = 'uint32'
string_t = 'string'

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
'name': ('VisionPreselectFramesize', 'vision_preselect_framesize'),
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
'elements': [('milliseconds', big_t, 1, 'in'),
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
'name': ('VisionPause', 'vision_pause'),
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
             ('parameter', string_t, 16, 'in'),
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
             ('parameter', string_t, 16, 'in'),
             ('value', parameter_t, 1, 'out'),
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
'name': ('VisionModuleStart', 'vision_module_start'),
'elements': [('name', string_t, 16, 'in'),
             ('id', id_t, 1, 'out'),
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
'name': ('VisionSceneStart', 'vision_scene_start'),
'elements': [('module_id', id_t, 1, 'in'),
             ('scene_id', scene_t, 1, 'out'),
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
'name': ('VisionLocation', 'vision_location'),
'elements': [('id', id_t, 1, 'out'),
             ('x', coord_t, 1, 'out'),
             ('y', coord_t, 1, 'out'),
             ('width', coord_t, 1, 'out'),
             ('height', coord_t, 1, 'out')],
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
