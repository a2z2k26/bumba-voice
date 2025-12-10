"""Manual test to verify Kokoro is selected for af_sky voice."""

import asyncio
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from voice_mode.providers import get_tts_client_and_voice
from voice_mode.provider_discovery import provider_registry


async def test_provider_selection():
    """Test that the voice-first selection works correctly."""
    print("Testing voice-first provider selection...")
    print(f"TTS_VOICES env: {os.getenv('BUMBA_TTS_VOICES', 'not set')}")
    print(f"TTS_BASE_URLS env: {os.getenv('BUMBA_TTS_BASE_URLS', 'not set')}")
    
    # Test 1: Default selection (should pick af_sky -> Kokoro if available)
    print("\n1. Testing default selection (no parameters)...")
    try:
        client, voice, model, endpoint = await get_tts_client_and_voice()
        print(f"   Selected: {endpoint.base_url} ({endpoint.provider_type})")
        print(f"   Voice: {voice}")
        print(f"   Model: {model}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Specific voice (af_sky should select Kokoro)
    print("\n2. Testing specific voice=af_sky...")
    try:
        client, voice, model, endpoint = await get_tts_client_and_voice(voice="af_sky")
        print(f"   Selected: {endpoint.base_url} ({endpoint.provider_type})")
        print(f"   Voice: {voice}")
        print(f"   Model: {model}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: Specific voice (nova should select OpenAI)
    print("\n3. Testing specific voice=nova...")
    try:
        client, voice, model, endpoint = await get_tts_client_and_voice(voice="nova")
        print(f"   Selected: {endpoint.base_url} ({endpoint.provider_type})")
        print(f"   Voice: {voice}")
        print(f"   Model: {model}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Show registry state
    print("\n4. Provider Registry State:")
    for service_type in ["tts", "stt"]:
        print(f"\n   {service_type.upper()} Endpoints:")
        for url, info in provider_registry.registry[service_type].items():
            print(f"   - {url} ({info.provider_type})")
            print(f"     Healthy: {info.healthy}")
            print(f"     Models: {info.models}")
            if service_type == "tts":
                print(f"     Voices: {info.voices[:3]}... ({len(info.voices)} total)")


if __name__ == "__main__":
    asyncio.run(test_provider_selection())