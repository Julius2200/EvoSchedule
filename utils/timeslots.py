

def generate_periods(start_hour, stop_hour):
    periods = []
    for hour in range(start_hour, stop_hour):
        start = f"{hour :02d}:00"
        stop = f"{hour +1 :02d}:00"
        periods.append(f"{start} - {stop}")

    return periods