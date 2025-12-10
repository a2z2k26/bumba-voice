#!/usr/bin/env python3
"""
BUMBA Brand Identity - Part of the BUMBA Platform
===================================================
Building Unified Multi-agent Business Applications
Professional • Intelligent • Secure • Enterprise-Ready
"""

# BUMBA Platform Color Palette (shared across all BUMBA products)
COLORS = {
    # Primary gradient (Green → Yellow → Orange → Red)
    'gradient': {
        'green': '\033[38;2;0;170;0m',        # Rich green
        'yellowGreen': '\033[38;2;102;187;0m', # Yellow-green
        'yellow': '\033[38;2;255;221;0m',      # Golden yellow
        'orangeYellow': '\033[38;2;255;170;0m', # Orange-yellow
        'orangeRed': '\033[38;2;255;102;0m',   # Orange-red
        'red': '\033[38;2;221;0;0m'            # Deep red
    },

    # Department colors (matching BUMBA emoji system)
    'departments': {
        'strategy': '\033[38;2;255;215;0m',    # Yellow (🟡)
        'backend': '\033[38;2;0;255;0m',       # Green (🟢)
        'frontend': '\033[38;2;255;0;0m',      # Red (🔴)
        'testing': '\033[38;2;255;165;0m',     # Orange (🟠)
        'completion': '\033[97m'                # White (🏁)
    },

    # Semantic colors
    'success': '\033[92m',    # Green
    'warning': '\033[93m',    # Yellow
    'error': '\033[91m',      # Red
    'info': '\033[96m',       # Cyan
    'primary': '\033[97m',    # White
    'secondary': '\033[90m',  # Gray

    # Brand accent colors (BUMBA spec)
    'gold': '\033[38;2;212;175;55m',      # Brand gold #D4AF37
    'wheat': '\033[38;2;245;222;179m',    # Brand wheat #F5DEB3
    'border': '\033[38;2;255;221;0m',     # Golden yellow borders

    # Standard
    'bold': '\033[1m',
    'underline': '\033[4m',
    'end': '\033[0m'
}

# BUMBA ASCII Logo (matching BUMBA style)
BUMBA_LOGO = [
    ' ██████╗██╗  ██╗ █████╗ ████████╗████████╗ █████╗ ',
    '██╔════╝██║  ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗',
    '██║     ███████║███████║   ██║      ██║   ███████║',
    '██║     ██╔══██║██╔══██║   ██║      ██║   ██╔══██║',
    '╚██████╗██║  ██║██║  ██║   ██║      ██║   ██║  ██║',
    ' ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝'
]

# BUMBA Compact Logo (BUMBA-styled box)
BUMBA_LOGO_COMPACT = [
    '╔════════════════════════════════════════════╗',
    '║   ____ _   _    _  _____ _____  _         ║',
    '║  / ___| | | |  / \\|_   _|_   _|/ \\        ║',
    '║ | |   | |_| | / _ \\ | |   | | / _ \\       ║',
    '║ | |___|  _  |/ ___ \\| |   | |/ ___ \\      ║',
    '║  \\____|_| |_/_/   \\_\\_|   |_/_/   \\_\\     ║',
    '║                                            ║',
    '║  Natural Voice Conversations for AI        ║',
    '║  Building Unified Multi-agent Business     ║',
    '║            Applications                    ║',
    '╚════════════════════════════════════════════╝'
]

# Simple text version for minimal contexts
BUMBA_SIMPLE = 'BUMBA - Natural Voice Conversations • Part of BUMBA Platform'

# Official BUMBA Platform emoji set (ONLY these are permitted)
EMOJIS = {
    'strategy': '🟡',      # ProductStrategist Department
    'backend': '🟢',       # BackendEngineer Department
    'frontend': '🔴',      # DesignEngineer Department
    'testing': '🟠',       # Testing & QA
    'completion': '🏁'     # Task Complete
}

def apply_gradient(text_lines):
    """Apply BUMBA gradient colors to ASCII art."""
    result = []
    gradient_colors = list(COLORS['gradient'].values())
    
    for index, line in enumerate(text_lines):
        # Calculate color index based on line position
        color_index = int((index / len(text_lines)) * len(gradient_colors))
        color = gradient_colors[min(color_index, len(gradient_colors) - 1)]
        result.append(f"{color}{COLORS['bold']}{line}{COLORS['end']}")
    
    return result

def display_logo(variant='main', clear=False):
    """Display BUMBA logo with BUMBA gradient."""
    import os
    
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    logo = BUMBA_LOGO if variant == 'main' else BUMBA_LOGO_COMPACT
    colored_logo = apply_gradient(logo)
    
    for line in colored_logo:
        print(line)

def create_header(title, width=60):
    """Create a branded header with BUMBA styling."""
    border_color = COLORS['border']
    gold = COLORS['gold']
    
    lines = []
    lines.append(f"{border_color}{'═' * width}{COLORS['end']}")
    
    # Center the title
    padding = (width - len(title) - 2) // 2
    title_line = f"{gold}{COLORS['bold']} {' ' * padding}{title}{' ' * (width - len(title) - padding - 2)} {COLORS['end']}"
    lines.append(title_line)
    
    lines.append(f"{border_color}{'═' * width}{COLORS['end']}")
    
    return '\n'.join(lines)

