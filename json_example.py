import json

user_profile = {
    "userId": 101,
    "username": "py_guru",
    "isActive": True,
    "roles": ["admin", "editor"],
    "settings": {
        "theme": "dark",
        "notifications": None
    }
}

# --- Using dumps() to get a string ---
json_string = json.dumps(user_profile, indent=4)
print("--- JSON String ---")
print(json_string)

# --- Using dump() to write to a file ---
with open("profile.json", "w") as f:
    json.dump(user_profile, f, indent=4)

print("\nprofile.json has been created.")