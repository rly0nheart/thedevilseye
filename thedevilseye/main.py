#!/usr/bin/env python3

import os
from thedevilseye.thedevilseye import *


def create_parser():
    parser = argparse.ArgumentParser(description="Get tor hidden services and descriptions that match with the users query  — by Richard Mwewa | https://about.me/rly0nheart",epilog="thedevilseye is an osint tool that uses Ahmia.fi to get Tor hidden services and descriptions that match with the users query.")
    parser.add_argument('query', help='search quey')
    parser.add_argument("-d","--dump", metavar="path/to/file", help=argparse.SUPPRESS)
    return parser


def main():
    devils_eye = TheDevilsEye() 
    # Parse command-line arguments
    parser = create_parser()
    args = parser.parse_args()
    start_time = datetime.now()
    
    os.system("cls" if os.name == "nt" else "clear")
    xprint(f"{RED}THEDEVILSEYE{RESET} 1.5.2-{RED}hellfire#7{RESET}")
    xprint(f"\n[{GREEN}*{RESET}] initialized <time_dt={start_time}, query='{args.query}'> ...")
    try:
        devils_eye.search_ahmia_fi(query=args.query)
    except Exception as e:
        xprint(f"[{RED}x{RESET}] An error occurred: {RED}{e}{RESET}")

    xprint(f"[{GREEN}-{RESET}] Complete <time_sec={datetime.now() - start_time}>")
