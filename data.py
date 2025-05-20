headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Jhon",
    "phone": "+14234567890",
    "address": "123 Elm Street, Hilltop"
}

def get_user_body(first_name):
    return {
        "first_Name": first_name,
        "last_Name": "TestLast",
        "email": "test@example.com"
    }
