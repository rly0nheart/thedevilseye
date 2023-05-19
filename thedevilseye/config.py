import argparse
from rich.table import Table

# rich library colours
COLOURS = {
    "RED": "[red]",
    "GREEN": "[white]",
    "GREEN": "[green]",
    "BLUE": "[blue]",
    "YELLOW": "[yellow]",
    "RESET": "[reset]"
}


# create result table
def create_results_table():
    results_table = Table(show_header=True, header_style='bold white')
    results_table.add_column("#", style="dim")
    results_table.add_column("Title")
    results_table.add_column("URL")
    results_table.add_column("Description")
    return results_table


# create argparse
def create_parser():
    parser = argparse.ArgumentParser(description="thedevilseye — by Richard Mwewa | https://about.me/rly0nheart",
                                     epilog="thedevilseye is an osint tool that uses Ahmia.fi to get Tor hidden "
                                            "services and descriptions that match with the user's query.")
    parser.add_argument('query', help='search query')
    parser.add_argument('-c', '--count', help='number of results to return (default %(default)s)', default=10)
    parser.add_argument('-d', '--debug', help='enable debug mode', action='store_true')
    parser.add_argument("-o", "--output", metavar="path/to/file", help=argparse.SUPPRESS)
    return parser
