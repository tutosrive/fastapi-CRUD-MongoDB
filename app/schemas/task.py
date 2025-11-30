def task_entity(item: dict) -> dict:
    return {
        'id': str(item['_id']),
        'title': item['title'],
        'description': item['description'],
        'completed': item['completed'],
        'created_by': item['created_by']
    }

def tasks_entity(items: list[dict]) -> list[dict]:
    return [task_entity(item) for item in items]

def task_update_entity(item: dict) -> dict:
    copy_dict = item.copy()
    for key in copy_dict.keys():
        if item[key] == None:
            del item[key]
    return item