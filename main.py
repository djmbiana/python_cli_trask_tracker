import json
import os
import click

@click.group()
def taskie():
    pass


if os.path.exists("tasks.json"):
    with open("tasks.json", mode="r") as json_file:
        tasks = json.load(json_file)
else:
    tasks = []





@taskie.command()
@click.argument("description")
def add(description):
    if tasks:
        max_id = max(task['id'] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1

    user_task = {
        "id": new_id,
        "description": description,
        "status": "todo"
    }

    tasks.append(user_task)

    try:
        with open("tasks.json", mode="w") as json_file:
            json.dump(tasks, json_file, indent=4)
    except IOError as e:
        print("didnt work :()")


    
if __name__ == "__main__":
    taskie()