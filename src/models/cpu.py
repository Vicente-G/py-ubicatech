from sqlmodel import Field, Session, SQLModel, select


class CPU(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    brand: str
    cores: int
    threads: int
    base_clock: float  # in GHz
    boost_clock: float | None = None  # in GHz
    tdp: int  # in watts
    socket: str
    price: float  # in CLP
    architecture: str
    characteristics: str | None = None
    integrated_graphics: bool | None = None


# Create a new CPU
def create_cpu(session: Session, cpu: CPU) -> int:
    session.add(cpu)
    session.commit()
    session.refresh(cpu)
    return cpu.id


# Read a CPU by ID
def get_cpu_by_id(session: Session, cpu_id: int) -> CPU | None:
    statement = select(CPU).where(CPU.id == cpu_id)
    return session.exec(statement).first()


# Read all CPUs
def get_all_cpus(session: Session) -> list[CPU]:
    statement = select(CPU)
    return session.exec(statement).all()


# Update a CPU
def update_cpu(session: Session, cpu_id: int, updated_data: dict) -> CPU | None:
    cpu = get_cpu_by_id(session, cpu_id)
    if not cpu:
        return None
    for key, value in updated_data.items():
        setattr(cpu, key, value)
    session.add(cpu)
    session.commit()
    session.refresh(cpu)
    return cpu


# Delete a CPU
def delete_cpu(session: Session, cpu_id: int) -> bool:
    cpu = get_cpu_by_id(session, cpu_id)
    if not cpu:
        return False
    session.delete(cpu)
    session.commit()
    return True
