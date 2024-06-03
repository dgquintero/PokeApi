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

    plt.figure(figsize=(12, 7))
    plt.hist(growth_time, bins =range(min(growth_time), max(growth_time) + 1, 1), edgecolor = 'black')
    plt.title('Histogram of Berry growth times', fontsize=16)
    plt.xlabel('Growth time (Hours)', fontsize=14)
    plt.ylabel('Frequency (Number of plants)', fontsize=14)

    counts, bins, patches = plt.hist(growth_time, bins=range(min(growth_time), max(growth_time) + 1, 1), edgecolor='black')
    for count, patch in zip(counts, patches):
        plt.text(patch.get_x() + patch.get_width() / 2, count, int(count), ha='center', va='bottom', fontsize=12)

    plt.xticks(range(min(growth_time), max(growth_time) + 1))
    plt.grid(axis='y', alpha=0.75)

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
