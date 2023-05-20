import os
import time
from thedevilseye.thedevilseye import *


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def thedevilseye():
    clear_screen()
    xprint(f"thedevilseye v{current_version} - {time.asctime()}\n")
    xprint(f"{COLOURS['GREEN']}[*]{COLOURS['RESET']} initialized <query='{arguments.query}', result_count={arguments.count}> ...")
    try:
        check_updates()
        get_hidden_services(query=arguments.query, result_count=int(arguments.count))
    except KeyboardInterrupt:
        xprint(f"{COLOURS['YELLOW']}[!]{COLOURS['RESET']} User interruption detected.")

    except Exception as e:
        xprint(f"{COLOURS['RED']}[x]{COLOURS['RESET']} An error occurred: {COLOURS['RED']}{e}{COLOURS['RESET']}")
