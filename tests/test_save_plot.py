import pandas as pd
import pytest

from util import plot_and_save_hist


@pytest.fixture
def correct_dataframe():
    columns = {
        "title": ["Book_1", "Book_2", "Book_3", "Book_4", "Book_5", "Book_6"],
        "author": ["Author_1", "Author_2", -1, "Author_4", "Author_4", "Author_4, Author_5"],
        "year": ["1992", "1997", "1997", "1994", "1991", "1993"]
    }
    return pd.DataFrame(columns)


def test_save_plot(correct_dataframe):
    """Hand test, need to test locally"""
    records_grouped_by_year = correct_dataframe[["title", "year"]].groupby(["year"])
    plot_and_save_hist(records_grouped_by_year, "./pictures/amount_per_year.pdf")
