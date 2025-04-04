import os

def generate_migration_from(data, output_folder, table_name):
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, f"01_{table_name}_insert.sql")

    if not data:
        print("No data to insert.")
        return

    columns = data[0].keys()
    inserts = [f"({', '.join(f'NULL' if v is None else f'\'{v}\'' for v in row.values())})" for row in data]

    with open(output_file, 'w', encoding='utf-8') as sql_file:
        sql_file.write(f"DO $$ BEGIN\n")
        sql_file.write(f"    INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n    " + ",\n    ".join(inserts) + "\n")
        sql_file.write("    ON CONFLICT DO NOTHING;\nEND $$;\n")

    print(f"Archivo SQL generado: {output_file}")

# Ejemplo de uso
#data = [
#    {"id": 2, "name": "Mouse", "price": 25.99, "stock": 50},
#    {"id": 3, "name": "Teclado", "price": 45.0, "stock": 30}
# {"id": 1, "name": "Laptop", "price": 800.5, "stock": 10},
#
#]
# generate_plpgsql_insert(data, "output", "cpu")
