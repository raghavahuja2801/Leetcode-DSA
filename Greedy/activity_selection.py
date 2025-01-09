def activity_selection(start, finish):
    """
    Select the maximum number of activities that don't overlap.
    
    Parameters:
        start (list[int]): List of start times for activities.
        finish (list[int]): List of finish times for activities.
    
    Returns:
        list[int]: Indices of the selected activities.
    """
    n = len(start)
    activities = list(range(n))

    # Sort activities by their finish times
    activities.sort(key=lambda x: finish[x])

    # Select activities
    selected_activities = []
    last_finish_time = -1

    for activity in activities:
        if start[activity] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = finish[activity]

    return selected_activities

# Example usage
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print("Selected activities:", activity_selection(start, finish))
