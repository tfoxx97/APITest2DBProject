import json
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class JSONEncodedResult(TypeDecorator):
    '''format for entering data: {"teardown": "unexpected error at teardown: ...}'''
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class Results(Base):
    __tablename__ = "Results"

    id = Column(Integer, primary_key=True)
    firmware_id = Column(Integer, ForeignKey('Firmware.id'))
    date_tested = Column(DateTime)
    component = Column(String(50))
    feature = Column(String(50))
    scenarioID = Column(Integer)
    result = Column(Boolean)
    debug = Column(JSONEncodedResult, nullable=True)

class Firmware(Base):
    __tablename__ = "Firmware"

    id = Column(Integer, primary_key=True)
    release_id = Column(Integer, ForeignKey('Release.id'))
    firmware = Column("firmware", String)

class Release(Base):
    __tablename__ = "Release"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    firmwares = relationship("Firmware", backref="release")

#create table
engine = create_engine('sqlite:///firmware.db')
Base.metadata.create_all(engine)