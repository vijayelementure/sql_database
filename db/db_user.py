from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

def create_user(db:Session,request:UserBase):
    new_user = DbUser(
        pub_topic = request.pub_topic,
        topic_payload = request.topic_payload,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



'''def create_user(db:Session,request:UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user'''


'''def get_all_users(db:Session):
    return db.query(DbUser).all()'''


    