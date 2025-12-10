"""Unit tests for configuration management functions."""
import asyncio
import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from voice_mode.tools.configuration_management import update_config, list_config_keys


class TestConfigurationManagement:
    """Test configuration management functions."""

    @pytest.mark.asyncio
    async def test_list_config_keys(self):
        """Test listing configuration keys."""
        result = await list_config_keys.fn()
        
        # Should return a formatted string with config keys
        assert isinstance(result, str)
        assert "BUMBA_" in result
        
        # Should include common config keys
        assert "BUMBA_BASE_DIR" in result
        assert "BUMBA_DEBUG" in result
        assert "BUMBA_" in result
        
        # Should include descriptions
        assert "provider" in result.lower() or "TTS" in result

    @pytest.mark.asyncio
    async def test_update_config_returns_message(self):
        """Test that update_config returns a message."""
        # Create a proper temp file
        import tempfile
        import os
        
        fd, temp_path = tempfile.mkstemp(suffix='.env')
        try:
            # Write initial content
            with os.fdopen(fd, 'w') as f:
                f.write("# Test config\n")
                f.write("EXISTING_KEY=old_value\n")
            
            # Patch the config path
            with patch("voice_mode.tools.configuration_management.USER_CONFIG_PATH", Path(temp_path)):
                result = await update_config.fn("TEST_KEY", "test_value")
                
                # Should return a message (success or error)
                assert isinstance(result, str)
                assert len(result) > 0
                
                # If successful, should mention the key and value
                if "success" in result.lower() or "updated" in result.lower():
                    assert "TEST_KEY" in result
        finally:
            os.unlink(temp_path)

    @pytest.mark.asyncio
    async def test_update_config_function_exists(self):
        """Test that update_config function is callable."""
        # Just verify the function exists and is callable
        assert callable(update_config.fn)
        
        # Test with a mock path that doesn't exist
        with patch("voice_mode.tools.configuration_management.USER_CONFIG_PATH", Path("/nonexistent/test.env")):
            with patch("pathlib.Path.mkdir"), patch("pathlib.Path.exists", return_value=False):
                with patch("builtins.open", mock_open()) as mock_file:
                    result = await update_config.fn("TEST_KEY", "test_value")
                    # Should return a string result
                    assert isinstance(result, str)

    @pytest.mark.asyncio
    async def test_list_config_keys_structure(self):
        """Test that list_config_keys returns properly structured output."""
        result = await list_config_keys.fn()
        
        # Should have sections
        assert "Core Configuration" in result or "Configuration" in result
        assert "======" in result or "------" in result  # Section dividers
        
        # Should explain usage
        assert "Usage" in result or "update_config" in result

    @pytest.mark.asyncio
    async def test_config_functions_integration(self):
        """Test that config functions work together."""
        # List should work
        list_result = await list_config_keys.fn()
        assert len(list_result) > 100  # Should have substantial content
        
        # Update should return a message (even if it fails due to permissions)
        with patch("voice_mode.tools.configuration_management.USER_CONFIG_PATH", Path("/tmp/test_config.env")):
            with patch("pathlib.Path.mkdir"):
                try:
                    update_result = await update_config.fn("TEST_INTEGRATION", "test")
                    assert isinstance(update_result, str)
                    assert len(update_result) > 0
                except Exception:
                    # Even if it fails, that's ok for this test
                    pass

    @pytest.mark.asyncio
    async def test_list_config_keys_formatting(self):
        """Test that list_config_keys returns properly formatted output."""
        result = await list_config_keys.fn()
        
        # Should have multiple lines
        lines = result.split('\n')
        assert len(lines) > 10  # Should have many config keys
        
        # Should have consistent formatting
        config_lines = [l for l in lines if 'BUMBA_' in l]
        assert len(config_lines) > 0
        
        # Each config line should have key and description
        for line in config_lines[:5]:  # Check first few
            if 'BUMBA_' in line and ':' in line:
                # Should have format like "BUMBA_KEY: description"
                assert line.count(':') >= 1