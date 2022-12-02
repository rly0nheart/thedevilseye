#!/usr/bin/env python3

from datetime import datetime
from rich import print as xprint
from thedevilseye.banner import banner
from thedevilseye.thedevilseye import TheDevilsEye
from thedevilseye.thedevilseye import create_parser


def main():
    devils_eye = TheDevilsEye() 
    # Parse command-line arguments
    parser = create_parser()
    args = parser.parse_args()

    start_time = datetime.now()
    xprint(banner)
    xprint(f"\n[[green]STARTED[/]] initialized: <time_dt={start_time}, engine=[green]{args.engine}[/], query=[green]{args.query}[/]>")

    if args.query == None:
        exit('[[red]NEGATIVE[/]] Search query not specified (-q/--query).')
    if args.engine == 'ahmia.fi':
        devils_eye.search_ahmia_fi(query=args.query)
    elif args.engine == 'tor.link':
        devils_eye.search_tor_link(query=args.query)
    else:
      exit('thedevilseye: use -h/--help to show usage.')

    xprint(f"[[green]COMPLETE[/]] Complete: <time_sec={datetime.now() - start_time}>")
