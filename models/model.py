
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Membuat basis model database
Base = declarative_base()


class Mahasiswa(Base):
    # Nama tabel di database
    __tablename__ = "mahasiswa"

    # Struktur kolom tabel mahasiswa
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    ipk = Column(Float)
    sks = Column(Integer)
    status_kelulusan = Column(String)
