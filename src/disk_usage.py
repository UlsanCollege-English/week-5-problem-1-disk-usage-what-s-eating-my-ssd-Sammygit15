def total_size(node):
    """
    Compute total size of a nested file/dir tree.

    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}

    Returns:
        int: total size of all files within the node (recursively).
    """
    # Guard: handle invalid or missing input
    if not isinstance(node, dict):
        return 0

    node_type = node.get("type")

    # Base case: file node
    if node_type == "file":
        # Return size, defaulting to 0 if missing or malformed
        return node.get("size", 0) or 0

    # Recursive case: directory node
    if node_type == "dir":
        children = node.get("children", [])
        # Sum total_size for each child node
        return sum(total_size(child) for child in children)

    # Unknown type or malformed entry — ignore
    return 0
