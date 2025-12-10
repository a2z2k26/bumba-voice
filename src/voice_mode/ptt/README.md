# Push-to-Talk (PTT) Module

## Overview
This module implements keyboard-controlled voice recording for Bumba Voice, allowing users to control recording via configurable key combinations instead of automatic silence detection.

## Status
✅ **Phase 2 Complete** - Foundation Setup (100% Complete)
🚧 **Next Up:** Phase 3 - Core PTT Implementation

## Module Structure
```
ptt/
├── __init__.py              # Module initialization and public API ✅
├── keyboard.py              # Keyboard event handling ✅
├── logging.py               # PTT logging infrastructure ✅
├── controller.py            # Main PTT controller (Phase 3)
├── permissions.py           # Permission management (Phase 3)
├── recorder.py              # PTT-specific recording (Phase 3)
└── README.md                # This file ✅
```

**Configuration**: PTT settings in `src/voice_mode/config.py` ✅

**Documentation**:
- 📖 [Testing Guide](TESTING.md) - Comprehensive testing documentation
- 🤝 [Contributing Guide](CONTRIBUTING.md) - Developer contribution guidelines

## Features (Planned)

### Core Functionality
- [x] Module structure created
- [ ] State machine implementation
- [ ] Keyboard event detection
- [ ] Recording control
- [ ] Thread-safe communication

### Recording Modes
- [ ] Hold-to-record (default)
- [ ] Toggle mode (press to start/stop)
- [ ] Hybrid mode (hold + silence detection)

### Platform Support
- [ ] macOS (with accessibility permissions)
- [ ] Windows (no elevation required)
- [ ] Linux (X11 and Wayland)

### Configuration
- [ ] Environment variables
- [ ] YAML configuration files
- [ ] Runtime overrides
- [ ] Configuration presets

## Current API (Phase 2 Complete)

### Keyboard Handler

The `KeyboardHandler` class provides cross-platform keyboard event monitoring:

```python
from voice_mode.ptt import KeyboardHandler

# Basic usage - default key combo (option_r)
def on_combo_press():
    print("Recording started!")

def on_combo_release():
    print("Recording stopped!")

handler = KeyboardHandler(
    key_combo="option_r",
    on_press_callback=on_combo_press,
    on_release_callback=on_combo_release
)

# Start monitoring
handler.start()

# Check if running
if handler.is_running():
    print("Handler is active")

# Stop monitoring
handler.stop()
```

**Key Features:**
- Cross-platform key monitoring (macOS, Windows, Linux)
- Configurable key combinations (e.g., "option_r", "ctrl+c", "space")
- Callback-based architecture
- Thread-safe operation
- Debouncing support (configurable delay)
- Automatic key normalization

**Key Combination Examples:**
```python
# Single key
handler = KeyboardHandler("space")

# Two keys
handler = KeyboardHandler("ctrl+c")

# Option keys
handler = KeyboardHandler("option_r")  # Default (Right Option Key)

# Function keys
handler = KeyboardHandler("f12")
```

### PTT Logger

The `PTTLogger` class provides structured logging for PTT operations:

```python
from voice_mode.ptt import PTTLogger, get_ptt_logger

# Get global logger instance
logger = get_ptt_logger()

# Or create custom logger
logger = PTTLogger(session_id="my_session")

# Log events
logger.log_event("key_press", {
    "key": "space",
    "combo_active": True
})

# Log key events (convenience method)
logger.log_key_event("press", "space", combo_active=True)

# Performance timing
timer_id = logger.start_timer("recording_start")
# ... perform operation ...
duration_ms = logger.stop_timer(timer_id)

# Log state transitions
logger.log_state_transition(
    from_state="IDLE",
    to_state="RECORDING",
    trigger="key_press"
)

# Log errors
logger.log_error("permission_denied", {
    "permission": "accessibility",
    "platform": "macOS"
})

# Get session summary
summary = logger.get_session_summary()
print(f"Session {summary['session_id']} - {summary['total_events']} events")

# Export to JSON
logger.export_session("/path/to/session.json")

# Export to JSONL
logger.export_to_jsonl("/path/to/session.jsonl")
```

**Logging Features:**
- Structured event logging
- Performance timing measurements
- Session tracking with unique IDs
- JSONL and JSON export
- Event statistics and summaries
- Thread-safe operation

### Configuration

PTT configuration via environment variables:

```bash
# Core settings
export BUMBA_PTT_ENABLED=true
export BUMBA_PTT_KEY_COMBO="option_r"
export BUMBA_PTT_MODE="hold"          # hold, toggle, or hybrid
export BUMBA_PTT_TIMEOUT=120.0

# Behavior settings
export BUMBA_PTT_AUTO_ENABLE=false
export BUMBA_PTT_REQUIRE_BOTH_KEYS=true
export BUMBA_PTT_RELEASE_DELAY=0.1
export BUMBA_PTT_MIN_DURATION=0.5

# Audio feedback
export BUMBA_PTT_AUDIO_FEEDBACK=true
export BUMBA_PTT_FEEDBACK_VOLUME=0.7
export BUMBA_PTT_VISUAL_FEEDBACK=true

# Advanced settings
export BUMBA_PTT_CANCEL_KEY="escape"
export BUMBA_PTT_BUFFER_PRE_RECORDING=false
export BUMBA_PTT_BUFFER_DURATION=0.5
export BUMBA_PTT_KEY_REPEAT_IGNORE=true

# Platform-specific
export BUMBA_PTT_MACOS_ACCESSIBILITY_CHECK=true
export BUMBA_PTT_WINDOWS_HOOK_TYPE="low_level"
export BUMBA_PTT_LINUX_INPUT_METHOD="auto"

# Debug settings
export BUMBA_PTT_DEBUG=false
export BUMBA_PTT_LOG_KEYS=false
export BUMBA_PTT_SIMULATE=false
```

