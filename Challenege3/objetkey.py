def get_value_from_nested_object(obj, key):
    keys = key.split('/')  # Split the key into individual keys
    current_obj = obj

    try:
        # Traverse through the nested object
        for k in keys:
            current_obj = current_obj[k]
        
        return current_obj
    except (KeyError, TypeError):
        return None

# Example usage:
obj1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
print(get_value_from_nested_object(obj1, key1))  # Output: d

obj2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
print(get_value_from_nested_object(obj2, key2))  # Output: a
