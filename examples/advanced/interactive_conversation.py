#!/usr/bin/env python3
"""
BUMBA Interactive Voice Conversation
A real conversation flow using Kokoro TTS and Whisper STT
"""
import requests
import subprocess
import tempfile
import os
import time
import sys

def speak_kokoro(text, voice="af_alloy"):
    """Generate speech using Kokoro TTS and play it"""
    print(f"🤖 BUMBA: {text}")
    
    try:
        response = requests.post(
            "http://localhost:7888/v1/audio/speech",
            json={
                "input": text,
                "voice": voice,
                "model": "tts-1"
            },
            timeout=10
        )
        
        if response.status_code == 200:
            # Save and play audio
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                f.write(response.content)
                audio_file = f.name
            
            # Play audio (macOS)
            if os.path.exists("/usr/bin/afplay"):
                subprocess.run(["afplay", audio_file], check=False)
            
            # Clean up
            os.remove(audio_file)
            return True
        else:
            print(f"❌ Kokoro TTS error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Kokoro error: {e}")
        return False

def record_audio(duration=5, output_file="recording.wav"):
    """Record audio from microphone (macOS)"""
    print(f"🎤 Recording for {duration} seconds... Speak now!")
    
    try:
        # Use sox or ffmpeg for recording
        if os.path.exists("/usr/local/bin/sox"):
            # Use sox if available
            subprocess.run([
                "sox", "-d", "-r", "16000", "-c", "1", "-b", "16",
                output_file, "trim", "0", str(duration)
            ], check=True)
        elif os.path.exists("/usr/local/bin/ffmpeg"):
            # Use ffmpeg as fallback
            subprocess.run([
                "ffmpeg", "-f", "avfoundation", "-i", ":0",
                "-t", str(duration), "-ar", "16000", "-ac", "1",
                "-y", output_file
            ], check=True, capture_output=True)
        else:
            # Use macOS say to create test audio
            print("⚠️  No recording tool found, using test phrase")
            test_phrase = "Hello BUMBA, this is a test message"
            subprocess.run([
                "say", "-o", output_file,
                "--data-format=LEI16@16000",
                test_phrase
            ], check=True)
        
        print("✅ Recording complete")
        return True
    except Exception as e:
        print(f"❌ Recording error: {e}")
        return False

def transcribe_whisper(audio_file):
    """Transcribe audio using Whisper STT"""
    try:
        with open(audio_file, "rb") as f:
            files = {"file": (audio_file, f, "audio/wav")}
            data = {"model": "whisper-1"}
            response = requests.post(
                "http://localhost:8880/v1/audio/transcriptions",
                files=files,
                data=data,
                timeout=30
            )
        
        if response.status_code == 200:
            text = response.json().get("text", "").strip()
            print(f"👤 You said: {text}")
            return text
        else:
            print(f"❌ Whisper STT error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Whisper error: {e}")
        return None

def simple_response(user_input):
    """Generate a simple response based on user input"""
    user_input_lower = user_input.lower()
    
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hello there! It's great to hear from you. How are you doing today?"
    elif "how are you" in user_input_lower:
        return "I'm functioning perfectly, thank you for asking! My voice services are operational and ready to chat."
    elif "name" in user_input_lower:
        return "I'm BUMBA, your voice-enabled AI assistant. Nice to meet you!"
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Goodbye! It was lovely talking with you. Have a wonderful day!"
    elif "test" in user_input_lower:
        return "Test received loud and clear! The voice system is working perfectly."
    elif "weather" in user_input_lower:
        return "I wish I could tell you about the weather, but I'm focused on testing our voice connection right now!"
    else:
        return f"I heard you say: {user_input}. That's interesting! Tell me more."

def conversation_flow():
    """Main conversation flow"""
    print("\n" + "="*60)
    print("🎙️  BUMBA Interactive Voice Conversation")
    print("="*60)
    print("Testing Kokoro TTS → Your Voice → Whisper STT → Kokoro TTS")
    print("-"*60)
    
    # Check services
    print("\nChecking services...")
    try:
        r1 = requests.get("http://localhost:7888/health", timeout=2)
        r2 = requests.get("http://localhost:8880/health", timeout=2)
        if r1.status_code == 200 and r2.status_code == 200:
            print("✅ All services ready!\n")
        else:
            print("❌ Services not ready. Please run: docker-compose up")
            return
    except:
        print("❌ Services not running. Please run: docker-compose up")
        return
    
    # Start conversation
    print("Starting conversation...\n")
    time.sleep(1)
    
    # 1. Kokoro greets you
    greeting = "Hello! I'm BUMBA, your voice assistant. I'm ready to have a conversation with you. Please say something after the beep!"
    if not speak_kokoro(greeting):
        print("Failed to generate greeting")
        return
    
    time.sleep(1)
    
    # Conversation loop
    recording_file = "user_audio.wav"
    rounds = 0
    max_rounds = 5
    
    while rounds < max_rounds:
        rounds += 1
        print(f"\n--- Round {rounds}/{max_rounds} ---")
        
        # 2. Record user's voice
        if not record_audio(duration=4, output_file=recording_file):
            print("Failed to record audio")
            break
        
        # 3. Transcribe with Whisper
        user_text = transcribe_whisper(recording_file)
        if not user_text:
            print("Failed to transcribe audio")
            continue
        
        # Check for exit
        if "bye" in user_text.lower() or "goodbye" in user_text.lower():
            response = "Goodbye! It was wonderful talking with you. Have a great day!"
            speak_kokoro(response)
            break
        
        # 4. Generate and speak response
        response = simple_response(user_text)
        if not speak_kokoro(response):
            print("Failed to generate response")
            break
        
        time.sleep(1)
    
    # Clean up
    if os.path.exists(recording_file):
        os.remove(recording_file)
    
    print("\n" + "="*60)
    print("🎉 Conversation complete!")
    print("="*60)

def test_microphone():
    """Test if microphone recording works"""
    print("\n🎤 Testing microphone access...")
    test_file = "mic_test.wav"
    
    # Try different recording methods
    methods = [
        ("sox", ["sox", "-d", "-r", "16000", "-c", "1", "-b", "16", test_file, "trim", "0", "1"]),
        ("ffmpeg", ["ffmpeg", "-f", "avfoundation", "-i", ":0", "-t", "1", "-ar", "16000", "-ac", "1", "-y", test_file])
    ]
    
    for name, cmd in methods:
        try:
            if os.path.exists(f"/usr/local/bin/{name}") or os.path.exists(f"/usr/bin/{name}"):
                print(f"Trying {name}...")
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
                if os.path.exists(test_file) and os.path.getsize(test_file) > 0:
                    print(f"✅ {name} recording works!")
                    os.remove(test_file)
                    return name
        except:
            continue
    
    print("⚠️  No recording method available. Install sox: brew install sox")
    print("    Or we'll use text-to-speech for testing")
    return None

if __name__ == "__main__":
    print("🎤 BUMBA Voice Conversation Demo")
    print("-" * 40)
    
    # Test microphone first
    recorder = test_microphone()
    if not recorder:
        print("\n⚠️  No microphone recording available.")
        print("We'll use generated test audio instead.")
        response = input("\nContinue with test audio? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    print("\nReady to start the conversation!")
    print("Say 'goodbye' or 'bye' to end the conversation.\n")
    input("Press Enter to begin... ")
    
    conversation_flow()