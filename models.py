print("\n=== NOMOR 2 ===")

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BukuDB(Base):
    __tablename__ = 'buku'
    id = Column(Integer, primary_key=True)
    judul = Column(String(255), nullable=False)
    penulis = Column(String(255), nullable=False)
    penerbit = Column(String(255))
    tahun_terbit = Column(Integer)
    konten = Column(Text)
    iktsar = Column(Text)

# Setup database connection
engine = create_engine('sqlite:///perpustakaan.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



print("\n=== NOMOR 3 ===")

def get_buku_by_id(buku_id):
    return session.query(BukuDB).filter(BukuDB.id == buku_id).first()


print("\n=== NOMOR 4 ===")

def save_buku(buku):
    buku_db = BukuDB(
        judul=buku.judul,
        penulis=buku.penulis,
        penerbit=buku.penerbit,
        tahun_terbit=buku.tahun_terbit,
        konten='\n'.join(buku.konten),
        iktsar=buku.iktsar
    )
    session.add(buku_db)
    session.commit()

