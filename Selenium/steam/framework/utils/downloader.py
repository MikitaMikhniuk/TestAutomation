import os
import time

CONFIG_PATH = "Selenium\\steam\\framework\\resources\\factory_config.json"


def set_up_download_folder(factory_config):
    """
    Method is used to create a folder for the current test run.

    Input (parsed json) -> factory config

    Returns (str) -> download path
    """
    os.chdir(factory_config["DEFAULT_DOWNLOAD_PATH"])
    folder_name = factory_config["BROWSER"] + "_" + 'test_run_' + time.strftime("%d.%m.%Y^%H_%M_%S")
    os.mkdir(folder_name)
    os.chdir(folder_name)
    print(
        f"Files will be downloaded to {factory_config['DEFAULT_DOWNLOAD_PATH']} > {folder_name}")
    default_download_path = os.getcwd()
    return default_download_path


def wait_for_download_finish(file_name, wait_sec= 10):
    """
    Method is used to wait for a specific file to be found in current folder.

    Input -> Full file name (str). e.g. "SteamSetup.exe"
    """
    i = 0
    while i < wait_sec:
        if file_name in os.getcwd():
            break
        else:
            time.sleep(1)
            i += 1
    if i > wait_sec:
        raise Exception(f"Time is ticking! Unable to download file {file_name}!")
