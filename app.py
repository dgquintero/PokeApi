# initialize a basic flask application

from flask import Flask
from config import POKE_API_URL

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home route    
    """
    return f"Poke-berries Statistics API - POKEAPI_URL: {POKE_API_URL}"

if __name__ == '__main__':
    app.run(debug=True)
