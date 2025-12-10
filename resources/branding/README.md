# Branding Directory 🎨

This directory contains BUMBA's branding assets as part of the BUMBA Platform.

## Files

- **branding.py** - Core branding module
  - BUMBA Platform color gradients
  - BUMBA ASCII logo with gradient support
  - Emoji set for consistent UI elements
  - Terminal color utilities

## Color Palette

BUMBA Platform gradient colors:
- 🟢 Green: RGB(0, 170, 0)
- 🟡 Yellow-Green: RGB(102, 187, 0)
- 🟡 Yellow: RGB(255, 221, 0)
- 🟠 Orange-Yellow: RGB(255, 170, 0)
- 🟠 Orange-Red: RGB(255, 102, 0)
- 🔴 Red: RGB(221, 0, 0)

## Emoji Set

Limited brand emojis:
- 🎙️ Voice/Audio features
- 🟢 Success states
- 🟡 Warning states
- 🔴 Error states
- 🟠 Info/Notice states
- 🏁 Completion states

## Usage

```python
from branding.branding import display_logo, Colors

# Display BUMBA logo with gradient
display_logo()

# Use brand colors
print(f"{Colors.GREEN}Success!{Colors.ENDC}")
```