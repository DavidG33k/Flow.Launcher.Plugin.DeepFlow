# -*- coding: utf-8 -*-
"""

DeepFlow: DeepL Plugin for Flow Launcher.

Dev By Davide Gena (https://github.com/DavidG33k)

"""

import os, sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from plugin.Engine import deepL

if __name__ == "__main__":
    deepL()
