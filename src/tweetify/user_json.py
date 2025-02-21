import json

def get_user_from_json(filepath, username_to_find):  # Add username parameter
    """Reads a JSON file and returns the user dictionary matching the given username."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

            # Check if the username exists as a key and return the corresponding data
            if username_to_find in data:
                return data[username_to_find]  # Return the corresponding value
            else:
                return None  # Or raise an exception if you prefer


    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'")
        return None


if __name__ == "__main__":
    filepath = "../users.json"
    username_to_search = "SadhguruJV"  # Example: Search for SadhguruJV
    user = get_user_from_json(filepath, username_to_search)

    if user:
        print(user['id'])
    else:
        print(f"User '{username_to_search}' not found in JSON.")