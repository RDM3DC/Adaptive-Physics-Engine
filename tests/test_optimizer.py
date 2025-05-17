import unittest
import importlib
import sys
import os

# Ensure the src directory is on the path for module discovery
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

class TestOptimizerImport(unittest.TestCase):
    """Basic tests for optimizer module loading."""

    def test_import_optimizer(self):
        """Module should import without raising exceptions."""
        module = importlib.import_module('optimizer')
        self.assertIsNotNone(module)

if __name__ == '__main__':
    unittest.main()
