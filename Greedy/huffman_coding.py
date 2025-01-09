import heapq

def huffman_coding(symbols, frequencies):
    """
    Create a Huffman tree for encoding a set of symbols based on their frequencies.
    
    Parameters:
        symbols (list[str]): List of symbols (e.g., characters).
        frequencies (list[int]): List of frequencies corresponding to the symbols.
    
    Returns:
        dict: A dictionary with symbols as keys and their Huffman codes as values.
    """
    # Create a priority queue (min heap)
    heap = [[weight, [symbol, ""]] for symbol, weight in zip(symbols, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return dict(sorted(heap[0][1:], key=lambda p: p[0]))

# Example usage
symbols = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]
codes = huffman_coding(symbols, frequencies)
print("Huffman Codes:", codes)
