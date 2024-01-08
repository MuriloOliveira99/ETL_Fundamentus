from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Fundamentus(Base):
    # nome da tabela
    __tablename__ = 'fundamentus' 
    
    # chave primária
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # campos
    papel = Column(String(10), nullable=False)
    segmento = Column(String(30), nullable=False)
    cotacao = Column(Float, nullable=False)
    ffo_yield = Column(Float, nullable=False)
    dividend_yield = Column(Float, nullable=False)
    p_vp = Column(Float, nullable=False)
    valor_mercado = Column(Float, nullable=False)
    liquidez = Column(Float, nullable=False)
    qtd_imovel = Column(Integer, nullable=False)
    preco_m2 = Column(Float, nullable=False)
    aluguel_m2 = Column(Float, nullable=False)
    cap_rate = Column(Float, nullable=False)
    vacancia_media = Column(Float, nullable=False)
        

def conn_db():
    SERVER = ""
    DATABASE = ""
    DRIVER = ""
    
    CONN = f"mssql+pyodbc://{SERVER}/{DATABASE}?trusted_connection=yes&driver={DRIVER}" 
    engine = create_engine(CONN) 
    return engine

def create_table(engine):
    return Base.metadata.create_all(bind=engine)

def sessao(engine):
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session

if __name__ == '__main__':

    engine = conn_db()
    conn_db()
    create_table(engine)




    
