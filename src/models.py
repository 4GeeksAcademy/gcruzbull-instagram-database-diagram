from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    



class Follower(db.Model):
    user_to_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    user_from_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    


    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #     }
    

    
class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(unique=True, nullable=False)


    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #         # do not serialize the password, its a security breach
    #     }



class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True, nullable=False)


    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #         # do not serialize the password, its a security breach
    #     }
    

    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(unique=True, nullable=False)


    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #         # do not serialize the password, its a security breach
    #     }
