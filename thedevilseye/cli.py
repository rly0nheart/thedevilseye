import argparse

import pandas as pd
from requests import Session
from rich import box
from rich.table import Table

from .main import get_hidden_services, check_updates
from .utils import console, export_dataframe, print_banner
from .version import Version


def arg_parser():
    author: str = "Richard Mwewa"
    parser = argparse.ArgumentParser(
        description=f"thedevilseye — by {author} | https://gravatar.com/rly0nheart",
        epilog="An OSINT tool that uses Ahmia.fi to get hidden Tor "
        "services and descriptions that match with the user's query.",
    )
    parser.add_argument("query", help="search query")
    parser.add_argument(
        "-e",
        "--export",
        type=str,
        help="a comma-separated list of file types to export the output to (supported: csv,html,json,xml)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"thedevilseye {Version.release} © GPL-3.0 License {author}. All rights reserved.",
    )
    return parser.parse_args()


def start():
    args = arg_parser()
    console.clear()
    print_banner()
    with console.status("Establishing connection w/ new session...") as status:
        try:
            session = Session()
            check_updates(session=session)
            results = get_hidden_services(
                query=args.query, status=status, session=session
            )
            dataframe = pd.DataFrame(results)
            # Display as rich table
            if not dataframe.empty:
                table = Table(show_header=True, header_style="bold magenta", box=box.ASCII, highlight=True)

                for column in dataframe.columns:
                    table.add_column(column, overflow="fold", max_width=60)

                for _, row in dataframe.iterrows():
                    table.add_row(*(str(cell) if pd.notna(cell) else "" for cell in row))

                console.print(table)
            else:
                console.print("[bold yellow]No results found.[/]")
            if args.export:
                export_dataframe(
                    dataframe=dataframe,
                    filename=args.query,
                    formats=args.export.split(","),
                )

        except KeyboardInterrupt:
            console.log("User interruption detected (CTRL+C)")
        except Exception as e:
            console.log(f"An unknown error occurred: {e}")
