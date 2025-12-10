# Phase 5 Plan: Enhanced Features

**Phase:** Phase 5 - Enhanced Features
**Start Date:** 2025-11-09
**Status:** 📋 Planning
**Prerequisites:** Phase 4 Complete ✅

---

## Overview

Phase 5 focuses on enhancing the PTT user experience with visual feedback, audio cues, statistics tracking, and polish features that make PTT more intuitive and delightful to use.

**Philosophy:** Phase 4 made PTT work. Phase 5 makes PTT great.

---

## Goals

### Primary Goals

1. **Visual Feedback** - Clear terminal indicators showing PTT status
2. **Audio Cues** - Distinct sounds for PTT events (start, stop, cancel)
3. **Statistics Tracking** - Usage metrics and performance monitoring
4. **User Experience** - Polish, error messages, help system
5. **Configuration** - Easy setup, validation, and troubleshooting

### Success Criteria

- [ ] User can see PTT status without checking logs
- [ ] Audio cues provide clear feedback for all PTT events
- [ ] Statistics help users understand and optimize PTT usage
- [ ] Setup process is smooth and well-documented
- [ ] Error messages are clear and actionable

---

## Sprint Breakdown

### Sprint 5.1: Visual Feedback System

**Duration:** ~3 hours
**Deliverables:**
- Terminal status indicator module
- Recording status display
- Mode indicator (hold/toggle/hybrid)
- Duration counter
- Key hint display

**Components:**
```python
src/voice_mode/ptt/
├── visual_feedback.py     # Terminal UI components
├── status_display.py      # Status rendering
└── terminal_utils.py      # Terminal control utilities
```

