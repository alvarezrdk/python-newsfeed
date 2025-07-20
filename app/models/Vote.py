from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey, select, func
from sqlalchemy.orm import column_property

class Vote(Base):
  __tablename__ = 'votes'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))
  count = column_property(
      select(func.count(post_id))
      .where(post_id == id)
  )

