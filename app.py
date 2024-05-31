# initialize a basic flask application

from flask import Flask
from config import POKE_API_URL
from utils.data_fetch import fetch_poke_berry_data

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home route    
    """
    return f"Poke-berries Statistics API - POKEAPI_URL: {POKE_API_URL}"

@app.route('/poke-berries', methods=['GET'])
def poke_berries():
    """
    Route to fetch pokemon berries data
    """
    data = fetch_poke_berry_data()
    return data

if __name__ == '__main__':
    app.run(debug=True)
