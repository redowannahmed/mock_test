def chunk_list(items, size):
    """Split a list into chunks."""
    if size <= 0:
        raise ValueError("size must be positive")

    return [
        items[index:index + size]
        for index in range(0, len(items), size)
    ]


def safe_get(dictionary, key, default=None):
    """Get a value from a dictionary safely."""
    return dictionary.get(key, default)