
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

console = Console()

import config as config

def print_section_header(message):
    """
    Print a formatted section header.

    Args:
        message (str): The message to be displayed in the header.
    """
    print("\n" + "=" * config.TERMINAL_WIDTH)
    print(f'\033[1m{message.center(config.TERMINAL_WIDTH)}\033[0m')
    print("=" * config.TERMINAL_WIDTH + "\n")


def styled_print(icon: str, text: str, color: str, bold: bool = True, panel: bool = False):
    """Prints formatted text with an icon, color, and optional bold styling inside a panel."""
    style = f"bold {color}" if bold else color
    message = f"{icon} [{style}]{text}[/{style}]"
    
    if panel:
        console.print(Panel(message, expand=False, border_style=color))
    else:
        console.print(message)