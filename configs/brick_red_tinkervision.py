# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Tinkervision additions for the RED Brick communication config

packets = []

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
'name': ('VisionPreselectFramesize', 'vision_preselect_framesize'),
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
'name': ('VisionSetLatency', 'vision_set_latency'),
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
'name': ('VisionGetResolution', 'vision_get_resolution'),
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
'name': ('VisionPause', 'vision_pause'),
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
'name': ('VisionQuit', 'vision_quit'),
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
'name': ('VisionPauseID', 'vision_pause_id'),
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
'name': ('VisionRestartID', 'vision_restart_id'),
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
'name': ('VisionSceneStart', 'vision_scene_start'),
'elements': [('module_id', 'int8', 1, 'in'),
             ('scene_id', 'int16', 1, 'out'),
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
'name': ('VisionColormatchStart', 'vision_colormatch_start'),
'elements': [('id', 'int8', 1, 'in'),
             ('min_hue', 'uint8', 1, 'in'),
             ('max_hue', 'uint8', 1, 'in'),
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
'name': ('VisionColormatchStop', 'vision_colormatch_stop'),
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
'name': ('VisionColormatchGet', 'vision_colormatch_get'),
'elements': [('id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('min_hue', 'uint8', 1, 'out'),
             ('max_hue', 'uint8', 1, 'out')],
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
'name': ('VisionColormatch', 'vision_colormatch'),
'elements': [('id', 'int8', 1, 'out'),
             ('x', 'uint16', 1, 'out'),
             ('y', 'uint16', 1, 'out')],
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
