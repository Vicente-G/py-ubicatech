BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 71c59bb1f132

CREATE TABLE cpu (
    id SERIAL NOT NULL,
    name VARCHAR NOT NULL,
    brand VARCHAR NOT NULL,
    image VARCHAR NOT NULL,
    price_usd FLOAT NOT NULL,
    price_clp FLOAT NOT NULL,
    solotodo_link VARCHAR NOT NULL,
    cores INTEGER NOT NULL,
    threads INTEGER NOT NULL,
    base_clock INTEGER NOT NULL,
    boost_clock INTEGER NOT NULL,
    tdp INTEGER NOT NULL,
    socket VARCHAR NOT NULL,
    architecture VARCHAR NOT NULL,
    integrated_graphics VARCHAR NOT NULL,
    cpu_cooler VARCHAR NOT NULL,
    benchmark_single_core INTEGER NOT NULL,
    benchmark_multi_core INTEGER NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('71c59bb1f132') RETURNING alembic_version.version_num;

COMMIT;