def create_box(content, style='default'):
    """Create a branded box around content."""
    lines = content.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + 4
    
    border_color = COLORS['border']
    
    result = []
    result.append(f"{border_color}╔{'═' * (width - 2)}╗{COLORS['end']}")
    
    for line in lines:
        padding = width - len(line) - 4
        result.append(f"{border_color}║{COLORS['end']} {line}{' ' * padding} {border_color}║{COLORS['end']}")
    
    result.append(f"{border_color}╚{'═' * (width - 2)}╝{COLORS['end']}")
    
    return '\n'.join(result)

def format_status(status, message):
    """Format status messages with appropriate colors and emojis."""
    status_config = {
        'success': (COLORS['success'], EMOJIS['success']),
        'warning': (COLORS['warning'], EMOJIS['warning']),
        'error': (COLORS['error'], EMOJIS['error']),
        'info': (COLORS['info'], EMOJIS['info']),
        'complete': (COLORS['success'], EMOJIS['complete'])
    }
    
    color, emoji = status_config.get(status, (COLORS['info'], EMOJIS['info']))
    return f"{emoji} {color}{message}{COLORS['end']}"

def create_progress_bar(current, total, width=30):
    """Create a progress bar with BUMBA gradient colors."""
    percentage = int((current / total) * 100)
    filled = int((current / total) * width)
    empty = width - filled
    
    # Use gradient colors for filled portion
    bar = f"{COLORS['gradient']['green']}{'█' * filled}{COLORS['secondary']}{'░' * empty}{COLORS['end']}"
    
    return f"{bar} {percentage}%"

def get_brand_info():
    """Get BUMBA brand information."""
    return {
        'name': 'BUMBA',
        'fullName': 'Conversational Hybrid Assistant for Text-To-Audio',
        'platform': 'BUMBA Platform',
        'version': '3.34.3',
        'tagline': 'Natural Voice Conversations for AI Assistants',
        'description': 'Part of the BUMBA Platform Suite'
    }

# Installation banner for BUMBA
def display_installation_banner(version='3.34.3', show_features=True):
    """Display BUMBA installation banner with full BUMBA branding."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display logo with gradient
    display_logo('main')

    print()
    print(f"{COLORS['gold']}{'▄' * 52}{COLORS['end']}")
    print(f"{COLORS['gold']}{COLORS['bold']}🏁 BUMBA VOICE MODE FRAMEWORK 🏁{COLORS['end']}")
    print(f"{COLORS['gold']}{'▀' * 52}{COLORS['end']}")
    print()
    print(f"{COLORS['wheat']}Professional • Intelligent • Secure{COLORS['end']}")
    print(f"{COLORS['wheat']}Enterprise-Ready • BUMBA Platform Integrated{COLORS['end']}")
    print()
    print(f"{COLORS['secondary']}By BUMBA Platform Team • v{version}{COLORS['end']}")

    if show_features:
        print()
        print(f"{COLORS['primary']}Features:{COLORS['end']}")
        print(format_status('success', 'Multi-agent voice coordination'))
        print(format_status('warning', 'Professional TTS/STT integration'))
        print(format_status('error', 'Enterprise-grade security'))
        print(format_status('info', 'Real-time WebRTC support'))
        print(format_status('complete', 'Production-ready deployment'))
    print(f"{COLORS['gold']}{'▀' * 52}{COLORS['end']}")
    print()
    print(f"{COLORS['wheat']}Natural Voice Conversations • AI Assistant Integration{COLORS['end']}")
    print(f"{COLORS['wheat']}Enterprise-Ready • Part of BUMBA Platform{COLORS['end']}")
    print()
    print(f"{COLORS['secondary']}By BUMBA Platform Team • v{get_brand_info()['version']}{COLORS['end']}")
    print()

def display_completion_banner():
    """Display completion banner."""
    print()
    print(f"{COLORS['gradient']['green']}{'═' * 52}{COLORS['end']}")
    print(f"{EMOJIS['complete']} {COLORS['gradient']['green']}{COLORS['bold']}INSTALLATION COMPLETE{COLORS['end']} {EMOJIS['complete']}")
    print(f"{COLORS['gradient']['green']}{'═' * 52}{COLORS['end']}")
    print()
    print(f"{COLORS['success']}✓ BUMBA is ready for voice conversations{COLORS['end']}")
    print(f"{COLORS['success']}✓ Part of the BUMBA Platform Suite{COLORS['end']}")
    print()
    print(f"{COLORS['info']}Run 'bumba' to start using voice mode{COLORS['end']}")
    print(f"{COLORS['info']}Run 'bumba --help' for more options{COLORS['end']}")
    print()

if __name__ == "__main__":
    # Demo the branding
    display_installation_banner()
    print()
    print(create_header("BUMBA Features"))
    print()
    print(format_status('success', 'OpenAI-compatible TTS/STT'))
    print(format_status('success', 'Local Whisper.cpp integration'))
    print(format_status('success', 'Kokoro TTS with multiple voices'))
    print(format_status('success', 'LiveKit real-time communication'))
    print(format_status('info', 'MCP tool integration'))
    print()
    print("Installation Progress:")
    print(create_progress_bar(85, 100, 40))
    print()
    display_completion_banner()