import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import creat_engine
Base = declaretive_base()
####beginning line####

class Restaurant(Base):
  _tablename_ = 'restaurant'
  name = Column(String(80), nullable = False)
  id = Column(Integer, primary_key = True)
  
class MenuItem(Base):
  _tablename_ = 'menu_item'
  name = Column(String(80), nullable = False)
  id = Column(Integer, primary_key = True)
  course = Column(String(250))
  description = Column(String(250))
  price = Column(String(8))
  restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
  restaurant = relationship(Restaurant)
  
  
  
####end line####
engine = creat_engine ( sqlite:///restaurantmenu.db')
Base.metabata.create_all(engine)
