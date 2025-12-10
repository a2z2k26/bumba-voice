```
██████╗ ██╗   ██╗███╗   ███╗██████╗  █████╗     ██╗   ██╗ ██████╗ ██╗ ██████╗███████╗
██╔══██╗██║   ██║████╗ ████║██╔══██╗██╔══██╗    ██║   ██║██╔═══██╗██║██╔════╝██╔════╝
██████╔╝██║   ██║██╔████╔██║██████╔╝███████║    ██║   ██║██║   ██║██║██║     █████╗
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║    ╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║     ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝      ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝
```

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)

<br>

### Talk with Claude. Keyboard control. Optimized latency. Bumba Voice is a keyboard-driven push-to-talk voice assistant for Claude Code and AI assistants, delivering 60% faster response times through optimized audio processing. Built on the Model Context Protocol (MCP), it combines precise PTT control with sub-2-second latency for natural, real-time conversations. ###

---

### 🔴 Push-to-Talk Control ###

1. **Press key**: `Right Option Key` to talk just like a walkie-talkie:
2. **Press and Hold**: Hold the PTT key (Right Option) while speaking.
3. **Release key**: Release the key when done - your speech is processed immediately.

---

### 🟡 60% Faster Response Times (sub 2sec) ###

- **Traditional flows**: 3.5s average (record → process → speak)
- **Bumba Voice flow**: 1.4s average (parallel processing, WebRTC VAD, connection pooling)

---

### 🟢 Zero Cost Option ###

- **Local & free** run locally without API fees.
- **Whisper.cpp** for speech-to-text (on-device)
- **Kokoro TTS** for text-to-speech (50+ voices)
- **No cloud required** or mix local + cloud services

<br>

### 🏁 Performance ###

| Metric | Traditional | Bumba Voice | Improvement |
|--------|------------|--------|-------------|
| **Total Turnaround** | 3.5s | 1.4s | **60% faster** |
| Time to First Audio | 2.1s | 0.8s | 62% faster |
| Speech-to-Text | 1.2s | 0.4s | 67% faster |

*Based on average conversation over 100+ interactions*

<br>

### 🏁 Latency Optimization ###
- Parallel TTS/STT processing
- WebRTC VAD for instant speech detection
- HTTP connection pooling
- Zero-copy audio buffers
- Provider health caching

<br>

### 🏁 Installation ###

(requires Python 3.10+, FFmpeg)

```bash
# Clone and install
git clone https://github.com/a2z2k25/Bumba-Voice
cd Bumba-Voice
make dev-install

# Or install from source (requires uv)
uv pip install -e .

# Or install released package (coming soon)
pip install bumba

```

<br>

### 🏁 Configuration ###
Add to Claude Code (`~/.claude/mcp_settings.json)

```json
{
  "mcpServers": {
    "bumba": {
      "command": "python",
      "args": ["-m", "voice_mode.server"]
    }
  }
}
```

<br>

### 🏁 Environment Setup ###

Create `voicemode.env` in your project root:

```bash
# Push-to-Talk Configuration
BUMBA_PTT_ENABLED=true
BUMBA_PTT_MODE=hold              # hold, toggle, or hybrid
BUMBA_PTT_KEY_COMBO=option_r     # Your preferred key combo (Right Option Key)

# Voice Services (optional - uses OpenAI by default)
OPENAI_API_KEY=your-key-here      # For cloud TTS/STT

# Or use local services (zero cost)
# VOICEMODE_TTS_URL=http://localhost:8880/v1  # Local Kokoro
# VOICEMODE_STT_URL=http://localhost:7880/v1  # Local Whisper
```

<br>

---

<br>

### 🏁 Basic Conversation ###
```python
# In Claude Code, just say:
"Use the converse tool to chat with me"

# Claude will respond in voice and listen for your reply
```

<br>

### 🟢 First Conversation ###

1. Start: "Hey Claude, use the converse tool"
2. Hello Message: Claude will say 'Hello..'
3. Hold your PTT key: hold Right Option key
4. Speak: add your prompt by voice
5. Release key: release Right Option key
6. Listen: hear Claude respond!

<br>

---

<br>

### 🏁 Install Whisper.cpp (Speech-to-text) ###
```bash
# Using MCP tool in Claude Code (recommended):
"Install whisper with the base model"

# The MCP tool will:
# - Auto-detect your platform (macOS with Metal, Linux with CUDA if available)
# - Download and compile whisper.cpp with optimal settings
# - Download the specified model (default: base, 142MB)
# - Configure the service to auto-start
```

<br>

### 🏁 Install Kokoro (Text-to-speech) ###
```bash
# Using MCP tool in Claude Code (recommended):
"Install kokoro TTS service"

# The MCP tool will:
# - Clone kokoro-fastapi repository
# - Install dependencies in a virtual environment
# - Download required models on first start
# - Configure service to auto-start (macOS: launchd, Linux: systemd)
```

<br>

---

<br>

### 🏁 Setup Environment Variables ###

```bash
# PTT Settings
BUMBA_PTT_ENABLED=true|false
BUMBA_PTT_MODE=hold|toggle|hybrid
BUMBA_PTT_KEY_COMBO=option_r

# Voice Preferences
VOICEMODE_TTS_VOICE=alloy,nova,shimmer  # Preferred voices in order
VOICEMODE_STT_MODEL=whisper-1

# Service URLs (optional - auto-discovered)
VOICEMODE_TTS_URL=http://localhost:8880/v1
VOICEMODE_STT_URL=http://localhost:7880/v1

# Audio Settings
VOICEMODE_AUDIO_FEEDBACK=true|false
VOICEMODE_FEEDBACK_STYLE=whisper|shout
VOICEMODE_VAD_AGGRESSIVENESS=0-3  # Voice activity detection sensitivity
```

<br>

### 🏁 Setup Voice Preferences ###

Create `.voices.txt` in your project or home directory:

```
# Cloud voices (OpenAI)
alloy
nova

# Local voices (Kokoro)
af_sky    # American Female - Sky
am_adam   # American Male - Adam
bf_emma   # British Female - Emma
```

<br>

---

<br>

### 🟡 Audio Issues ###
```bash
# Check audio devices
python -m voice_mode.tools.devices

# Test microphone
# In Claude Code: "check my audio devices"
```

<br>

### 🟠 Service Issues ###
```bash
# Check service status
# In Claude Code: "check voice service status"

# Or use MCP service management tools:
# In Claude Code: "restart the whisper service"
# In Claude Code: "restart the kokoro service"
# In Claude Code: "show whisper service logs"
```

<br>

### 🔴 PTT Not Working ###
- Check `voicemode.env` has correct settings
- Verify key combination doesn't conflict with system shortcuts
- Try a different key combo: `BUMBA_PTT_KEY_COMBO=f12`

<br>

---

<br>

### 🏁 Documentation ###

- **[PTT Guide](docs/ptt/README.md)** - Complete Push-to-Talk documentation
- **[API Reference](docs/ptt/API_REFERENCE.md)** - Tool and configuration reference
- **[Architecture](docs/ARCHITECTURE_DIAGRAMS.md)** - System design diagrams
- **[Case Study](docs/CASE_STUDY.md)** - Development journey and decisions

<br>

### 🏁 License ###

MIT License - See [LICENSE](LICENSE) for details

<br>

### 🏁 Acknowledgement ###

Built upon the foundation of the [VoiceMode project by @mbailey](https://github.com/mbailey/voicemode)

<br>

---

<div align="center">

### 🏁 BUMBA Multi-Agent Orchestration Framework 🏁 ###
</div>
