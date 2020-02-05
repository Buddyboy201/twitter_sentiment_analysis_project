import pandas as pd
import numpy as np


def get_senator_party_data(sen_df):
    sen_party = {}
    for i in range(len(sen_df)):
        a = sen_df.iloc[i]
        sen_party[a[0]] = a[3]
    return sen_party

def get_representative_party_data(rep_df):
    rep_party = {}
    for i in range(len(rep_df)):
        a = rep_df.iloc[i]
        rep_party[a[0]] = a[3]
    return rep_party

def get_politician_party_mapping(sen_data_file, rep_data_file):
    sen_df = pd.read_excel(sen_data_file)
    rep_df = pd.read_excel(rep_data_file)
    pol_party = {}
    pol_party.update(get_senator_party_data(sen_df))
    pol_party.update(get_representative_party_data(rep_df))
    return pol_party

#sen_file = "senators_data.xlsx"
#rep_file = "representatives_data.xlsx"

#pol_party = get_politician_party_mapping(sen_file, rep_file)
#print(pol_party)
