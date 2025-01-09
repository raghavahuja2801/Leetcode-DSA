def minimum_platforms(arrivals, departures):
    """
    Find the minimum number of platforms required for all trains to arrive and depart.
    
    Parameters:
        arrivals (list[int]): The arrival times of the trains.
        departures (list[int]): The departure times of the trains.
    
    Returns:
        int: The minimum number of platforms required.
    """
    arrivals.sort()  # Sort arrival and departure times
    departures.sort()

    platforms_needed = 0
    max_platforms = 0
    i = j = 0

    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        
        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms

# Example usage
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum platforms required:", minimum_platforms(arrivals, departures))