**Features:**
- Colorized status messages (green=active, red=cancelled, yellow=waiting)
- Live duration counter during recording
- Current mode display
- Key combination hints
- Non-blocking terminal updates (doesn't interfere with logging)

**Tests:**
- Visual output formatting tests
- Terminal compatibility tests
- Color escape code tests
- Update rate tests

---

### Sprint 5.2: Audio Feedback System

**Duration:** ~4 hours
**Deliverables:**
- PTT-specific audio cue system
- Chime sounds for PTT events
- Volume control
- Audio feedback configuration

**Components:**
```python
src/voice_mode/ptt/
├── audio_feedback.py      # PTT audio cues
└── sounds/               # Audio files
    ├── ptt_start.wav     # Recording start chime
    ├── ptt_stop.wav      # Recording stop chime
    ├── ptt_cancel.wav    # Recording cancel sound
    └── ptt_waiting.wav   # Waiting for key press
```

**Features:**
- Distinct sounds for each PTT event
- Configurable volume (`PTT_FEEDBACK_VOLUME`)
- Option to disable (`PTT_AUDIO_FEEDBACK=false`)
- Non-blocking playback
- Works alongside existing voice_mode audio feedback

**Integration:**
- Integrate with existing `audio_feedback.py` module
- Respect global audio feedback settings
- PTT events play in addition to (not instead of) standard feedback

**Tests:**
- Audio playback tests
- Volume control tests
- Disable/enable tests
- Non-blocking verification

---

### Sprint 5.3: Statistics & Metrics

**Duration:** ~4 hours
**Deliverables:**
- PTT usage statistics tracking
- Performance metrics
- Session summaries
- Statistics export

**Components:**
```python
src/voice_mode/ptt/
├── statistics.py          # PTT statistics tracking
└── metrics.py            # Performance metrics
```

**Tracked Metrics:**
- Total recordings count
- Average recording duration
- Mode usage breakdown (hold/toggle/hybrid)
- Cancel rate
- Key press latency
- Recording start/stop latency
- Error rate
- Success rate

**Features:**
- Real-time statistics updates
- Session summaries at disable
- Export to JSON
- Integration with voice_mode statistics

**Tests:**
- Metric tracking tests
- Accuracy tests
- Export format tests
- Reset functionality tests

---

### Sprint 5.4: Configuration Validation & Setup

**Duration:** ~3 hours
**Deliverables:**
- Configuration validation system
- Setup wizard/helper
- Permission checker
- Configuration troubleshooting

**Components:**
```python
src/voice_mode/ptt/
├── config_validation.py   # Validate PTT config
├── setup_helper.py       # Interactive setup
└── permissions.py        # Permission checking
```

**Features:**
- Validate all PTT config variables on startup
- Check keyboard permissions (macOS accessibility)
- Verify audio device availability
- Interactive setup for first-time users
- Configuration recommendations
- Troubleshooting diagnostics

**Validation Checks:**
- Valid key combinations
- Valid mode selection
- Reasonable timeout values
- Audio device availability
- Keyboard permissions granted
- Sound files present (if audio feedback enabled)

**Tests:**
- Configuration validation tests
- Permission check tests (mocked)
- Setup workflow tests
- Error message tests

---

### Sprint 5.5: Error Messages & Help System

**Duration:** ~2 hours
**Deliverables:**
- Improved error messages
- Context-sensitive help
- Troubleshooting guide
- Error recovery suggestions

**Components:**
```python
src/voice_mode/ptt/
├── error_messages.py      # Clear error messages
└── help_system.py        # Context help
```

**Features:**
- Clear, actionable error messages
- Suggestions for fixing common issues
- Link to documentation
- Context-aware help (depends on current state)
- Common issues FAQ

**Error Message Examples:**
```
Before: "Failed to enable PTT controller"
After:  "❌ Could not enable PTT: Keyboard permissions not granted.
         → Grant accessibility permissions in System Preferences
         → See: docs/ptt/troubleshooting.md#macos-permissions"

Before: "Invalid key combo"
After:  "❌ Invalid key combination 'control+space'
         → Use 'ctrl+space' (not 'control')
         → Valid modifiers: ctrl, shift, alt, cmd
         → Example: 'ctrl+shift+r' or 'down+right'"
```

**Tests:**
- Error message format tests
- Help context tests
- Link generation tests
- Example validation tests

---

### Sprint 5.6: Cancel Key Enhancement

**Duration:** ~2 hours
**Deliverables:**
- Verify cancel key functionality
- Enhanced cancel feedback
- Cancel statistics
- Cancel key tests

**Components:**
- Verify existing cancel key implementation
- Add visual/audio feedback for cancel
- Track cancel statistics
- Improve cancel key documentation

**Features:**
- Visual feedback when cancel key pressed
- Audio cue for cancellation
- Track cancel rate in statistics
- Display cancel key in status/help

**Tests:**
- Cancel key functionality tests
- Cancel feedback tests
- Cancel statistics tests
- Cancel in different modes tests

---

### Sprint 5.7: Performance Optimization

**Duration:** ~3 hours
**Deliverables:**
- Profile PTT performance
- Optimize hot paths
- Reduce latency
- Memory usage optimization

**Focus Areas:**
- Keyboard event processing latency
- State transition speed
- Audio buffer management
- Memory allocation reduction

**Optimization Targets:**
- Key press to recording start: <50ms → <30ms
- Recording stop latency: <100ms → <50ms
- Memory overhead: ~10KB → <5KB
- CPU usage during idle: <1% → <0.5%

**Tests:**
- Performance benchmark tests
- Latency measurement tests
- Memory profiling tests
- CPU usage tests

---

### Sprint 5.8: Integration & Polish

**Duration:** ~3 hours
**Deliverables:**
- Integrate all Phase 5 features
- End-to-end testing
- Documentation updates
- Phase 5 completion report

**Tasks:**
- Ensure all features work together
- Update configuration documentation
- Update API reference
- Create Phase 5 summary document
- Update examples with new features
- Run full test suite
- Performance regression testing

**Deliverables:**
- Phase 5 integration tests
- Updated documentation
- Phase 5 completion report
- Updated examples

---

## Technical Architecture

### Visual Feedback Architecture

```
PTTController
  ↓ (state changes)
StatusDisplay
  ├─ TerminalRenderer (colorized output)
  ├─ ModeIndicator (hold/toggle/hybrid)
  ├─ DurationCounter (live timer)
  └─ KeyHints (show active keys)
```

### Audio Feedback Integration

```
PTT Event
  ↓
PTTAudioFeedback
  ├─ Check PTT_AUDIO_FEEDBACK config
  ├─ Select appropriate sound file
  ├─ Play via non-blocking audio
  └─ Respect PTT_FEEDBACK_VOLUME

Standard Audio Feedback (existing)
  └─ Continues to work independently
```

### Statistics Architecture

```
PTTStatistics (singleton)
  ├─ Metric collectors
  ├─ Session tracking
  ├─ Aggregation logic
  └─ Export functionality

PTTController
  ↓ (events)
PTTStatistics.record_event()
  ↓
Metrics updated

User requests stats
  ↓
PTTStatistics.get_summary()
```

---

## Configuration Updates

### New Configuration Variables

```bash
# Visual Feedback
export BUMBA_PTT_VISUAL_FEEDBACK=true           # Enable terminal indicators
export BUMBA_PTT_VISUAL_STYLE=compact           # compact, detailed, minimal
export BUMBA_PTT_SHOW_KEY_HINTS=true            # Show key combination hints
export BUMBA_PTT_SHOW_DURATION=true             # Show live duration counter

# Audio Feedback
export BUMBA_PTT_AUDIO_FEEDBACK=true            # Enable PTT audio cues
export BUMBA_PTT_FEEDBACK_VOLUME=0.7            # Volume (0.0-1.0)
export BUMBA_PTT_CUSTOM_SOUNDS_DIR=/path/       # Custom sound files

# Statistics
export BUMBA_PTT_STATISTICS=true                # Track PTT statistics
export BUMBA_PTT_STATS_AUTO_EXPORT=false        # Auto-export on disable
export BUMBA_PTT_STATS_EXPORT_PATH=/path/       # Export directory

# Setup & Validation
export BUMBA_PTT_VALIDATE_CONFIG=true           # Validate on startup
export BUMBA_PTT_INTERACTIVE_SETUP=false        # Interactive first-time setup
export BUMBA_PTT_SHOW_STARTUP_HELP=true         # Show help on first enable
```

---

## File Structure

```
src/voice_mode/ptt/
├── __init__.py                  # Exports (updated)
├── controller.py                # Existing
├── state_machine.py             # Existing
├── keyboard_handler.py          # Existing
├── recorder.py                  # Existing
├── logger.py                    # Existing
├── transport_adapter.py         # Existing (Phase 4)
│
├── visual_feedback.py           # NEW: Visual indicators
├── status_display.py            # NEW: Status rendering
├── terminal_utils.py            # NEW: Terminal control
│
├── audio_feedback.py            # NEW: PTT audio cues
├── sounds/                      # NEW: Audio files
│   ├── ptt_start.wav
│   ├── ptt_stop.wav
│   ├── ptt_cancel.wav
│   └── ptt_waiting.wav
│
├── statistics.py                # NEW: Statistics tracking
├── metrics.py                   # NEW: Performance metrics
│
├── config_validation.py         # NEW: Config validation
├── setup_helper.py              # NEW: Setup wizard
├── permissions.py               # NEW: Permission checking
│
├── error_messages.py            # NEW: Error messages
└── help_system.py               # NEW: Help system

tests/unit/ptt/
├── test_controller.py           # Existing
├── test_state_machine.py        # Existing
├── test_keyboard_handler.py     # Existing
├── test_recorder.py             # Existing
├── test_transport_adapter.py    # Existing (Phase 4)
│
├── test_visual_feedback.py      # NEW
├── test_status_display.py       # NEW
├── test_audio_feedback.py       # NEW
├── test_statistics.py           # NEW
├── test_config_validation.py    # NEW
├── test_setup_helper.py         # NEW
└── test_error_messages.py       # NEW

tests/integration/ptt/
├── test_converse_integration.py # Existing (Phase 4)
├── test_phase5_integration.py   # NEW: Phase 5 features
└── test_end_to_end.py          # NEW: Complete workflow

docs/ptt/
├── PHASE_4_COMPLETION_REPORT.md # Existing
├── PHASE_5_PLAN.md              # This document
├── PHASE_5_COMPLETION_REPORT.md # To be created (Sprint 5.8)
├── SPRINT_5.*.md                # Sprint summaries (to be created)
└── TROUBLESHOOTING.md           # NEW: Troubleshooting guide
```

---

## Dependencies

### New Python Dependencies

**Optional (for enhanced visuals):**
- `rich` - Rich terminal output (optional, graceful fallback to basic)
- `colorama` - Cross-platform colored terminal text

**Audio:**
- Existing: `sounddevice`, `numpy`
- No new dependencies (will generate/include audio files)

### Audio Files

**Source:**
- Generate simple tones using `numpy` + `sounddevice`
- Or include pre-generated WAV files
- Keep file size small (<10KB each)

**Format:**
- WAV, 16kHz, mono
- Short duration (100-200ms)
- Clear, distinct sounds

---

## Testing Strategy

### Unit Tests

**Target:** 100 new unit tests across Phase 5 features

**Coverage:**
- Visual feedback rendering
- Audio feedback playback
- Statistics tracking accuracy
- Configuration validation
- Error message formatting
- Help system context
- Performance benchmarks

### Integration Tests

**Target:** 15 new integration tests

**Scenarios:**
- Visual + audio feedback together
- Statistics tracking during actual recording
- Configuration validation + setup wizard
- Error recovery with feedback
- Complete workflow with all features enabled

### Manual Tests

**Focus:**
- Visual appearance in different terminals
- Audio cue distinctness and volume
- Statistics accuracy verification
- Setup wizard usability
- Error message clarity

---

## Documentation

### User Documentation

**To Create:**
1. **Troubleshooting Guide** (`TROUBLESHOOTING.md`)
   - Common issues and solutions
   - Platform-specific gotchas
   - Permission problems
   - Audio issues
   - Configuration problems

2. **Configuration Guide** (`CONFIGURATION.md`)
   - All PTT configuration variables
   - Recommended settings by use case
   - Examples
   - Validation

3. **Statistics Guide** (`STATISTICS.md`)
   - Metrics explained
   - How to interpret statistics
   - Export format
   - Integration with analytics

### Developer Documentation

**To Update:**
- API reference with new components
- Architecture diagrams
- Integration points
- Testing guide

---

## Performance Targets

### Latency Targets

| Metric | Current (Phase 4) | Target (Phase 5) |
|--------|------------------|------------------|
| Key press → Recording start | <50ms | <30ms |
| Recording stop latency | <100ms | <50ms |
| State transition | <5ms | <3ms |
| Visual update rate | N/A | 60 FPS |

### Resource Targets

| Resource | Current (Phase 4) | Target (Phase 5) |
|----------|------------------|------------------|
| CPU (idle) | <1% | <0.5% |
| CPU (recording) | <5% | <3% |
| Memory overhead | ~10KB | <5KB |
| Startup time | ~100ms | <50ms |

---

## Acceptance Criteria

Phase 5 is complete when ALL of the following are met:

### Feature Completeness
- [ ] Visual feedback system implemented and tested
- [ ] Audio cues for all PTT events
- [ ] Statistics tracking functional
- [ ] Configuration validation working
- [ ] Error messages improved
- [ ] Cancel key verified/enhanced
- [ ] Performance optimizations applied

### Testing
- [ ] 100+ new unit tests passing (100%)
- [ ] 15+ new integration tests passing (100%)
- [ ] Manual testing completed on macOS, Linux, Windows
- [ ] Performance benchmarks meet targets
- [ ] No regressions from Phase 4

### Quality
- [ ] All features work together seamlessly
- [ ] No conflicts between visual and audio feedback
- [ ] Statistics accurate and useful
- [ ] Error messages clear and actionable
- [ ] Help system context-aware

### Documentation
- [ ] Troubleshooting guide created
- [ ] Configuration guide updated
- [ ] Statistics guide created
- [ ] API reference updated
- [ ] Examples updated with new features
- [ ] Phase 5 completion report written

### User Experience
- [ ] Setup process smooth (first-time users)
- [ ] Visual feedback non-intrusive
- [ ] Audio cues distinct and pleasant
- [ ] Statistics helpful for optimization
- [ ] Error recovery intuitive

---

## Risk Assessment

### Technical Risks

**1. Terminal Compatibility**
- **Risk:** Visual feedback may not work on all terminals
- **Mitigation:** Graceful fallback to basic output, detect terminal capabilities
- **Impact:** Medium

**2. Audio Playback Conflicts**
- **Risk:** PTT audio cues may conflict with existing audio feedback
- **Mitigation:** Coordinate with existing system, non-blocking playback
- **Impact:** Low

**3. Performance Regression**
- **Risk:** New features may slow down PTT
- **Mitigation:** Performance benchmarking, optimization sprint
- **Impact:** Low

### User Experience Risks

**1. Visual Noise**
- **Risk:** Too much visual feedback may be distracting
- **Mitigation:** Configurable styles (minimal/compact/detailed)
- **Impact:** Medium

**2. Audio Annoyance**
- **Risk:** Audio cues may become annoying with frequent use
- **Mitigation:** Volume control, disable option, pleasant sounds
- **Impact:** Medium

---

## Success Metrics

Phase 5 will be considered successful if:

1. **User Satisfaction:**
   - Users can operate PTT without checking logs
   - Visual feedback is clear but not intrusive
   - Audio cues are helpful and pleasant

2. **Code Quality:**
   - 100% test coverage for new features
   - No performance regressions
   - All automated tests passing

3. **Usability:**
   - First-time setup success rate >90%
   - Error recovery success rate >95%
   - Configuration validation catches all invalid configs

4. **Performance:**
   - All performance targets met
   - Resource overhead <5KB memory, <0.5% CPU
   - Latency targets achieved

---

## Timeline

**Total Estimated Duration:** ~24 hours of development

| Sprint | Duration | Focus |
|--------|----------|-------|
| 5.1 | 3h | Visual Feedback System |
| 5.2 | 4h | Audio Feedback System |
| 5.3 | 4h | Statistics & Metrics |
| 5.4 | 3h | Configuration & Setup |
| 5.5 | 2h | Error Messages & Help |
| 5.6 | 2h | Cancel Key Enhancement |
| 5.7 | 3h | Performance Optimization |
| 5.8 | 3h | Integration & Polish |

**Estimated Completion:** ~24 hours from start

---

## Next Phase Preview

### Phase 6: Cross-Platform Testing

After Phase 5 completion:
- Comprehensive testing on macOS, Linux, Windows
- Platform-specific bug fixes
- Performance testing across platforms
- Accessibility testing
- Edge case validation

---

## Notes

- Phase 5 focuses on user experience and polish
- All features should be configurable (can be disabled)
- Maintain backward compatibility
- Keep resource overhead minimal
- Prioritize clarity and usability over features

---

**Document Version:** 1.0
**Date:** 2025-11-09
**Phase:** 5 - Enhanced Features
**Status:** 📋 Planning (Ready to Begin)
**Prerequisites:** Phase 4 Complete ✅
