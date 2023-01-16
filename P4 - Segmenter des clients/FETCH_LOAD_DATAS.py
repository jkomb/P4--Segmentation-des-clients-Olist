__doc__ = """Ce module contient la définition des variables de chemins de destination ainsi que l'importation des librairies nécessaires à la définition des 2 fonctions suivantes:
	- fetch_olist_data() : qui sert à télécharger dans un sous-dossier du dossier de travail, 'datasets', l'ensemble des jeux de données nécessaire à notre travail
	- load_olist_data() : qui sert à charger ce jeu de données dans un DataFrame
"""

import os
import urllib
import zipfile
import pandas as pd

DOWNLOAD_URL = "https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/download?datasetVersionNumber=2"
ZIP_NAME = "archive.zip"
DATA_PATH = "datasets/olist_database"
ZIP_PATH = os.path.join(DATA_PATH, ZIP_NAME)

def fetch_olist_data(data_path=DATA_PATH, dwnld_url=DOWNLOAD_URL, zip_path=ZIP_PATH):

    """fonction d'extraction des données depuis https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"""

    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    urllib.request.urlretrieve(dwnld_url, zip_path)

    with zipfile.ZipFile(zip_path, mode="r") as archive:
        archive.extractall(data_path)

    os.remove(zip_path)

def load_olist_data(data_path=DATA_PATH):

    """fonction de chargement des données extraites dans un dataframe"""
    dict_data = dict()
    List_data_names = list()
    for _, _, files in os.walk(data_path):
        for filename in files:
            file_path = os.path.join(DATA_PATH, filename)
            file_short = filename.split('.')[0]
            df_tmp = pd.read_csv(file_path)
            df_tmp.index.name = file_short
            dict_data[file_short] = df_tmp
            List_data_names.append(file_short)

    return dict_data, List_data_names