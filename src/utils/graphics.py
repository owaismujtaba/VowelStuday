
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