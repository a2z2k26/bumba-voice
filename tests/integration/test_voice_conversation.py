#!/usr/bin/env python3
"""Direct test of BUMBA voice conversation functionality."""

import asyncio
import os
import sys

# Add the project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure environment for local services if available
os.environ.setdefault("PREFER_LOCAL", "true")
os.environ.setdefault("BUMBA_AUDIO_FEEDBACK", "true")
os.environ.setdefault("BUMBA_DISABLE_SILENCE_DETECTION", "false")

async def test_voice_conversation():
    """Test the voice conversation system."""
    print("=" * 70)
    print("🎤 BUMBA Voice Conversation Test")
    print("=" * 70)
    print()
    
    try:
        # Import the converse tool and get the actual function
        from voice_mode.tools import converse as converse_module
        
        # The converse function is wrapped as an MCP tool, get the actual function
        if hasattr(converse_module, 'converse'):
            converse_tool = converse_module.converse
            # FastMCP FunctionTool has an 'fn' attribute with the actual function
            if hasattr(converse_tool, 'fn'):
                converse = converse_tool.fn
            elif hasattr(converse_tool, 'func'):
                converse = converse_tool.func
            elif hasattr(converse_tool, '__wrapped__'):
                converse = converse_tool.__wrapped__
            else:
                # Try to call it directly
                converse = converse_tool
        else:
            raise ImportError("Cannot find converse function")
            
        print("✅ BUMBA voice module loaded successfully")
        print()
        
        # Test 1: Simple TTS test
        print("📍 Test 1: Text-to-Speech")
        print("-" * 40)
        print("🤖 Speaking: 'Hello! This is BUMBA voice mode testing.'")
        print()
        
        result = await converse(
            message="Hello! This is BUMBA voice mode testing. The system has completed all 48 sprints successfully!",
            wait_for_response=False,
            voice="af_alloy"
        )
        
        if result:
            print(f"✅ TTS Result: Success")
            if 'audio_duration' in result:
                print(f"   Audio duration: {result['audio_duration']:.2f} seconds")
        print()
        
        # Test 2: Voice conversation with STT
        print("📍 Test 2: Full Voice Conversation")
        print("-" * 40)
        print("🤖 Speaking and listening for your response...")
        print("   (You have 5 seconds to respond after the message)")
        print()
        
        result = await converse(
            message="Please say something to test the speech recognition. What would you like to talk about?",
            wait_for_response=True,
            listen_duration=5.0,
            voice="af_alloy"
        )
        
        if result and 'user_response' in result:
            user_text = result['user_response']
            print(f"🎤 You said: '{user_text}'")
            print()
            
            # Generate a response
            response_message = f"I heard you say: {user_text}. The voice recognition is working perfectly!"
            
            print(f"🤖 Responding: '{response_message}'")
            await converse(
                message=response_message,
                wait_for_response=False,
                voice="af_alloy"
            )
            
            print()
            print("✅ Full conversation cycle complete!")
        else:
            print("⚠️  No speech detected or STT unavailable")
            print("   Result:", result)
            
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("   Make sure you're in the BUMBA project directory")
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
    
    print()
    print("=" * 70)
    print("Test complete!")
    print("=" * 70)

if __name__ == "__main__":
    print("Initializing BUMBA voice system...")
    print()
    asyncio.run(test_voice_conversation())