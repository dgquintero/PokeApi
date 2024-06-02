# initialize a basic flask application

from flask import Flask, jsonify, Response
from flask_caching import Cache
from config import POKE_API_URL
from utils.data_fetch import fetch_all_berry_data
from utils.calculations import calculate_stats


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 120})

@app.route('/')
def home():
    """
    Home route    
    """
    return f"Poke-berries Statistics API - POKEAPI_URL: {POKE_API_URL}"

@app.route('/allBerryStats', methods=['GET'])
@cache.cached(timeout=120)
def all_berry_stats():
    """
    Route to fetch pokemon berries data
    """
    data = fetch_all_berry_data()
    if data:
        stats = calculate_stats(data)
        if stats:
            return Response(
                response = jsonify(stats).get_data(),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response = jsonify({"error": "Error calculating statistics"}).get_data(),
                status=500,
                mimetype="application/json"
            )
    else:
        return Response(
                response = jsonify({"error": "Failed to fetch data"}).get_data(),
                status=500,
                mimetype="application/json"
            )

if __name__ == '__main__':
    app.run(debug=True)
