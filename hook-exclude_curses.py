# PyInstaller hook to exclude curses module
from PyInstaller.utils.hooks import collect_submodules

# Exclude curses-related modules
excludedimports = ['_curses', 'curses', 'curses.ascii', 'curses.textpad']
