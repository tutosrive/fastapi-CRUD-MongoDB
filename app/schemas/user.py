from app.models.user import User

def user_entity(item: dict) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'age': item['age'],
        'email': item['email'],
    }

def users_entity(items: list[User]) -> list[dict]:
    return [user_entity(item) for item in items]