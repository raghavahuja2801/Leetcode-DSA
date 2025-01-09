def set_cover(universe, sets):
    """
    Find a minimum set cover for the given universe using a greedy approach.
    
    Parameters:
        universe (set): The set of all elements to be covered.
        sets (list[set]): A list of sets that can cover the elements.
    
    Returns:
        list: A list of sets that cover the universe.
    """
    covered = set()
    selected_sets = []

    while covered != universe:
        # Find the set that covers the most uncovered elements
        best_set = max(sets, key=lambda s: len(s - covered))
        selected_sets.append(best_set)
        covered |= best_set  # Add the elements of the chosen set to the covered set

    return selected_sets

# Example usage
universe = {1, 2, 3, 4, 5}
sets = [{1, 2, 3}, {2, 4}, {1, 4, 5}, {3, 5}]
print("Selected sets:", set_cover(universe, sets))
