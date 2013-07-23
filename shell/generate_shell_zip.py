#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shell ZIP Generator
Copyright (C) 2012-2013 Matthias Bolte <matthias@tinkerforge.com>
Copyright (C) 2011 Olaf Lüke <olaf@tinkerforge.com>

generator_shell_zip.py: Generator for Shell ZIP

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import sys
import os
import shutil
import subprocess
import glob
import re

sys.path.append(os.path.split(os.getcwd())[0])
import common

device = None

def copy_examples_for_zip():
    examples = common.find_examples(device, common.path_binding, 'shell', 'example_', '.sh')
    dest = os.path.join('/tmp/generator/examples/',
                        device.get_category().lower(),
                        device.get_underscore_name())

    if not os.path.exists(dest):
        os.makedirs(dest)

    for example in examples:
        shutil.copy(example[1], dest)

def make_files(device_, directory):
    global device
    device = device_

    copy_examples_for_zip()

def generate(path):
    # Make temporary generator directory
    if os.path.exists('/tmp/generator'):
        shutil.rmtree('/tmp/generator/')
    os.makedirs('/tmp/generator')
    os.chdir('/tmp/generator')

    # Copy examples
    common.generate(path, 'en', make_files, None, None, False)
    shutil.copy(common.path_binding.replace('/generators/shell', '/doc/en/source/Software/example.sh'),
                '/tmp/generator/examples/example_enumerate.sh')

    # Copy bindings and readme
    shutil.copy(path + '/tinkerforge', '/tmp/generator')
    shutil.copy(path + '/tinkerforge-bash-completion.sh', '/tmp/generator')
    shutil.copy(path + '/changelog.txt', '/tmp/generator')
    shutil.copy(path + '/readme.txt', '/tmp/generator')

    # Make zip
    version = common.get_changelog_version(path)
    common.make_zip('shell', '/tmp/generator', path, version)

if __name__ == "__main__":
    generate(os.getcwd())