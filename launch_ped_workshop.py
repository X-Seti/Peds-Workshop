#!/usr/bin/env python3
#this belongs in root /launch_ped_workshop.py - Version: 1
# X-Seti - October 21 2026 - Ped Workshop - Root Launcher

import os
import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))
if sys.platform.startswith('linux'):           # NVIDIA on Wayland: X11 / GLX backend
    os.environ['QT_QPA_PLATFORM'] = 'xcb'

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    from apps.components.Ped_Workshop.ped_workshop import open_ped_workshop
    app = QApplication(sys.argv)
    ws = open_ped_workshop(None, sys.argv[1] if len(sys.argv) > 1 else '')
    ws.setWindowTitle("Ped Workshop - Standalone")
    sys.exit(app.exec())
