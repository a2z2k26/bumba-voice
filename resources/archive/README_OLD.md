# BUMBA 🎙️

```
 ██████╗██╗  ██╗ █████╗ ████████╗████████╗ █████╗ 
██╔════╝██║  ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗
██║     ███████║███████║   ██║      ██║   ███████║
██║     ██╔══██║██╔══██║   ██║      ██║   ██╔══██║
╚██████╗██║  ██║██║  ██║   ██║      ██║   ██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝

Natural Voice Conversations for AI Assistants • Part of the BUMBA Platform
```

[![Version](https://img.shields.io/badge/version-3.34.3-gold.svg)](https://github.com/mbailey/bumba)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![BUMBA](https://img.shields.io/badge/BUMBA-Platform-red.svg)](https://bumba.ai)

## 🖥️ Compatibility

**Runs on:** Linux • macOS • Windows (WSL) • NixOS | **Python:** 3.10+

## ✨ Features

- **🎙️ Voice conversations** with Claude - ask questions and hear responses
- **🔄 Multiple transports** - local microphone or LiveKit room-based communication  
- **🗣️ OpenAI-compatible** - works with any STT/TTS service (local or cloud)
- **⚡ Real-time** - low-latency voice interactions with automatic transport selection
- **🔧 MCP Integration** - seamless with Claude Desktop and other MCP clients
- **🎯 Silence detection** - automatically stops recording when you stop speaking (no more waiting!)

## 🎯 Simple Requirements

**All you need to get started:**

1. **🎤 Computer with microphone and speakers** OR **☁️ LiveKit server** ([LiveKit Cloud](https://docs.livekit.io/home/cloud/) or [self-hosted](https://github.com/livekit/livekit))
2. **🔑 OpenAI API Key** (optional) - BUMBA can install free, open-source transcription and text-to-speech services locally

**Optional for enhanced performance:**

- **🍎 Xcode** (macOS only) - Required for Core ML acceleration of Whisper models (2-3x faster inference). Install from [Mac App Store](https://apps.apple.com/app/xcode/id497799835) then run `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`

## Quick Start

> 📖 **Using a different tool?** See our [Integration Guides](docs/integrations/README.md) for Cursor, VS Code, Gemini CLI, and more!

### 🎯 One-Command Installation (Easiest)

```bash
curl -fsSL https://bumba.ai/install | bash
```

This launches an interactive setup wizard that guides you through:
- System compatibility check
- Dependency installation
- Voice service configuration (OpenAI API or local services)
- Docker setup for local services
- Claude Code integration
- Final testing and verification

### Interactive Setup Wizard (Recommended)

If you've already cloned the repository:

```bash
# Run the interactive setup wizard
make setup
# or
python setup_wizard.py
```

The wizard will:
- ✅ Check system requirements
- 📦 Install missing dependencies
- 🔑 Configure API keys (optional)
- 🐳 Set up Docker services
- 🤖 Configure Claude Code integration
- 🧪 Test everything works

### Manual Installation

For manual setup or custom configurations:

```bash
# Install BUMBA
pip install bumba

# Optional: Set OpenAI API key for cloud services
export OPENAI_API_KEY=your-openai-key

# Start voice services (if using local)
docker-compose up -d

# Configure MCP server
claude /bumba:configure
```

For detailed manual setup steps, see the [Claude Code Integration Guide](docs/integrations/claude-code/README.md).

## 🎬 Demo

Watch BUMBA in action with Claude Code:

[![BUMBA Demo](https://img.youtube.com/vi/cYdwOD_-dQc/maxresdefault.jpg)](https://www.youtube.com/watch?v=cYdwOD_-dQc)

### BUMBA with Gemini CLI

See BUMBA working with Google's Gemini CLI (their implementation of Claude Code):

[![BUMBA with Gemini CLI](https://img.youtube.com/vi/HC6BGxjCVnM/maxresdefault.jpg)](https://www.youtube.com/watch?v=HC6BGxjCVnM)

## Example Usage

Once configured, try these prompts with Claude:

### 👨‍💻 Programming & Development
- `"Let's debug this error together"` - Explain the issue verbally, paste code, and discuss solutions
- `"Walk me through this code"` - Have Claude explain complex code while you ask questions
- `"Let's brainstorm the architecture"` - Design systems through natural conversation
- `"Help me write tests for this function"` - Describe requirements and iterate verbally

### 💡 General Productivity  
- `"Let's do a daily standup"` - Practice presentations or organize your thoughts
- `"Interview me about [topic]"` - Prepare for interviews with back-and-forth Q&A
- `"Be my rubber duck"` - Explain problems out loud to find solutions

### 🎯 Voice Control Features
- `"Read this error message"` (Claude speaks, then waits for your response)
- `"Just give me a quick summary"` (Claude speaks without waiting)
- Use `converse("message", wait_for_response=False)` for one-way announcements

The `converse` function makes voice interactions natural - it automatically waits for your response by default, creating a real conversation flow.

## Supported Tools

BUMBA works with your favorite AI coding assistants:

- 🤖 **[Claude Code](docs/integrations/claude-code/README.md)** - Anthropic's official CLI
- 🖥️ **[Claude Desktop](docs/integrations/claude-desktop/README.md)** - Desktop application
- 🌟 **[Gemini CLI](docs/integrations/gemini-cli/README.md)** - Google's CLI tool
- ⚡ **[Cursor](docs/integrations/cursor/README.md)** - AI-first code editor
- 💻 **[VS Code](docs/integrations/vscode/README.md)** - With MCP preview support
- 🦘 **[Roo Code](docs/integrations/roo-code/README.md)** - AI dev team in VS Code
- 🔧 **[Cline](docs/integrations/cline/README.md)** - Autonomous coding agent
- ⚡ **[Zed](docs/integrations/zed/README.md)** - High-performance editor
- 🏄 **[Windsurf](docs/integrations/windsurf/README.md)** - Agentic IDE by Codeium
- 🔄 **[Continue](docs/integrations/continue/README.md)** - Open-source AI assistant

## Installation

### Prerequisites
- Python >= 3.10
- [Astral UV](https://github.com/astral-sh/uv) - Package manager (install with `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- OpenAI API Key (or compatible service)

#### System Dependencies

<details>
<summary><strong>Ubuntu/Debian</strong></summary>

```bash
sudo apt update
sudo apt install -y python3-dev libasound2-dev libasound2-plugins libportaudio2 portaudio19-dev ffmpeg pulseaudio pulseaudio-utils
```

**Note for WSL2 users**: WSL2 requires additional audio packages (pulseaudio, libasound2-plugins) for microphone access. See our [WSL2 Microphone Access Guide](docs/troubleshooting/wsl2-microphone-access.md) if you encounter issues.
</details>

<details>
<summary><strong>Fedora/RHEL</strong></summary>

```bash
sudo dnf install python3-devel alsa-lib-devel portaudio-devel ffmpeg
```
</details>

<details>
<summary><strong>macOS</strong></summary>

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install portaudio ffmpeg cmake
```
</details>

<details>
<summary><strong>Windows (WSL)</strong></summary>

Follow the Ubuntu/Debian instructions above within WSL.
</details>

<details>
<summary><strong>NixOS</strong></summary>

BUMBA includes a flake.nix with all required dependencies. You can either:

1. **Use the development shell** (temporary):
```bash
nix develop github:mbailey/bumba
```

2. **Install system-wide** (see Installation section below)
</details>

### Quick Install

```bash
# Using Claude Code (recommended)
claude mcp add --scope user bumba uvx bumba

# Using Claude Code with Nix (NixOS)
claude mcp add bumba nix run github:mbailey/bumba

# Using UV
uvx bumba

# Using pip
pip install bumba

# Using Nix (NixOS)
nix run github:mbailey/bumba
```

### Configuration for AI Coding Assistants

> 📖 **Looking for detailed setup instructions?** Check our comprehensive [Integration Guides](docs/integrations/README.md) for step-by-step instructions for each tool!

Below are quick configuration snippets. For full installation and setup instructions, see the integration guides above.

<details>
<summary><strong>Claude Code (CLI)</strong></summary>

```bash
claude mcp add bumba -- uvx bumba
```

Or with environment variables:
```bash
claude mcp add bumba --env OPENAI_API_KEY=your-openai-key -- uvx bumba
```
</details>

<details>
<summary><strong>Claude Desktop</strong></summary>

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "bumba": {
      "command": "uvx",
      "args": ["bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```
</details>

<details>
<summary><strong>Cline</strong></summary>

Add to your Cline MCP settings:

**Windows**:
```json
{
  "mcpServers": {
    "bumba": {
      "command": "cmd",
      "args": ["/c", "uvx", "bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```

**macOS/Linux**:
```json
{
  "mcpServers": {
    "bumba": {
      "command": "uvx",
      "args": ["bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```
</details>

<details>
<summary><strong>Continue</strong></summary>

Add to your `.continue/config.json`:
```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "uvx",
          "args": ["bumba"],
          "env": {
            "OPENAI_API_KEY": "your-openai-key"
          }
        }
      }
    ]
  }
}
```
</details>

<details>
<summary><strong>Cursor</strong></summary>

Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "bumba": {
      "command": "uvx",
      "args": ["bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```
</details>

<details>
<summary><strong>VS Code</strong></summary>

Add to your VS Code MCP config:
```json
{
  "mcpServers": {
    "bumba": {
      "command": "uvx",
      "args": ["bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```
</details>

<details>
<summary><strong>Windsurf</strong></summary>

```json
{
  "mcpServers": {
    "bumba": {
      "command": "uvx",
      "args": ["bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```
</details>

<details>
<summary><strong>Zed</strong></summary>

Add to your Zed settings.json:
```json
{
  "context_servers": {
    "bumba": {
      "command": {
        "path": "uvx",
        "args": ["bumba"],
        "env": {
          "OPENAI_API_KEY": "your-openai-key"
        }
      }
    }
  }
}
```
</details>

<details>
<summary><strong>Roo Code</strong></summary>

1. Open VS Code Settings (`Ctrl/Cmd + ,`)
2. Search for "roo" in the settings search bar
3. Find "Roo-veterinaryinc.roo-cline → settings → Mcp_settings.json"
4. Click "Edit in settings.json"
5. Add BUMBA configuration:

```json
{
  "mcpServers": {
    "bumba": {
      "command": "uvx",
      "args": ["bumba"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```
</details>

### Alternative Installation Options

<details>
<summary><strong>Using Docker</strong></summary>

```bash
docker run -it --rm \
  -e OPENAI_API_KEY=your-openai-key \
  --device /dev/snd \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=$DISPLAY \
  ghcr.io/mbailey/bumba:latest
```
</details>

<details>
<summary><strong>Using pipx</strong></summary>

```bash
pipx install bumba
```
</details>

<details>
<summary><strong>From source</strong></summary>

```bash
git clone https://github.com/mbailey/bumba.git
cd bumba
pip install -e .
```
</details>

<details>
<summary><strong>NixOS Installation Options</strong></summary>

**1. Install with nix profile (user-wide):**
```bash
nix profile install github:mbailey/bumba
```

**2. Add to NixOS configuration (system-wide):**
```nix
# In /etc/nixos/configuration.nix
environment.systemPackages = [
  (builtins.getFlake "github:mbailey/bumba").packages.${pkgs.system}.default
];
```

**3. Add to home-manager:**
```nix
# In home-manager configuration
home.packages = [
  (builtins.getFlake "github:mbailey/bumba").packages.${pkgs.system}.default
];
```

**4. Run without installing:**
```bash
nix run github:mbailey/bumba
```
</details>

## Tools

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `converse` | Have a voice conversation - speak and optionally listen | `message`, `wait_for_response` (default: true), `listen_duration` (default: 30s), `transport` (auto/local/livekit) |
| `listen_for_speech` | Listen for speech and convert to text | `duration` (default: 5s) |
| `check_room_status` | Check LiveKit room status and participants | None |
| `check_audio_devices` | List available audio input/output devices | None |
| `start_kokoro` | Start the Kokoro TTS service | `models_dir` (optional, defaults to ~/Models/kokoro) |
| `stop_kokoro` | Stop the Kokoro TTS service | None |
| `kokoro_status` | Check the status of Kokoro TTS service | None |
| `install_whisper_cpp` | Install whisper.cpp for local STT | `install_dir`, `model` (default: base.en), `use_gpu` (auto-detect) |
| `install_kokoro_fastapi` | Install kokoro-fastapi for local TTS | `install_dir`, `port` (default: 8880), `auto_start` (default: true) |

**Note:** The `converse` tool is the primary interface for voice interactions, combining speaking and listening in a natural flow.

**New:** The `install_whisper_cpp` and `install_kokoro_fastapi` tools help you set up free, private, open-source voice services locally. See [Installation Tools Documentation](docs/installation-tools.md) for detailed usage.

## Configuration

- 📖 **[Integration Guides](docs/integrations/README.md)** - Step-by-step setup for each tool
- 🔧 **[Configuration Reference](docs/configuration.md)** - All environment variables
- 📁 **[Config Examples](config-examples/)** - Ready-to-use configuration files

### Quick Setup

The only required configuration is your OpenAI API key:

```bash
export OPENAI_API_KEY="your-key"
```

### Optional Settings

```bash
# Custom STT/TTS services (OpenAI-compatible)
export STT_BASE_URL="http://127.0.0.1:2022/v1"  # Local Whisper
export TTS_BASE_URL="http://127.0.0.1:8880/v1"  # Local TTS
export TTS_VOICE="alloy"                        # Voice selection

# Or use voice preference files (see Configuration docs)
# Project: /your-project/voices.txt or /your-project/.bumba/voices.txt
# User: ~/voices.txt or ~/.bumba/voices.txt

# LiveKit (for room-based communication)
# See docs/livekit/ for setup guide
export LIVEKIT_URL="wss://your-app.livekit.cloud"
export LIVEKIT_API_KEY="your-api-key"
export LIVEKIT_API_SECRET="your-api-secret"

# Debug mode
export VOICEMODE_DEBUG="true"

# Save all audio (TTS output and STT input)
export VOICEMODE_SAVE_AUDIO="true"

# Audio format configuration (default: pcm)
export VOICEMODE_AUDIO_FORMAT="pcm"         # Options: pcm, mp3, wav, flac, aac, opus
export VOICEMODE_TTS_AUDIO_FORMAT="pcm"     # Override for TTS only (default: pcm)
export VOICEMODE_STT_AUDIO_FORMAT="mp3"     # Override for STT upload

# Format-specific quality settings
export VOICEMODE_OPUS_BITRATE="32000"       # Opus bitrate (default: 32kbps)
export VOICEMODE_MP3_BITRATE="64k"          # MP3 bitrate (default: 64k)
```

### Audio Format Configuration

BUMBA uses **PCM** audio format by default for TTS streaming for optimal real-time performance:

- **PCM** (default for TTS): Zero latency, best streaming performance, uncompressed
- **MP3**: Wide compatibility, good compression for uploads
- **WAV**: Uncompressed, good for local processing
- **FLAC**: Lossless compression, good for archival
- **AAC**: Good compression, Apple ecosystem
- **Opus**: Small files but NOT recommended for streaming (quality issues)

The audio format is automatically validated against provider capabilities and will fallback to a supported format if needed.

## Local STT/TTS Services

For privacy-focused or offline usage, BUMBA supports local speech services:

- **[Whisper.cpp](docs/whisper.cpp.md)** - Local speech-to-text with OpenAI-compatible API
- **[Kokoro](docs/kokoro.md)** - Local text-to-speech with multiple voice options

These services provide the same API interface as OpenAI, allowing seamless switching between cloud and local processing.

### OpenAI API Compatibility Benefits

By strictly adhering to OpenAI's API standard, BUMBA enables powerful deployment flexibility:

- **🔀 Transparent Routing**: Users can implement their own API proxies or gateways outside of BUMBA to route requests to different providers based on custom logic (cost, latency, availability, etc.)
- **🎯 Model Selection**: Deploy routing layers that select optimal models per request without modifying BUMBA configuration
- **💰 Cost Optimization**: Build intelligent routers that balance between expensive cloud APIs and free local models
- **🔧 No Lock-in**: Switch providers by simply changing the `BASE_URL` - no code changes required

Example: Simply set `OPENAI_BASE_URL` to point to your custom router:
```bash
export OPENAI_BASE_URL="https://router.example.com/v1"
export OPENAI_API_KEY="your-key"
# BUMBA now uses your router for all OpenAI API calls
```

The OpenAI SDK handles this automatically - no BUMBA configuration needed!

## Architecture

```
┌─────────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│   Claude/LLM        │     │  LiveKit Server  │     │  Voice Frontend     │
│   (MCP Client)      │◄────►│  (Optional)     │◄───►│  (Optional)         │
└─────────────────────┘     └──────────────────┘     └─────────────────────┘
         │                            │
         │                            │
         ▼                            ▼
┌─────────────────────┐     ┌──────────────────┐
│  Voice MCP Server   │     │   Audio Services │
│  • converse         │     │  • OpenAI APIs   │
│  • listen_for_speech│◄───►│  • Local Whisper │
│  • check_room_status│     │  • Local TTS     │
│  • check_audio_devices    └──────────────────┘
└─────────────────────┘
```

## Troubleshooting

### Common Issues

- **No microphone access**: Check system permissions for terminal/application
  - **WSL2 Users**: See [WSL2 Microphone Access Guide](docs/troubleshooting/wsl2-microphone-access.md)
- **UV not found**: Install with `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **OpenAI API error**: Verify your `OPENAI_API_KEY` is set correctly
- **No audio output**: Check system audio settings and available devices

### Debug Mode

Enable detailed logging and audio file saving:

```bash
export VOICEMODE_DEBUG=true
```

Debug audio files are saved to: `~/bumba_recordings/`

### Audio Diagnostics

Run the diagnostic script to check your audio setup:

```bash
python scripts/diagnose-wsl-audio.py
```

This will check for required packages, audio services, and provide specific recommendations.

### Audio Saving

To save all audio files (both TTS output and STT input):

```bash
export VOICEMODE_SAVE_AUDIO=true
```

Audio files are saved to: `~/.bumba/audio/YYYY/MM/` with timestamps in the filename.

## Documentation

📚 **[Read the full documentation at bumba.readthedocs.io](https://bumba.readthedocs.io)**

### Getting Started
- **[Integration Guides](docs/integrations/README.md)** - Step-by-step setup for all supported tools
- **[Configuration Guide](docs/configuration.md)** - Complete environment variable reference

### Development
- **[Using uv/uvx](docs/uv.md)** - Package management with uv and uvx
- **[Local Development](docs/local-development-uvx.md)** - Development setup guide
- **[Audio Formats](docs/audio-format-migration.md)** - Audio format configuration and migration
- **[Statistics Dashboard](docs/statistics-dashboard.md)** - Performance monitoring and metrics

### Service Guides
- **[Whisper.cpp Setup](docs/whisper.cpp.md)** - Local speech-to-text configuration
- **[Kokoro Setup](docs/kokoro.md)** - Local text-to-speech configuration
- **[Service Health Checks](docs/service-health-checks.md)** - Service readiness and health monitoring
- **[LiveKit Integration](docs/livekit/README.md)** - Real-time voice communication

### Troubleshooting
- **[WSL2 Microphone Access](docs/troubleshooting/wsl2-microphone-access.md)** - WSL2 audio setup
- **[Migration Guide](docs/migration-guide.md)** - Upgrading from older versions

## Links

- **Website**: - **Documentation**: [bumba.readthedocs.io](https://bumba.readthedocs.io)
- **GitHub**: [github.com/mbailey/bumba](https://github.com/mbailey/bumba)
- **PyPI**: [pypi.org/project/bumba](https://pypi.org/project/bumba/)
- **npm**: [npmjs.com/package/bumba](https://www.npmjs.com/package/bumba)

### Community

- **Discord**: [Join our community](https://discord.gg/Hm7dF3uCfG)
- **Twitter/X**: [@getbumba](https://twitter.com/getbumba)
- **YouTube**: [@getbumba](https://youtube.com/@getbumba)

## See Also

- 🚀 [Integration Guides](docs/integrations/README.md) - Setup instructions for all supported tools
- 🔧 [Configuration Reference](docs/configuration.md) - Environment variables and options
- 🎤 [Local Services Setup](docs/kokoro.md) - Run TTS/STT locally for privacy
- 🐛 [Troubleshooting](docs/troubleshooting/README.md) - Common issues and solutions

## License

MIT - A [Failmode](https://failmode.com) Project

---

<sub>[Project Statistics](docs/project-stats/README.md)</sub>
