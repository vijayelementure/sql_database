from sqlalchemy import Integer,String
from db.database import Base
from sqlalchemy import Column

class DbUser(Base):
    __tablename__= "mqtt-paho-client"
    
    id = Column(Integer,primary_key=True)
    pub_topic = Column(String)
    topic_payload = Column(String)


'''class DbUser(Base):
    __tablename__= "vijay"
    
    id = Column(Integer,primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)'''