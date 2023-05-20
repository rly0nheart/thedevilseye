import os
import time
from thedevilseye.thedevilseye import *


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def thedevilseye():
    if arguments.debug:
        
    xprint(f"{COLOURS['RED']}THEDEVILSEYE{COLOURS['RESET']} {current_version}-{COLOURS['RED']}hellfire#7{COLOURS['RESET']}")
    xprint(f"{COLOURS['GREEN']}[*]{COLOURS['RESET']} initialized <time_dt={time.asctime()}, query='{arguments.query}'> ...")
    try:
        get_hidden_services(query=arguments.query, result_count=arguments.count)
    except KeyboardInterrupt:
        xprint(f"{COLOURS['YELLOW']}[!]{COLOURS['RESET']} User interruption detected.")

    except Exception as e:
        xprint(f"{COLOURS['RED']}[x]{COLOURS['RESET']} An error occurred: {COLOURS['RED']}{e}{COLOURS['RESET']}")
