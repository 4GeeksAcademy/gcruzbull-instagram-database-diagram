from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey, Enum
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    comment: Mapped[List["Comment"]] = relationship(back_populates="user")
    post: Mapped[List["Post"]] = relationship(back_populates="user")
    

class Follower(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    
class MediaType(enum.Enum):
    image = "image"
    video = "video"

    
class Media(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[enum.Enum] = mapped_column(Enum(MediaType), nullable=False)
    url: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)
    post: Mapped["Post"] = relationship(back_populates="media")

class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="post")
    comment: Mapped[List["Comment"]] = relationship(back_populates="post")

    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="comment")
    post: Mapped["Post"] = relationship(back_populates="comment")


    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #         # do not serialize the password, its a security breach
    #     }