**Loading Configuration:**
```python
from voice_mode import config

# Access PTT settings
enabled = config.PTT_ENABLED
key_combo = config.PTT_KEY_COMBO
mode = config.PTT_MODE
timeout = config.PTT_TIMEOUT

# Use in your code
if config.PTT_ENABLED:
    handler = KeyboardHandler(config.PTT_KEY_COMBO)
```

### Permission Checking

Check platform permissions (currently macOS):

```python
from voice_mode.ptt import check_keyboard_permissions

# Check if permissions are available
has_permissions = check_keyboard_permissions()

if not has_permissions:
    print("Please grant accessibility permissions in System Preferences")
    print("System Preferences → Security & Privacy → Privacy → Accessibility")
```

## Future Usage (Phase 3+)

When PTT integration is complete, you'll be able to use it with the converse tool:

```python
from voice_mode.tools.converse import converse

# Enable PTT for this conversation
response = await converse(
    "Hello",
    push_to_talk=True,
    ptt_key_combo="option_r"
)

# Or use global configuration
# BUMBA_PTT_ENABLED=true
response = await converse("Hello")
```

## Development Progress

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 1: Research & Design | ✅ Complete | 100% |
| Phase 2: Foundation Setup | ✅ Complete | 100% (6/6) |
| Phase 3: Core PTT | ⏳ Ready to Start | 0% |
| Phase 4: Transport Adaptation | ⏳ Not Started | 0% |
| Phase 5: Enhanced Features | ⏳ Not Started | 0% |
| Phase 6: Testing & Quality | ⏳ Not Started | 0% |
| Phase 7: Documentation | ⏳ Not Started | 0% |
| Phase 8: Release Preparation | ⏳ Not Started | 0% |
| Phase 9: Post-Release Support | ⏳ Not Started | 0% |

### Phase 2 Completed Sprints
- ✅ Sprint 2.1: Development Environment Setup
- ✅ Sprint 2.2: Keyboard Library Integration (pynput 1.8.1)
- ✅ Sprint 2.3: Configuration Extensions (19 config vars)
- ✅ Sprint 2.4: Logging Infrastructure (JSONL + session tracking)
- ✅ Sprint 2.5: Test Fixtures Setup (21 fixtures, 54 tests passing)
- ✅ Sprint 2.6: Documentation Structure (README, TESTING, CONTRIBUTING)

## Dependencies
- `pynput`: Cross-platform keyboard monitoring
- `sounddevice`: Audio recording
- `asyncio`: Async/await support

## Testing

### Quick Start

```bash
# Run all PTT unit tests
source .venv/bin/activate
python -m pytest tests/unit/ptt/ -v

# Run with coverage
python -m pytest tests/unit/ptt/ --cov=voice_mode.ptt --cov-report=html

# Run specific test file
python -m pytest tests/unit/ptt/test_keyboard_handler.py -v
```

### Test Coverage

| Component | Tests | Status |
|-----------|-------|--------|
| Keyboard Handler | 10 | ✅ All passing |
| Configuration | 7 | ✅ All passing |
| Logging | 16 | ✅ All passing |
| Test Fixtures | 21 | ✅ All passing |
| **Total** | **54** | **✅ 100%** |

For comprehensive testing documentation, see [TESTING.md](TESTING.md).

## Troubleshooting

### macOS Permission Issues

**Problem:** Keyboard events not detected on macOS

**Solution:**
1. Open System Preferences → Security & Privacy → Privacy → Accessibility
2. Grant accessibility permissions to your terminal or Python interpreter
3. Restart your application

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'voice_mode.ptt'`

**Solution:**
```bash
# Ensure package is installed in development mode
pip install -e .

# Or activate virtual environment
source .venv/bin/activate
```

### Key Combo Not Working

**Problem:** Key combination not triggering callbacks

**Debugging steps:**
```python
import os
os.environ["BUMBA_PTT_DEBUG"] = "true"
os.environ["BUMBA_PTT_LOG_KEYS"] = "true"

from voice_mode.ptt import KeyboardHandler
handler = KeyboardHandler("your_combo")
handler.start()
# Check logs for key events
```

### Common Questions

**Q: Can I use more than two keys in a combination?**
A: Phase 2 supports up to 2 keys. Multi-key support (3+) is planned for Phase 5.

**Q: What key names are supported?**
A: All standard keys from pynput: letters, numbers, function keys, arrow keys, modifiers (ctrl, alt, shift, cmd). See [pynput documentation](https://pynput.readthedocs.io/) for full list.

**Q: Does this work in production?**
A: Phase 2 provides foundation components. Full PTT integration is in Phase 3-4 (in development).

**Q: How do I contribute?**
A: See [CONTRIBUTING.md](CONTRIBUTING.md) for developer guidelines.

## References
- [Research Documentation](../../../docs/research/)
- [Sprint Plan](/Users/az/Desktop/PTT_Feature_Sprint_Plan.md)
- [Main Bumba Voice README](../../../README.md)
