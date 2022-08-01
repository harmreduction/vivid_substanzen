## update the json file from the Google sheets file

import pandas as pd
import json

substance_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQM9INa12gkmzYivUzD4AqBpsYllL7Skehz6DdlqKWqVu3rPbYOA4IyFBo3q8IdswJNoUW7CmNLdZHs/pub?gid=1734089&single=true&output=tsv"
substances_db = pd.read_csv(substance_sheet, sep="\t", index_col="Substanz")

substance_dic = substances_db.to_dict("index")

## set columns to be joined in a dataframe
dose_oral = ['Dosierung Oral Leichte Dosis', 'Dosierung Oral Mittlere Dosis', 'Dosierung Oral Hohe Dosis', ]
wirkdauer_oral = ['Wirkdauer Oral Wirkungseintritt', 'Wirkdauer Oral Peak',
                  'Wirkdauer Oral Wirkdauer']
dose_nasal = ['Dosierung Nasal Leichte Dosis',
              'Dosierung Nasal Mittlere Dosis', 'Dosierung Nasal Hohe Dosis']
wirkdauer_nasal = ['Wirkdauer Nasal Wirkungseintritt', 'Wirkdauer Nasal Peak',
                   'Wirkdauer Nasal Wirkdauer']

subs_dict = {}
for subst, y in substances_db.iterrows():
    subs_dict[subst] = y.to_dict()

    #     Dose dataframe
    dose_dfor = pd.DataFrame.from_dict(y[dose_oral]).rename(columns={subst: 'Oral'})
    dose_dfor.index = dose_dfor.index.str.replace('Dosierung Oral ', '')
    dose_dfnas = pd.DataFrame.from_dict(y[dose_nasal]).rename(columns={subst: 'Nasal'})
    dose_dfnas.index = dose_dfnas.index.str.replace('Dosierung Nasal ', '')

    dose_df = dose_dfor.join(dose_dfnas).dropna(axis='columns')

    #     Wirkdauer dataframe
    wirk_dfor = pd.DataFrame.from_dict(y[wirkdauer_oral]).rename(columns={subst: 'Oral'})
    wirk_dfor.index = wirk_dfor.index.str.replace('Wirkdauer Oral ', '')
    wirk_dfnas = pd.DataFrame.from_dict(y[wirkdauer_nasal]).rename(columns={subst: 'Nasal'})
    wirk_dfnas.index = wirk_dfnas.index.str.replace('Wirkdauer Nasal ', '')

    wirkd_df = wirk_dfor.join(wirk_dfnas).dropna(axis='columns')

    subs_dict[subst]["comment"] = y["Dosierung comment"]
    subs_dict[subst]["dose_dict"] = dose_df.to_dict()
    subs_dict[subst]["wirkdauer_dict"] = wirkd_df.to_dict()

with open('substances_updated.json', 'w') as f:
    json.dump(subs_dict, f, indent=4, sort_keys=True, ensure_ascii=False)
