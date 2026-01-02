from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(30), nullable= False) 
    firstname: Mapped[str] = mapped_column(String(25), nullable= False)
    lastname: Mapped[str] = mapped_column(String(25), nullable= False)
    email: Mapped[str] = mapped_column(
        String(120), unique = True, nullable= False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable= False)

class Followers(db.Model):
    __tablename__ = 'followers'
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key = True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key = True)

class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

class MediaEnum(enum.Enum):
    PHOTO = 'photo'
    VIDEO = 'video'

class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key = True)
    type: Mapped[MediaEnum] = mapped_column(db.Enum(MediaEnum), nullable= False)
    url: Mapped[str] = mapped_column(String(120))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))

class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key = True)
    comment_text: Mapped[str] = mapped_column(String(300), nullable= False)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))