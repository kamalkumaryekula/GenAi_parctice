# Create a custom exception class
class InvalidAgeError(Exception):
    """Raised when the input age is not a valid age."""
    pass # We don't need any custom logic, just the name.

def register_user(name, age):
    if age < 0:
        # Raise our custom exception for a specific error condition
        raise InvalidAgeError("Age cannot be negative.")
    if age < 18:
        raise ValueError("User must be at least 18 to register.")
        
    print(f"User '{name}' registered with age {age}.")

# --- Main Program Logic ---
try:
    register_user("Alice", 25)
    register_user("Bob", -5) # This will raise our custom exception
    register_user("Charlie", 15)
except InvalidAgeError as e:
    print(f"[ERROR] Registration failed: {e}")
except ValueError as e:
    print(f"[ERROR] Validation failed: {e}")


# output:

# User 'Alice' registered with age 25.
# [ERROR] Registration failed: Age cannot be negative.








# Create a custom exception class
class InvalidAgeError(Exception):
    """Raised when the input age is not a valid age."""
    pass # We don't need any custom logic, just the name.

def register_user(name, age):
    if age < 0:
        # Raise our custom exception for a specific error condition
        raise InvalidAgeError("Age cannot be negative.")
    if age < 18:
        raise ValueError("User must be at least 18 to register.")
        
    print(f"User '{name}' registered with age {age}.")

# --- Main Program Logic ---

users = [("Alice", 25), ("Bob", -5), ("Charlie", 15)]

for name, age in users:
    try:
        register_user(name, age)
    except InvalidAgeError as e:
        print(f"[ERROR] Registration failed for {name}: {e}")
    except ValueError as e:
        print(f"[ERROR] Validation failed for {name}: {e}")


# output:

# User 'Alice' registered with age 25.
# [ERROR] Registration failed for Bob: Age cannot be negative.
# [ERROR] Validation failed for Charlie: User must be at least 18 to register.