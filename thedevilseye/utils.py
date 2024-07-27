import os
from typing import Literal

import pandas as pd
from rich.console import Console


def print_banner():
    """
    Prints the projects banner and system information.
    """
    console.print(
        f"""
┏┳┓┓┏┏┓┳┓┏┓┓┏┳┓ ┏┓┏┓┓┏┏┓
 ┃ ┣┫┣ ┃┃┣ ┃┃┃┃ ┗┓┣ ┗┫┣ 
 ┻ ┛┗┗┛┻┛┗┛┗┛┻┗┛┗┛┗┛┗┛┗┛"""
    )


def export_dataframe(
    dataframe: pd.DataFrame,
    filename: str,
    formats: list[Literal["csv", "html", "json", "xml"]],
):
    """
    Exports a Pandas dataframe to specified file formats.

    :param dataframe: Pandas dataframe to export.
    :type dataframe: pandas.DataFrame
    :param filename: Name of the file to which the dataframe will be exported.
    :type filename: str
    :param formats: A list of file formats to which the data will be exported.
    :type formats: list[Literal]
    """
    file_mapping: dict = {
        "csv": lambda: dataframe.to_csv(f"{filename}.csv", encoding="utf-8"),
        "html": lambda: dataframe.to_html(
            f"{filename}.html",
            escape=False,
            encoding="utf-8",
        ),
        "json": lambda: dataframe.to_json(
            f"{filename}.json",
            orient="records",
            lines=True,
            force_ascii=False,
            indent=4,
        ),
        "xml": lambda: dataframe.to_xml(
            f"{filename}.xml",
            parser="etree",
            encoding="utf-8",
        ),
    }

    for file_format in formats:
        if file_format in file_mapping:
            filepath: str = f"{filename}.{file_format}"
            file_mapping.get(file_format)()
            console.log(
                f"{os.path.getsize(filepath)} bytes written to [link file://{filepath}]{filepath}"
            )
        else:
            console.log(f"Unsupported file format: {file_format}")


console = Console(color_system="auto", log_time=False)
