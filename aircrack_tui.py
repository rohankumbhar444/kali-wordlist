
#!/usr/bin/env python3
import os
import curses
from curses import wrapper

def select_file(stdscr, prompt, filetype):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, f"{prompt} ({filetype}): ")
    file_path = stdscr.getstr(1, 0, 100).decode("utf-8").strip()
    stdscr.clear()
    return file_path

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Aircrack-ng TUI Tool for Kali Linux")
    stdscr.addstr(1, 0, "-----------------------------------")
    stdscr.addstr(3, 0, "1. Enter .cap file path")
    stdscr.addstr(4, 0, "2. Enter wordlist (.txt) file path")
    stdscr.addstr(5, 0, "3. Start cracking")
    stdscr.addstr(7, 0, "Press any key to continue...")
    stdscr.getch()

    cap_file = select_file(stdscr, "Enter path to .cap file", "*.cap")
    wordlist = select_file(stdscr, "Enter path to wordlist file", "*.txt")

    stdscr.clear()
    stdscr.addstr(0, 0, f"Running aircrack-ng with:")
    stdscr.addstr(1, 0, f"CAP file   : {cap_file}")
    stdscr.addstr(2, 0, f"Wordlist   : {wordlist}")
    stdscr.addstr(4, 0, "Cracking started in new terminal...")

    stdscr.refresh()
    curses.napms(2000)

    cmd = f"x-terminal-emulator -e 'aircrack-ng "{cap_file}" -w "{wordlist}"'"
    os.system(cmd)

wrapper(main)
