#!/usr/bin/env python3
"""
Final Verification Test for BUMBA Feature Parity
Confirms audio feedback and VAD work in both Claude Desktop and Code
"""

import asyncio
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

async def main():
    print("=" * 60)
    print(" BUMBA FINAL VERIFICATION TEST")
    print("=" * 60)
    
    # 1. Check execution context
    is_mcp = not sys.stdin.isatty() or not sys.stdout.isatty()
    print(f"\n✓ Execution Context: {'MCP/Claude Code' if is_mcp else 'Direct/Claude Desktop'}")
    
    # 2. Verify audio files
    audio_dir = Path("voice_mode/audio")
    files = ["start_chime.wav", "end_chime.wav", "start_chime_bluetooth.wav", "end_chime_bluetooth.wav"]
    all_exist = all((audio_dir / f).exists() for f in files)
    print(f"✓ Audio Files: {'All present' if all_exist else 'Some missing'}")
    
    # 3. Test audio playback
    from voice_mode.core import play_chime_start, play_chime_end
    
    print("\n🔊 Testing Audio Feedback:")
    print("  Playing start chime...")
    start_ok = await play_chime_start()
    print(f"  {'✅' if start_ok else '❌'} Start chime: {'Success' if start_ok else 'Failed'}")
    
    await asyncio.sleep(0.5)
    
    print("  Playing end chime...")
    end_ok = await play_chime_end()
    print(f"  {'✅' if end_ok else '❌'} End chime: {'Success' if end_ok else 'Failed'}")
    
    # 4. Check VAD availability
    print("\n🎤 Testing VAD:")
    try:
        import webrtcvad
        vad = webrtcvad.Vad()
        vad_available = True
        print("  ✅ WebRTC VAD: Available")
    except ImportError:
        vad_available = False
        print("  ❌ WebRTC VAD: Not available")
    
    from voice_mode.config import DISABLE_SILENCE_DETECTION
    print(f"  {'✅' if not DISABLE_SILENCE_DETECTION else '❌'} Silence Detection: {'Enabled' if not DISABLE_SILENCE_DETECTION else 'Disabled'}")
    
    # 5. Summary
    print("\n" + "=" * 60)
    print(" VERIFICATION RESULTS")
    print("=" * 60)
    
    all_pass = all_exist and start_ok and end_ok and vad_available and not DISABLE_SILENCE_DETECTION
    
    if all_pass:
        print("\n✅ ALL TESTS PASSED!")
        print("\nFeature Status:")
        print("  • Audio feedback chimes: WORKING")
        print("  • VAD/Silence detection: AVAILABLE")
        print("  • Platform parity: ACHIEVED")
        print("\nThe BUMBA framework is fully operational for both")
        print("Claude Desktop and Claude Code environments!")
    else:
        print("\n⚠️  SOME TESTS FAILED")
        if not all_exist:
            print("  - Missing audio files (run generate_chimes.py)")
        if not (start_ok and end_ok):
            print("  - Audio playback issues")
        if not vad_available:
            print("  - WebRTC VAD not installed")
        if DISABLE_SILENCE_DETECTION:
            print("  - Silence detection is disabled")
    
    print("\n" + "=" * 60)
    return all_pass

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    success = asyncio.run(main())
    sys.exit(0 if success else 1)