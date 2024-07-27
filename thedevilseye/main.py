import bs4
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown

from .utils import console
from .version import Version


def get_page_source(url: str, session: requests.Session) -> bs4.BeautifulSoup:
    """
    Gets the HTML source of the specified URL.

    :param url: URL to get HTML source from.
    :type url: str
    :param session: A requests.Session to use for the request.
    :type session: requests.Session
    :return: The HTML source of the specified URL.
    :rtype: bs4.BeautifulSoup
    """
    response = make_request(url=url, session=session)
    html_content = BeautifulSoup(response.content, "html.parser")
    return html_content


def make_request(url: str, session: requests.Session) -> requests.Response:
    """
    Sends a GET request to the specified URL.

    :param url: URL to send request to.
    :type url: str
    :param session: A requests.Session to use for the request.
    :type session: requests.Session
    :return: Response from the specified URL.
    :rtype: requests.Response
    """
    response = session.get(url)
    return response


def check_updates(session: requests.Session):
    release = make_request(
        url="https://api.github.com/repos/rly0nheart/thedevilseye/releases/latest",
        session=session,
    ).json()

    if release.get("tag_name"):
        remote_version: str = release.get("tag_name")
        markup_release_notes: str = release.get("body")
        markdown_release_notes = Markdown(markup=markup_release_notes)

        # Splitting the version strings into components
        remote_parts: list = remote_version.split(".")

        update_level: str = ""

        # Check for differences in version parts
        if remote_parts[0] != Version.major:
            update_level = "MAJOR"

        elif remote_parts[1] != Version.minor:
            update_level = "MINOR"

        elif remote_parts[2] != Version.patch:
            update_level = "PATCH"

        if update_level:
            upgrade_instructions = Markdown(
                markup=f"""
## How To Upgrade
* **PyPI Package**: *`pip install --upgrade thedevilseye`*
"""
            )
            console.log(
                f"\n[bold]{update_level}[/] update available: [underline]{remote_version}[/]",
                justify="center",
            )
            console.log(markdown_release_notes)
            console.log(upgrade_instructions, "\n")


def get_hidden_services(query: str, status: Console.status, session: requests.Session):
    status.update(f"Searching for `{query} on Ahmia.fi...")
    response_content = get_page_source(
        f"https://ahmia.fi/search/?q={query}", session=session
    )
    results = response_content.find_all("li", {"class": "result"})
    status.update(f"Found {len(results)} results for `{query}`")
    results_list: list = []
    for index, result in enumerate(results, start=1):
        url = " ".join(result.find("cite").text.split())
        title = " ".join(result.find("h4").text.split())
        description = " ".join(result.find("p").text.split())
        results_list.append(
            {"title": title, "description": description, "onion_url": url}
        )

    return results_list
