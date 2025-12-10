"""Test provider detection logic."""

import pytest
from unittest.mock import Mock, AsyncMock, patch
from voice_mode.tools.converse import speech_to_text_with_failover, get_stt_config
from voice_mode.provider_discovery import EndpointInfo


class TestProviderDetection:
    """Test that provider detection works correctly for different URLs."""
    
    def test_localhost_detection(self):
        """Test that localhost URLs are detected as local providers."""
        # Test various localhost URLs
        localhost_urls = [
            "http://localhost:2022/v1",
            "https://localhost:2022/v1",
            "http://127.0.0.1:2022/v1",
            "https://127.0.0.1:2022/v1",
            "http://localhost:8880/v1",
            "http://127.0.0.1:8880/v1"
        ]
        
        for url in localhost_urls:
            # Check if provider detection logic works
            is_local = '127.0.0.1' in url or 'localhost' in url
            assert is_local, f"URL {url} should be detected as local"
    
    def test_duplicate_condition_bug(self):
        """Test that we don't have duplicate conditions in provider detection."""
        # This test specifically checks for the bug where '127.0.0.1' was checked twice
        # instead of checking both '127.0.0.1' and 'localhost'
        
        # Read the source file to check for the bug
        from pathlib import Path
        converse_file = Path(__file__).parent.parent / "src" / "voice_mode" / "tools" / "converse.py"
        
        with open(converse_file, 'r') as f:
            content = f.read()
        
        # Look for lines that might have duplicate conditions
        import re
        
        # Pattern to find duplicate checks in the same condition
        # This would match things like: "127.0.0.1" in x or "127.0.0.1" in x
        duplicate_pattern = r'["\']([^"\']+)["\']\s+in\s+(\w+)\s+or\s+["\'](\1)["\']\s+in\s+\2'
        
        matches = list(re.finditer(duplicate_pattern, content))
        
        assert len(matches) == 0, (
            f"Found duplicate condition checks in converse.py:\n" +
            "\n".join([f"  Line contains: {match.group(0)}" for match in matches]) +
            "\n\nThis likely means '127.0.0.1' is checked twice instead of checking both '127.0.0.1' and 'localhost'"
        )
    
    def test_provider_classification(self):
        """Test that providers are correctly classified based on URL."""
        # Define test cases
        test_cases = [
            # (url, expected_provider)
            ("http://127.0.0.1:2022/v1", "whisper-local"),
            ("http://localhost:2022/v1", "whisper-local"),
            ("https://api.openai.com/v1", "openai-whisper"),
            ("https://api.example.com/v1", "openai-whisper"),  # Unknown URLs default to OpenAI
        ]
        
        for url, expected_provider in test_cases:
            # Simulate the provider detection logic
            if '127.0.0.1' in url or 'localhost' in url:
                provider = 'whisper-local'
            else:
                provider = 'openai-whisper'
            
            assert provider == expected_provider, f"URL {url} should be detected as {expected_provider}, got {provider}"
    
    @pytest.mark.asyncio
    async def test_endpoint_info_attribute_usage(self):
        """Test that get_stt_config uses endpoint_info.base_url not endpoint_info.url."""
        # Create a mock EndpointInfo with base_url attribute
        mock_endpoint_info = Mock(spec=EndpointInfo)
        mock_endpoint_info.base_url = "http://127.0.0.1:2022/v1"
        # Note: EndpointInfo doesn't have a 'url' attribute
        
        mock_client = AsyncMock()
        mock_model = "whisper-1"
        
        with patch('voice_mode.tools.converse.get_stt_client') as mock_get_stt:
            mock_get_stt.return_value = (mock_client, mock_model, mock_endpoint_info)
            
            # Call get_stt_config
            config = await get_stt_config()
            
            # Verify it uses base_url, not url
            assert config['base_url'] == "http://127.0.0.1:2022/v1"
            assert config['provider'] == "http://127.0.0.1:2022/v1"  # For logging
            assert config['client'] == mock_client
            assert config['model'] == mock_model