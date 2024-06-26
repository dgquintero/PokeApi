# Poke-Berries Statistics API


## Description

This project is a Poke-Berries Statistics API that fetches data from the PokeAPI and computes various statistics about berry growth times. The API provides endpoints `/allBerryStats` which returns the names of all berries along with statistical data about their growth times and includes an endpoint to view a histogram of berry growth times `/showHistogram`.

## Deployed Services

The application is deployed and can be accessed through the following URLs:

- [Home](https://dgquintero.pythonanywhere.com/)
- [Berry Statistics](https://dgquintero.pythonanywhere.com/allBerryStats)
- [Berry Growth Time Histogram](https://dgquintero.pythonanywhere.com/showHistogram)

## Features

- Fetches data from the PokeAPI to get berry details.
- Computes various statistics such as minimum, maximum, mean, median, variance, and frequency of berry growth times.
- Caches the data for 2 minutes to improve performance.
- Includes content-type header (application/json) in the response.
- Functions are tested using `pytest`.

## Endpoints

### GET /allBerryStats

#### Response
```json
{
    "berries_names": [...],
    "min_growth_time": "", // time, int
    "median_growth_time": "", // time, float
    "max_growth_time": "", // time, int
    "variance_growth_time": "", // time, float
    "mean_growth_time": "", // time, float
    "frequency_growth_time": "" // time, {growth_time: frequency, ...}
}
````

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the project directory:
    ```bash
    cd pokeapi
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    ```bash
    # On macOS/Linux
    source venv/bin/activate

    # On Windows
    .\venv\Scripts\activate
    ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server:
    ```bash
    python app.py
    ```

2. Access the API in your browser or using a tool like `curl` or `Postman`:
    ```bash
    http://127.0.0.1:5000/allBerryStats
    ```

3. View the histogram image directly:
    ```bash
    http://127.0.0.1:8000/berryHistogram
    ```

4. View the HTML page displaying the histogram:
    ```bash
    http://127.0.0.1:8000/showHistogram
    ```

## Running with Docker

1. Build the Docker image:
    ```bash
    docker-compose build
    ```

2. Run the Docker container:
    ```bash
    docker-compose up
    ```

3. Access the API:
    ```bash
    http://127.0.0.1:8000/allBerryStats
    ```

4. View the histogram image directly:
    ```bash
    http://127.0.0.1:8000/berryHistogram
    ```

5. View the HTML page displaying the histogram:
    ```bash
    http://127.0.0.1:8000/showHistogram
    ```


## Testing

To run the tests, use `pytest`:
```bash
pytest

