import json


def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: invalid JSON format.")
        return []


def validate_user(user):
    if "@" not in user.get("email", ""):
        return False
    if user.get("age", -1) < 0:
        return False
    if user.get("logins", -1) < 0:
        return False
    return True


def get_valid_users(users):
    return [user for user in users if validate_user(user)]

def get_active_users(users):
    return [user for user in users if user.get("is_active") is True]


def get_adult_users(users):
    return [user for user in users if user.get("age", 0) >= 18]

def calculate_average_age(users):
    if not users:
        return 0
    total_age = sum(user["age"] for user in users)
    return total_age / len(users)


def calculate_total_logins(users):
    return sum(user["logins"] for user in users)


def get_user_with_most_logins(users):
    if not users:
        return None
    return max(users, key=lambda user: user["logins"])

def print_report(users):
    active_users = get_active_users(users)
    adult_users = get_adult_users(users)

    average_age = calculate_average_age(users)
    total_logins = calculate_total_logins(users)
    top_user = get_user_with_most_logins(users)

    print("=== USER REPORT ===")
    print(f"Total users: {len(users)}")
    print(f"Active users: {len(active_users)}")
    print(f"Adult users: {len(adult_users)}")
    print(f"Average age: {average_age:.2f}")
    print(f"Total logins: {total_logins}")

    if top_user:
        print(f"Top user by logins: {top_user['name']} ({top_user['logins']} logins)")





# --- main part ---
users = load_users()
valid_users = get_valid_users(users)

print_report(valid_users)
