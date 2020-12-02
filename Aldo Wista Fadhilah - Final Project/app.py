from flask import Flask, render_template, request, url_for, redirect
from data_py import item_fat_content, item_type, outlet_identifier, outlet_location_type, outlet_type
from dataset_bigmart import data_awal, list_item_identifier, item_sales_avg, outlet_sales_avg, data_final, item_telaris, item_pemasukan_terbesar, lokasi_pendapatan_terbanyak
from prediction import prediction_data

#initialize
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_predicition():
    item = list_item_identifier()
    if request.method == 'POST':
        data = request.form ## immutablemultidict
        data = data.to_dict()
        data['Item_Identifier'] = item_sales_avg(data['Item_Identifier'])
        data['Outlet_Identifier'] = outlet_sales_avg(data['Outlet_Identifier'])
        data['Item_MRP'] = float(data['Item_MRP'])
        hasil = prediction_data(data)
        return render_template('result.html',hasil_prediction=hasil)
    return render_template('home.html', data_location_type=sorted(outlet_location_type),
    data_item_fat=sorted(item_fat_content), data_item_type=sorted(item_type), 
    data_outlet_identifier=sorted(outlet_identifier), data_outlet_type=sorted(outlet_type),
    data_item_identifier=sorted(item)
    )

@app.route('/bigmart', methods=['GET', 'POST'])
def data():
    data = data_awal()
    return render_template('data_bigmart.html',data=data)

@app.route('/data_rating')
def data_rating():
    data_lokasi_pendapatan_terbanyak = lokasi_pendapatan_terbanyak()
    data_item_pemasukan_terbesar = item_pemasukan_terbesar()
    data_item_terlaris = item_telaris()
    return render_template('data_rating.html', data_item_terlaris = data_item_terlaris, item_pemasukan_terbesar=data_item_pemasukan_terbesar,
    data_lokasi_pendapatan_terbanyak = data_lokasi_pendapatan_terbanyak)

@app.route('/fe', methods=['GET', 'POST'])
def fe():
    data = data_final()
    return render_template('feature_engineering.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')
  
if __name__ == '__main__':
    app.run(debug=True,port=3333)