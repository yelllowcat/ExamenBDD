# PyInstaller runtime hook to handle missing curses module
import sys

# Mock the curses module to prevent import errors
class MockCurses:
    def __getattr__(self, name):
        return None

# Only mock on Windows
if sys.platform == 'win32':
    sys.modules['_curses'] = MockCurses()
    sys.modules['curses'] = MockCurses()
