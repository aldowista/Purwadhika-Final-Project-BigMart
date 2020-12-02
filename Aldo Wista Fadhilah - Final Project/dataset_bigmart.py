import pandas as pd 
import numpy as np
import seaborn as sns

def data_awal():
    df = pd.read_csv('train_bigmart.csv')
    return df

def data_final():
    df = pd.read_csv('data_bigmart_final.csv')
    return df

def list_item_identifier():
    df = pd.read_csv('data_bigmart_final.csv')
    list_item_iden = list(df['Item_Identifier'].unique())
    return list_item_iden

def item_sales_avg(data):
    df = pd.read_csv('data_bigmart_final.csv')
    df_baru = df.groupby(['Item_Identifier']).mean()
    hasil = df_baru.loc[data]['Item_Sales_AVG']
    return hasil

def outlet_sales_avg(data):
    df = pd.read_csv('data_bigmart_final.csv')
    df_baru = df.groupby(['Outlet_Identifier']).mean()
    hasil = df_baru.loc[data]['Outlet_Item_Sales_AVG']
    return hasil

def item_telaris():
    df=pd.read_csv('data_bigmart_final.csv')
    df_baru =df.groupby(['Item_Identifier']).mean()
    df_baru['Item_Identifier'] = df_baru.index
    hasil = df_baru[['Item_Identifier','Item_Weight', 'Item_MRP', 'Item_Sales_AVG']].sort_values(by=['Item_Sales_AVG'], ascending=False).head()
    return hasil

def item_pemasukan_terbesar():
    df=pd.read_csv('data_bigmart_final.csv')
    df_baru =df.groupby(['Item_Identifier']).sum()
    df_baru['Item_Identifier'] = df_baru.index
    hasil = df_baru[['Item_Identifier', 'Item_Outlet_Sales']].sort_values(by=['Item_Outlet_Sales'], ascending=False).head()
    return hasil

def lokasi_pendapatan_terbanyak():
    df=pd.read_csv('data_bigmart_final.csv')
    df_baru =df.groupby(['Outlet_Location_Type']).sum()
    df_baru['Outlet_Location_Type'] = df_baru.index
    hasil = df_baru[['Outlet_Location_Type', 'Item_Outlet_Sales']].sort_values(by=['Item_Outlet_Sales'], ascending=False).head()
    return hasil