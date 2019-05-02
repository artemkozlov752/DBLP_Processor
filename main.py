"""
Downloading and converting DBLP data to pandas DataFrame
Made by Artem Kozlov
~~~~~~~~~~~~
This module implements the DBLP downloading in gz format, parse, convert it to pandas DataFrame and save
a pdf histogram of the amount of the books per year.
Main data link:
http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/dblp/dblp.xml.gz.

copyright: (c) 2019 by Artem Kozlov.
"""


from util import get_config, logger_initializing, plot_and_save_hist
from parsers.ParseXMLData import ParseXMLData


PATH_TO_CONFIG = "./configs/config.yaml"
CONFIG = get_config(PATH_TO_CONFIG)
DBLP_ZIP_URL = CONFIG["zip_url"]
DBLP = CONFIG["xml_path"]
PICTURE_SAVE = CONFIG["picture_save_path"]


def main():
    logger_initializing(CONFIG["path_to_logger"])
    parser = ParseXMLData(DBLP_ZIP_URL, DBLP, CONFIG["pandas_columns"])
    parser.download_data()
    parser.convert_list()
    records_grouped_by_year = parser.records[["title", "year"]].groupby(["year"])
    plot_and_save_hist(records_grouped_by_year, PICTURE_SAVE)


if __name__ == "__main__":
    main()
