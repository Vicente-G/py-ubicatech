variable "components" {
  type = list(string)
  default = [
    "cpu",
  ]
}

locals {
  csv_data = [
    for component in var.components :
        split("\n", file("data/${component}.csv"))
  ]
}

data "template_dir" "migrations" {
  path = "migrations/atlas/revisions"
  vars = zipmap(var.components, local.csv_data)
}

env "local" {
    src = "file://migrations/atlas/data/schemas.sql"
    url = "postgresql://postgres:postgres@localhost:5432/ubicatech"
    dev = "postgresql://postgres:postgres@localhost:5432/ubicatech"
    migration {
        dir = data.template_dir.migrations.url
    }
}

env "tf" {
    migration {
        dir = data.template_dir.migrations.url
    }
}