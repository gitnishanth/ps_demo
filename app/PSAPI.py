import json
import requests

from flask import Flask

app = Flask(__name__)

healthStatus={
 'status':'200'
}

json_file_path='data.json'
country_code_data=None
api_status=None
#0 is for reading data from json file and 1 is to read data from API
api_call=0

def generate_data():
    if api_call:
        api_data=requests.get('https://www.travel-advisory.info/api')
        json_data=api_data.json()
    else:
        with open(json_file_path) as file_path:
            json_data = json.load(file_path)
    global country_code_data
    global api_status
    country_code_data = json_data['data']
    api_status = json_data['api_status']


@app.route('/')
def hello_world():
    return 'Hi Manager, use / health and /diag for !'


@app.route("/health")
def health_status():
    if api_status is None:
        generate_data()
    return healthStatus

@app.route("/diag")
def api_diag():
    if api_status is None:
        generate_data()

    data={'api_status':api_status}
    return data

@app.route("/convert/<country_code>")
def convert(country_code):
    if api_status is None:
        generate_data()
    
    country_code_list = country_code.split(",")

    data=[]
    for cc in country_code_list:
        try:
            data.append({cc:country_code_data[cc]['name']})
        except:
            data.append({cc:'country code doesnt exists'})
    
    output={'data':data}
    
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
