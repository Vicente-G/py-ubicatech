# TODO: Write a pipeline to migrate the schemas and the data right after
data "external_schema" "sqlalchemy" {
    program = [
        "atlas-provider-sqlalchemy",
        "--path", "./models", // replace with the path to your SQLAlchemy models
        "--dialect", "postgresql"
    ]
}

env "local" {
    src = data.external_schema.sqlalchemy.url
    dev = "postgres://usuario:contraseña@localhost:5432/nombre_de_tu_bd?search_path=public"
    migration {
        dir = "file://migrations"
    }
}
