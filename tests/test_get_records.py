import pandas as pd
import pytest

from parsers.ParseXMLData import ParseXMLData


@pytest.fixture
def pandas_columns():
    return ["title", "author", "year"]


@pytest.fixture
def correct_dataframe():
    columns = {
        "title": ["Book_1", "Book_2", "Book_3", "Book_4", "Book_5", "Book_6"],
        "author": ["Author_1", "Author_2", -1, "Author_4", "Author_4", "Author_4, Author_5"],
        "year": ["1992", "1997", "1997", "1994", "1991", "1993"]
    }
    return pd.DataFrame(columns)


def test_download_data(pandas_columns, correct_dataframe):
    parser = ParseXMLData("dblp_test_data.xml.gz", "tests/xml_data/dblp_test_data.xml.gz", pandas_columns)
    parser.convert_list()
    parser.records.fillna(-1, inplace=True)
    for column in parser.records.columns:
        for element, correct_element in zip(parser.records[column], correct_dataframe[column]):
            assert element == correct_element, f"Value {element} is not equal to {correct_element}"
