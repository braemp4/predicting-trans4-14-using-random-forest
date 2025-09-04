import requests
import numpy as np
import pandas as pd 



def get_gene_name(id):
    url = f"https://rest.ensembl.org/lookup/id/{id}"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        data = response.json() #put request in json format
        return data.get("display_name", "X")
    else:
        return None 

class GeneScraper():
    def __init__(self, ids):
        self.base_url = "https://rest.ensembl.org/lookup/id/"
        self.ids = ids
    def get_gene_names(self):
        gene_names = []
        for id in self.ids:
            url = self.base_url + id
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers= headers)

            if response.status_code == 200:
                data = response.json()
                gene_names.append(data.get("display_name", "X"))
            else:
                print(f"response failed for gene id{id}")

        return gene_names 
    

    def map_dataframe(self, df):
        '''
        Adds gene names as a column based on self.ids
        ensure self.ids is in the same order as the genes in your dataframe
        '''
        gene_names = self.get_gene_names()
        df["gene_names"] = gene_names

        return df 


        
