#!/usr/bin/env python3

from thedevilseye.thedevilseye import *


def create_parser():
    parser = argparse.ArgumentParser(description="Darkweb .onion link(s) extracting tool  — by Richard Mwewa | https://about.me/rly0nheart",epilog="thedevilseye scrapes darkweb search engines and gets information (.onion links, descriptions) requiring a Tor network. Developed by Richard Mwewa | https://about.me/rly0nheart")
    parser.add_argument('query', help='search quey')
    parser.add_argument("-d","--dump", metavar="path/to/file", help=argparse.SUPPRESS)
    return parser


def main():
    devils_eye = TheDevilsEye() 
    # Parse command-line arguments
    parser = create_parser()
    args = parser.parse_args()
    start_time = datetime.now()
    xprint("[[red]THEDEVILSEYE[/]] v2022.1.5.0-[red]hellfire#6[/]")
    xprint(f"\n[[green]STARTED[/]] initialized: <time_dt={start_time}, engine=[green]{args.engine}[/], query=[green]{args.query}[/]>")
    try:
        devils_eye.search_ahmia_fi(query=args.query)
    except Exception as e:
        xprint(f"[[red]ERROR[/]] An error occurred: [red]{e}[/]")

    xprint(f"[[green]COMPLETE[/]] Complete: <time_sec={datetime.now() - start_time}>")
