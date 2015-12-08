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
Check if the library is valid. Should be called once before usage.
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
Check if any camera device is available.
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionCameraIDAvailable', 'vision_camera_id_available'),
'elements': [('device', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Check if a specific camera device is available.
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionCameraIDSelect', 'vision_camera_id_select'),
'elements': [('device', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
If several cameras are available, select the preferred one.  If that device
is not available, another one may still be used.
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
Request the resolution of the camera frames.  This can only be called once
the camera is active, so in particular, if the resolution needs to be known
before a module can be started, vision_start_idle() must be called.
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
Selects a framesize WxH.
This will temporarily stop and restart all active modules.
If the requested framesize is not available, the settings will be restored
to the last valid settings, if any.  If no module is running, the camera
will just be tested.
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
Starts a dummy module keeping the Api up and running even if no 'real' module
is active.  This can be used to block the camera or if the resolution has to
be known before any module is running.  Subsequent calls will not start
another dummy.
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
Set the minimum inverse frame frequency. Vision modules registered
and started in the api will be executed sequentially during one
execution loop. The execution latency set here is the minimum
delay between two loops, i.e. the minimum inverse framerate
(frames are grabbed once at the beginning of each loop).
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
Get the effective frameperiod, which can be larger than the frameperiod
requested.
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
Pause Tinkervision, deactivating (but not disabling) every module.  The camera will
be released and no further callbacks will be executed, but on vision_restart(), the Api
will be found in the exact same state as left (assuming that the camera can
be acquired again).
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
Restart Tinkervision from paused state, initiated through call to vision_stop().
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
Set the value of a numerical parameter of a specific module.
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
Get the value of a numerical parameter of a specific module.
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
Set the value of a string parameter of a specific module.
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
Get the value of a string parameter of a specific module.
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
Start a vision module identified by its library name.
The requested module will be loaded and started if it is found in one of the
available library search paths (system/user).
On success, it will be assigned a unique id.
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
Disable a module without removing it.
A disabled module won't be executed, but it is still available for
configuration or reactivation. The associated camera will be released if it
is not used by other modules.
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
Restart a module that has been stopped with module_stop().
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
Deactivate and remove a module.
The id of a removed module is invalid afterwards.
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
Get the name of a loaded module.
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
Retrieve the id of a loaded library.
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
Check if a loaded module is active, i.e. actually running.
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
Get the number of currently available libraries.
This can be used to iterate through all libraries using
vision_lib_name_path().
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
Retrieve the number of loaded libraries.
The result can be used with vision_module_get_id().
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
Get the name and load path of an available library.
Pass a number smaller then vision_libs_count.
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
Get the number of parameters a library supports.
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
Get the properties of a parameter from a library. type is 0 for numeric parameters,
1 for string parameters. min, max, default are only valid in the first case.
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
Access the currently set user paths prefix.
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
Set the user paths prefix from an existing path. The directory has to
provide the subdirectories lib (path searched for user modules), data
(default path to store or load data or frames from) and scripts (path used to load
python scripts from).
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
Access the fixed system module load path.
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
Disable, remove and destroy all modules.
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
Get the result of the latest execution of a given module.
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionSceneStart', 'vision_scene_start'),
'elements': [('module_id', 'int8', 1, 'in'),
             ('result', 'int16', 1, 'out'),
             ('scene_id', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Start a new scene given a loaded module.
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
Add a module to an existing scene.
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
Remove a scene without affecting the associated modules.
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
Get a string representation of a result code. All api functions return 0 on success,
and a negative value on error.
"""
}]
})

packets.append({
'type': 'function',
'name': ('VisionGetBufferedResult', 'vision_get_buffered_result'),
'elements': [('result', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
If any vision method returned 1, the requested operation took too long and is running
in the background.  This method can then be called until a different result is
returned.
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
Callback for changes in the module system. Whenever a module is added to or removed
from one the valid paths (system/user), this will be called with the module name,
the path, and the status, where 1 means created, -1 means removed.
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
Callback for the result of a module's execution. Which values are set in the callback
is module specific. The convention is that unset numerical values are -1, the string
if unset is empty. x and y set would describe a point, x, y, width and height describes
a rectangular area. string, if set, can be anything, e.g. the name of a stored frame.
"""
}]
})
