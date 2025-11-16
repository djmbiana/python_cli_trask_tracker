import json
import os
import click
import datetime

if os.path.exists("tasks.json"):
    with open("tasks.json", mode="r") as json_file:
        tasks = json.load(json_file)
else:
    tasks = []


@click.group()
def taskie():
    pass

# add tasks
@taskie.command()
@click.argument("description")
def add(description):
    if tasks:
        max_id = max(task["id"] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1

    time_created = datetime.datetime.now().replace(microsecond=0)
    time_updated = datetime.datetime.now().replace(microsecond=0)

    user_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "time_created": time_created,
        "time_updated": time_updated,
    }

    tasks.append(user_task)

    try:
        with open("tasks.json", mode="w") as json_file:
            json.dump(tasks, json_file, indent=4, default=str)
    finally:
        print("Task Added!")
        print(f"ID: {user_task['id']}")
        print(f"Description: {user_task['description']}")
        print(f"Status: {user_task['status']}")
        print(f"Created On: {user_task['time_created']}")

# update tasks
@taskie.command()
@click.argument("id", type=int)
@click.argument("description")
def update(id, description):
    time_updated = datetime.datetime.now().replace(microsecond=0)

    with open("tasks.json", mode="r") as json_record:
        data = json.load(json_record)
        for record in data:
            if record['id'] == id:
               record['description'] = description 
               record['time_updated'] = time_updated
            break
               
    try:
        with open("tasks.json", mode="w") as json_file:
            json.dump(data, json_file, indent=4, default=str)
    finally:
        print(f"Time Update: {time_updated}") 

@taskie.command()
@click.argument("id", type=int)
def delete(id):
    with open("tasks.json", mode="r") as json_record:
        data = json.load(json_record)
    

# view all tasks
@taskie.command()
def view():
        with open("tasks.json", mode="r") as json_file:
            data = json.load(json_file)
        for task in data:
            print(f"Task ID: {task['id']}")
            print(f"Task Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created On: {task['time_created']}")
            print(f"Updated On: {task['time_updated']}")
            print("=" * 30)


if __name__ == "__main__":
    taskie()