def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            return "Access Denied"
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_user(user, user_id):
    return f"User {user_id} deleted by {user['name']}"

admin = {"name": "Alice", "role": "admin"}
guest = {"name": "Bob", "role": "guest"}

print(delete_user(admin, 42))
print(delete_user(guest, 42))
