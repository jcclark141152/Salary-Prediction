import os
import settings
import pandas as pd 

def concatenate():
    files = os.listdir(settings.DATA_DIR)
    full_df = []

    for f in files:
        data = pd.read_csv(os.path.join(settings.DATA_DIR, f)).set_index('Unnamed: 0')
        data['Role'] = os.path.basename(f).split('.')[0].replace('_',' ').title()
        full_df.append(data)

    full_df = pd.concat(full_df)
    full_df.index.name = None
    full_df.reset_index(drop = True)
    full_df.to_csv(os.path.join(settings.PROCESSED_DIR, 'data.csv'))

if __name__ == "__main__":
    concatenate()