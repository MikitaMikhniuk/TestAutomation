import os
import shutil
import json

CONFIG_PATH = "Selenium\\steam\\framework\\factory_config.json"

def downlaod_file(download_element):
    config_file = open(CONFIG_PATH)
    factory_config = json.load(config_file)
    download_path = factory_config["DEFAULT_DOWNLOAD_PATH"]
    os.chdir(download_path)
    if os.path.isdir("downloads"):
        try:
            shutil.rmtree(os.getcwd(),ignore_errors=True)
            print("'downloads' is already exsist! Deleting it...")
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    else:
        os.mkdir("downloads")
        print(f"Folder for the test downloads is created at '{download_path}'")
    
# юзать время и дату в названии папки, чтобы не удалать всю целиком

downlaod_file()