from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="Articals"
	articals_id=Column(Integer,primary_key=True)
	Title=Column(String)
	Topic=Column(String)
	Rate=Column(Integer)
	# print(articals_id)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	def prid(self):
		print(self.articals_id)

	def __repr__(self):
		if self.Rate>7:
			return ("Title: {}\n"
               "Topic: {} \n"
               "Rate {}").format(
                    self.Title, self.Topic, self.Rate)
		else:
			return("Unfortunately, this article does not have a better rating. Maybe, this is an article that should bereplaced soon!")

#x=Knowledge(articals_id=1,Title="123")
#x.prid()
#print(x)
#print(repr(Knowledge.__table__))

