import pickle
import pandas as pd

model = pickle.load(open('finalized_model_bigmart.sav','rb'))
one_hot_columns = pickle.load(open('x_dummies_colomn_bigmart.sav','rb'))

def prediction_data(data):
    df = pd.DataFrame(data,index=[0])
    df = pd.get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value = 0)
    hasil = model.predict(df)
    return round(hasil[0])

