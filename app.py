from flask import Flask, jsonify, Response, send_file, render_template
from flask_caching import Cache
from config import POKE_API_URL
from utils.data_fetch import fetch_all_berry_data
from utils.calculations import calculate_stats
import matplotlib.pyplot as plt
import io


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
@app.route("/berryHistogram", methods=['GET'])
def berry_histogram():
    """
    Route to fetch pokemon berries histogram
    """
    data = fetch_all_berry_data()
    growth_time = [berry['growth_time'] for berry in data]

    plt.figure(figsize=(10, 6))
    plt.hist(growth_time, bins =range(min(growth_time), max(growth_time) + 1, 1), edcolor = 'black')
    plt.title('Histogram of Berry growth time')
    plt.xlabel('Growth time')
    plt.ylabel('Frequency')

    img_path = "static/images/berry_histogram.png"
    plt.savefig(img_path, format='png')
    plt.close()

    return send_file(img_path, mimetype='image/png')

@app.route("/showHistogram", methods=["GET"])
def show_histogram():
    """
    Route to show histogram of pokemon berries
    """
    return render_template("histogram.html")

if __name__ == '__main__':
    app.run(debug=True)
