#!/usr/bin/env python3
"""Test that tilde expansion works correctly for path configuration variables."""

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


class TestConfigTildeExpansion(unittest.TestCase):
    """Test tilde expansion in configuration paths."""
    
    def test_expand_path_with_tilde(self):
        """Test that expand_path correctly expands tilde to home directory."""
        # Import inside test to avoid side effects
        from voice_mode.config import expand_path
        
        # Test tilde expansion
        result = expand_path("~/test/path")
        expected = Path.home() / "test" / "path"
        self.assertEqual(result, expected)
    
    def test_expand_path_with_env_var(self):
        """Test that expand_path correctly expands environment variables."""
        from voice_mode.config import expand_path
        
        # Set a test environment variable
        with patch.dict(os.environ, {"TEST_VAR": "/custom/path"}):
            result = expand_path("$TEST_VAR/subdir")
            expected = Path("/custom/path/subdir")
            self.assertEqual(result, expected)
    
    def test_expand_path_with_tilde_and_env_var(self):
        """Test that expand_path handles both tilde and env vars."""
        from voice_mode.config import expand_path
        
        with patch.dict(os.environ, {"SUBDIR": "mydir"}):
            result = expand_path("~/$SUBDIR/test")
            expected = Path.home() / "mydir" / "test"
            self.assertEqual(result, expected)
    
    def test_config_paths_with_tilde(self):
        """Test that configuration paths properly expand tilde."""
        # Set environment variables with tilde
        test_env = {
            "BUMBA_BASE_DIR": "~/test-voicemode",
            "BUMBA_MODELS_DIR": "~/models",
            "BUMBA_WHISPER_MODEL_PATH": "~/whisper",
            "BUMBA_KOKORO_MODELS_DIR": "~/kokoro/models",
            "BUMBA_KOKORO_CACHE_DIR": "~/kokoro/cache"
        }
        
        with patch.dict(os.environ, test_env, clear=False):
            # Import config module (this will use the patched environment)
            import importlib
            import voice_mode.config as config
            importlib.reload(config)
            
            # Check that all paths are properly expanded
            home = Path.home()
            self.assertEqual(config.BASE_DIR, home / "test-voicemode")
            self.assertEqual(config.MODELS_DIR, home / "models")
            self.assertEqual(config.WHISPER_MODEL_PATH, home / "whisper")
            self.assertEqual(config.KOKORO_MODELS_DIR, home / "kokoro" / "models")
            self.assertEqual(config.KOKORO_CACHE_DIR, home / "kokoro" / "cache")
    
    def test_config_paths_without_tilde(self):
        """Test that paths without tilde work normally."""
        # Use a temp directory that actually exists
        with tempfile.TemporaryDirectory() as tmpdir:
            test_env = {
                "BUMBA_BASE_DIR": tmpdir,
                "BUMBA_MODELS_DIR": f"{tmpdir}/models"
            }
            
            with patch.dict(os.environ, test_env, clear=False):
                import importlib
                import voice_mode.config as config
                importlib.reload(config)
                
                self.assertEqual(config.BASE_DIR, Path(tmpdir))
                self.assertEqual(config.MODELS_DIR, Path(tmpdir) / "models")


if __name__ == "__main__":
    unittest.main()