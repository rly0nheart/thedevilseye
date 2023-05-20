import requests
from bs4 import BeautifulSoup
from rich import print as xprint
from thedevilseye.config import COLOURS
from thedevilseye.config import Markdown, arguments, current_version, create_results_table, create_parser


def __get_page_resource(url: str):
    """
    Get the resource html of https://ahmia.fi
    :param url: ahmia.fi url (https://ahmia.fi/search/?q=some_query_here)
    :return: html string of the page
    """
    response = requests.get(url)
    html_content = BeautifulSoup(response.content, "html.parser")
    return html_content


# Check program updates
def check_updates():
    response = requests.get("https://api.github.com/repos/rly0nheart/thedevilseye/releases/latest").json()
    if response['tag_name'] == current_version:
        pass
    else:
        raw_release_notes = response['body']
        markdown_release_notes = Markdown(raw_release_notes)
        xprint(f"{COLOURS['GREEN']}[UPDATE]{COLOURS['RESET']} A new release of thedevilseye is available ({response['tag_name']}).\n")
        xprint(markdown_release_notes)


def get_hidden_services(query: str, result_count: int):
    """
    Get search results from Ahmia.fi
    :param query: query string
    :param result_count: number of results to return
    :return: None
    """
    response_content = __get_page_resource(f"https://ahmia.fi/search/?q={query}")
    results = response_content.find_all('li', {'class': 'result'})
    results_table = create_results_table()
    for index, result in enumerate(results, start=1):
        url = result.find('cite').text
        title = result.find('h4').text
        description = result.find('p').text
        results_table.add_row(str(index),
                              title,
                              COLOURS['BLUE'] + url + COLOURS['RESET'],
                              COLOURS['GREEN'] + description + COLOURS['RESET'])

        if index == result_count:
            break

    xprint(results_table)
