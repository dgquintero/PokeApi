import numpy as np


def calculate_stats(berries):
    """
    Calculate statistics for pokemon berries
    """
    try:
        berries_name = [berry['name'] for berry in berries]
        growth_times = [berry['growth_time'] for berry in berries]
        min_growth_time = int(np.min(growth_times))
        median_growth_time = float(np.median(growth_times))
        max_growth_time = int(np.max(growth_times))
        variance_growth_time = float(np.var(growth_times))
        mean_grow_time = float(np.mean(growth_times))

        frequency_growth_time = {}
        for time in growth_times:
            if time in frequency_growth_time:
                frequency_growth_time[time] += 1
            else:
                frequency_growth_time[time] = 1
        
        return {
            "berries_names": berries_name,
            "min_growth_time": min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_grow_time": mean_grow_time,
            "frequency_growth_time": frequency_growth_time
        }
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
