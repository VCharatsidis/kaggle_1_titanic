import pandas as pd

df = pd.read_csv('../Data/train.csv')


def process_df(df):
    df = drop_rows(df, 'Cabin')
    df['Cabin_1'] = df.Cabin.apply(lambda x: x.split('/')[0])
    df['Cabin_2'] = df.Cabin.apply(lambda x: x.split('/')[2])
    df = drop_rows(df, 'VIP')
    df = drop_rows(df, 'CryoSleep')
    df = df.drop(['PassengerId', 'Name', 'Cabin'], axis=1)
    df.CryoSleep = df.CryoSleep.apply(lambda x: int(x))
    df.VIP = df.VIP.apply(lambda x: int(x))
    df.HomePlanet = df.HomePlanet.fillna('Other')
    df_proccessed = pd.concat([df, pd.get_dummies(df[['HomePlanet', 'Destination', 'Cabin_1', 'Cabin_2']])], axis=1)
    df_proccessed = df_proccessed.drop(['HomePlanet', 'Destination', 'Cabin_1', 'Cabin_2'], axis=1)
    columns = ['HomePlanet_Earth', 'HomePlanet_Europa', 'HomePlanet_Mars',
       'HomePlanet_Other', 'Destination_55 Cancri e',
       'Destination_PSO J318.5-22', 'Destination_TRAPPIST-1e',
       'Cabin_1_A', 'Cabin_1_B', 'Cabin_1_C', 'Cabin_1_D', 'Cabin_1_E',
       'Cabin_1_F', 'Cabin_1_G', 'Cabin_1_T', 'Cabin_2_P', 'Cabin_2_S']
    for col in columns:
        df_proccessed[col] = df_proccessed[col].apply(lambda x: int(x))
    df_final = df_proccessed.dropna().reset_index(drop=True)
    return df_final


def drop_rows(df, column_name):
    ind = df[column_name].dropna().index
    df = df.iloc[ind].reset_index(drop=True)
    return df


df_final = process_df(df)
print(df_final.columns.values.shape)
print(df_final.columns)
print(df_final)