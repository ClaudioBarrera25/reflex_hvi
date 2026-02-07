#%%
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

import os 

DATABASE_URL = "postgresql://postgres:xUDEGTHpSsamuJrEQqUMLLaAylQureTN@postgres.railway.internal:5432/railway"


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class TestTable(Base):
    __tablename__ = "test-table"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    raza = Column(String, nullable=False)

    def __repr__(self):
        return f"<TestTable id={self.id} nombre={self.nombre} raza={self.raza}>"



def insert_test(nombre: str, raza: str):
    session = SessionLocal()
    try:
        row = TestTable(nombre=nombre, raza=raza)
        session.add(row)
        session.commit()
        session.refresh(row)
        print(f"✅ Insert OK → id={row.id}")
    except Exception as e:
        session.rollback()
        print("❌ Error insertando:", e)
    finally:
        session.close()

        
def list_all():
    session = SessionLocal()
    try:
        rows = session.query(TestTable).all()
        print("📋 Registros:")
        for r in rows:
            print(r)
    finally:
        session.close()


if __name__ == "__main__":
    insert_test("Firulais", "Quiltro")
    insert_test("Mishi", "Siames")

    list_all()
# %%
