from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Domain(Base):
        __tablename__ = 'malicious_domain'
        id = Column(Integer(), primary_key=True)
        domain = Column(String(), unique=True)
        first_seen = Column(String(), nullable=True)
        resource = Column(String(), nullable=False)


class Url(Base):
        __tablename__ = 'malicious_url'
        id = Column(Integer(), primary_key=True)
        url = Column(String(), nullable=False)
        domain_id = Column(
                Integer(),
                ForeignKey('malicious_domain.id'),
                nullable=False
        )
        dom = relationship(Domain)
        submission = Column(String(), nullable=True)
        resource = Column(String(), nullable=False)


class IP(Base):
        __tablename__ = 'malicious_ip'
        id = Column(Integer, primary_key=True)
        ip = Column(String(), nullable=False)
        resource = Column(String(), nullable=False)


engine = create_engine('sqlite:///DBMaliciousURL.db')
Base.metadata.create_all(engine)
