from bs4 import BeautifulSoup
import gzip
import logging
import pandas as pd
import urllib.request

from util import create_directory_if_not_exists


class ParseXMLData:
    """Download xml data and parse it to pandas DataFrame."""

    def __init__(self, url: str, file_path: str, pandas_columns: list):
        """Initialize downloaded url, file_path for saving data, records_list (list) and records (pd.DataFrame).

        Args:
            url (str): url for data downloading.

        """
        self.logger = logging.getLogger(__name__)
        self.url = url
        self.file_path = file_path
        self.columns = pandas_columns
        self.records = None

    def convert_list(self):
        """Main downloader and parser of xml file."""
        self.logger.info("load gz file content")
        file_content = self._read_gz_file()
        self.logger.info("get records list from loaded gz file content")
        records_list = self._get_records(file_content)
        self.logger.info("convert records list to pandas DataFrame")
        self.records = self._from_list_to_dataframe(records_list)

    def download_data(self) -> None:
        """Download zip dblp from self.url"""
        create_directory_if_not_exists(self.file_path)
        self.logger.info("download dblp data in gz format")
        try:
            urllib.request.urlretrieve(self.url, self.file_path)
        except Exception as e:
            error_message = f"Cannot download data from {self.url}"
            self.logger.critical(error_message)

    def _read_gz_file(self) -> str:
        """Read file from gz format and return its string content."""
        with gzip.open(self.file_path, 'rb') as gzip_file:
            file_content = gzip_file.read().decode('ascii')
        return file_content

    @staticmethod
    def _get_records(file_content: str):
        """Get records from string file_content.

        Args:
            file_content (str).

        Returns:
            (list): list with records.

        """
        file_content_without_newline = file_content.replace('\n', '')
        soup = BeautifulSoup(file_content_without_newline, features="lxml")
        return soup.find_all(lambda tag: tag.has_attr('key'))

    def _from_list_to_dataframe(self, records_list: list) -> pd.DataFrame:
        """Create pandas DataFrame with information about each book.

        Args:
            records_list (list): list with records about each book.

        Returns:
            (pd.DataFrame).

        """
        records_dataframe = pd.DataFrame(index=range(len(records_list)), columns=self.columns)
        for index, record in enumerate(records_list):
            children = record.children
            for child in children:
                raw_data = record.find_all(child.name)
                data = list(map(lambda element: element.contents[0], raw_data))
                if len(data) == 1:
                    data = data[0]
                else:
                    data = ", ".join(data)
                records_dataframe.iloc[index][child.name] = str(data)
        return records_dataframe
