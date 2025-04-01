import json


# TODO: Generate the chosen migration files from the json object
def generate_migration_from(json_object):
    with open("temp.json", "w") as file:
        file.write(json.dumps(json_object))
