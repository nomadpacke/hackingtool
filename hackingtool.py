#!/usr/bin/env python3
"""HackingTool - A collection of hacking tools for security researchers.

This is the main entry point for the hackingtool application.
It provides a menu-driven interface to access various security tools.
"""

import os
import sys
import subprocess

# Ensure the script is run with Python 3
if sys.version_info[0] < 3:
    print("[!] HackingTool requires Python 3. Please use Python 3.")
    sys.exit(1)


BANNER = r"""
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
              ████████╗ ██████╗  ██████╗ ██╗
              ╚══██╔══╝██╔═══██╗██╔═══██╗██║
                 ██║   ██║   ██║██║   ██║██║
                 ██║   ██║   ██║██║   ██║██║
                 ██║   ╚██████╔╝╚██████╔╝███████╗
                 ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
"""

AUTHOR = "Z4nzu (Fork)"
VERSION = "1.1.0"


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    """Display the application banner."""
    clear_screen()
    print(BANNER)
    print(f"  [*] Version  : {VERSION}")
    print(f"  [*] Author   : {AUTHORS}")
    print(f"  [*] GitHub   : https://github.com/Z4nzu/hackingtool")
    print()


def check_root():
    """Check if the script is running with root privileges."""
    if os.geteuid() != 0:
        print("[!] Warning: Some tools may require root privileges.")
        print("    Consider running with: sudo python3 hackingtool.py")
        print()


def check_dependencies():
    """Check if required system dependencies are available."""
    required = ["git", "python3", "pip3"]
    missing = []
    for dep in required:
        result = subprocess.run(
            ["which", dep],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode != 0:
            missing.append(dep)
    if missing:
        print(f"[!] Missing dependencies: {', '.join(missing)}")
        print("    Please install them before continuing.")
        sys.exit(1)


def get_main_menu():
    """Return the main menu categories."""
    return [
        ("Anonymous Surfing Tools",),
        ("Information Gathering Tools",),
        ("Wordlist Generator",),
        ("Wireless Attack Tools",),
        ("SQL Injection Tools",),
        ("Phishing Attack Tools",),
        ("Web Attack Tools",),
        ("Post Exploitation Tools",),
        ("Forensics Tools",),
        ("Payload Creation Tools",),
        ("Exploit Framework Tools",),
        ("Reverse Engineering Tools",),
        ("DDOS Attack Tools",),
        ("Remote Administrator Tools (RAT)",),
        ("XSS Attack Tools",),
        ("Steganography Tools",),
        ("SocialMedia Brute Force",),
        ("Android Hacking Tools",),
        ("IDN Homograph Attack Tools",),
        ("Email Verify Tools",),
        ("Hash Cracking Tools",),
        ("Wifi Deauthenticate",),
        ("All In One Tools",),
        ("Exit",),
    ]


def display_menu(menu_items):
    """Display a numbered menu from a list of items."""
    for idx, item in enumerate(menu_items, start=0):
        print(f"  [{idx:02d}] {item[0]}")
    print()


def main():
    """Main entry point for HackingTool."""
    try:
        print_banner()
        check_root()
        check_dependencies()

        menu_items = get_main_menu()

        while True:
            display_menu(menu_items)
            try:
                choice = input("[>>] Select an option: ").strip()
                if not choice.isdigit():
                    print("[!] Invalid input. Please enter a number.")
                    continue

                choice = int(choice)
                exit_index = len(menu_items) - 1

                if choice == exit_index:
                    print("\n[*] Exiting HackingTool. Goodbye!")
                    sys.exit(0)
                elif 0 <= choice < len(menu_items):
                    print(f"\n[*] Launching: {menu_items[choice][0]} ...")
                    # Tool category modules will be imported and invoked here
                else:
                    print("[!] Option out of range. Try again.")

            except KeyboardInterrupt:
                print("\n\n[*] Interrupted by user. Exiting...")
                sys.exit(0)

    except Exception as exc:
        print(f"[!] Unexpected error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
