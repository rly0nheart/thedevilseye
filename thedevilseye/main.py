#!/usr/bin/env python3

from thedevilseye.thedevilseye *


def main():
    devils_eye = TheDevilsEye() 
    # Parse command-line arguments
    parser = create_parser()
    args = parser.parse_args()

    start_time = datetime.now()
    xprint(banner)
    xprint(f"\n[[green]STARTED[/]] initialized: <time_dt={start_time}, engine=[green]{args.engine}[/], query=[green]{args.query}[/]>")
    try:
        devils_eye.search_ahmia_fi(query=args.query)
    except Exception as e:
        xprint(f"[[red]ERROR[/]] An error occurred: [red]{e}[/]")

    xprint(f"[[green]COMPLETE[/]] Complete: <time_sec={datetime.now() - start_time}>")
