# testing functions
from utils.data_fetch import fetch_berry_details
from utils.calculations import calculate_stats
from unittest.mock import patch, MagicMock
import pytest

@pytest.fixture
def berry_data():
    return [
        {
            "name": "cheri",
            "growth_time": 3
        },
        {
            "name": "chesto",
            "growth_time": 4
        },
        {
            "name": "pecha",
            "growth_time": 5
        }
    ]

def test_calculate_stats(berry_data):
    stats = calculate_stats(berry_data)
    assert stats["berries_names"] == ["cheri", "chesto", "pecha"]
    assert stats["min_growth_time"] == 3
    assert stats["median_growth_time"] == 4
    assert stats["max_growth_time"] == 5
    assert stats["variance_growth_time"] == 0.6666666666666666
    assert stats["mean_grow_time"] == 4.0
    assert stats["frequency_growth_time"] == {3: 1, 4: 1, 5: 1}

@patch('utils.data_fetch.requests.get')
def test_fetch_berry_details(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "name": "cheri",
        "growth_time": 3
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_berry_details(1)
    assert result == {"name": "cheri", "growth_time": 3}

