#!/usr/bin/env python3
"""
Direct Voice Test with Docker Services
Tests TTS and STT using BUMBA's core functions
"""
import os
import asyncio
import tempfile
import numpy as np
from scipy.io.wavfile import write as write_wav

# Configure for Docker services
os.environ["STT_BASE_URL"] = "http://localhost:8880/v1"
os.environ["TTS_BASE_URL"] = "http://localhost:7888/v1"
os.environ["PREFER_LOCAL"] = "true"
os.environ["OPENAI_API_KEY"] = "dummy-key-for-local"

async def main():
    print("="*60)
    print("🎙️  BUMBA Core Voice Functions Test")
    print("="*60)
    
    try:
        # Import core functions
        from voice_mode.core import text_to_speech
        from voice_mode.tools.converse import speech_to_text
        import sounddevice as sd
        
        print("✅ Core functions loaded\n")
        
        # Step 1: Test TTS with Kokoro
        print("📍 Step 1: Testing Kokoro TTS...")
        greeting = "Hello! This is BUMBA using Docker services. The voice pipeline is operational!"
        
        success = await text_to_speech(
            greeting,
            voice="af_alloy",
            client_key="tts",
            model="tts-1",
            base_url="http://localhost:7888/v1"
        )
        
        if success:
            print(f"✅ TTS Success: Spoke '{greeting[:50]}...'\n")
        else:
            print("❌ TTS failed\n")
        
        # Step 2: Test microphone recording
        print("📍 Step 2: Recording from microphone (5 seconds)...")
        print("🎤 Speak now!")
        
        sample_rate = 16000
        duration = 5
        
        # Record audio
        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()  # Wait for recording to complete
        
        print("✅ Recording complete\n")
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            # Convert to int16
            audio_int16 = (recording * 32767).astype(np.int16)
            write_wav(tmp.name, sample_rate, audio_int16)
            audio_file = tmp.name
        
        # Step 3: Test STT with Whisper
        print("📍 Step 3: Testing Whisper STT...")
        
        transcription = await speech_to_text(
            audio_file,
            client_key="stt",
            model="whisper-1",
            base_url="http://localhost:8880/v1"
        )
        
        if transcription:
            print(f"📝 Whisper heard: '{transcription}'\n")
            
            # Step 4: Respond based on transcription
            print("📍 Step 4: Generating response...")
            
            if "hello" in transcription.lower():
                response = "Hello! Great to hear from you!"
            elif "test" in transcription.lower():
                response = "Test successful! Everything is working!"
            else:
                response = f"I heard: {transcription}"
            
            await text_to_speech(
                response,
                voice="af_alloy",
                client_key="tts",
                model="tts-1",
                base_url="http://localhost:7888/v1"
            )
            
            print(f"🤖 BUMBA: {response}")
        else:
            print("❌ STT failed or no speech detected")
        
        # Clean up
        os.remove(audio_file)
        
        print("\n" + "="*60)
        print("✅ Voice pipeline test complete!")
        print("="*60)
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure sounddevice is installed: pip install sounddevice")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Testing BUMBA voice pipeline with Docker services...\n")
    asyncio.run(main())