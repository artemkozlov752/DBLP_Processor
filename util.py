import logging.config
import matplotlib.pyplot as plt
import os
import re
import yaml


def get_config(path_to_yaml_config: str):
    """Read configs from yaml.

    Args:
        path_to_yaml_config (str): path to config

    Returns:
        (dict).

    """
    with open(path_to_yaml_config, encoding='utf-8') as fin:
        config = yaml.safe_load(fin)
    return config


def logger_initializing(path_to_logger: str):
    """Initialize logger wrt to config.

    Args:
        path_to_logger (str): path to logger yaml config.

    """
    with open(path_to_logger, 'r') as stream:
        config = yaml.safe_load(stream)
    path_to_logs = config["handlers"]["info_file_handler"]["filename"]
    create_directory_if_not_exists(path_to_logs)
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info('logger has been initialized')


def create_directory_if_not_exists(path: str):
    """Check existence of the directory, where file should be downoloaded and create directory if it does not exist.

    Args:
        path (str): path to file

    """
    directory = re.findall("(\.\/.*)\/(.*)", path)[0][0]
    if not os.path.exists(directory):
        os.makedirs(directory)


def plot_and_save_hist(data_grouped, save_to_file_path):
    """Plot and save histogram of data_grouped per index of data_grouped

    Args:
        data_grouped.

    """
    create_directory_if_not_exists(save_to_file_path)
    plt.figure(figsize=(15, 7))
    data_grouped.count()["title"].plot(kind="bar")
    plt.title("Books per year")
    plt.savefig(save_to_file_path)
