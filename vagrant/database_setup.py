import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import creat_engine
Base = declaretive_base()
engine = creat_engine ( sqlite:///restaurantmenu.db')
