from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(Title,Topic,Rate):
	global art
	art=Knowledge(Title=Title,Topic=Topic,Rate=Rate)
	session.add(art)
	session.commit()


def query_all_articles():#prints all the articals in the databaseb
	arti=session.query(Knowledge).all()
	return(arti)

def query_article_by_topic():
	s1=session.query(Knowledge).filter_by(Rate=10).first()
	return(s1)
#def query_article_by_primary_key(key):
	#s1=session.query(Knowledge).filter_by(id=1).first()
	#return(s1)


def delete_article_by_topic(r):
	s1=session.query(Knowledge).filter_by(Rate=r).delete()
	session.commit()

def delete_all_articles():
	s1=session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(ti,rate):
	art1=session.query(Knowledge).filter_by(Title=ti).first()
	art1.Rate=rate
	session.commit()
def delet_by_rate(r):
	for i in range(-1,r+1):
		delete_article_by_topic(i)
	session.commit()




add_article("try","viki",9)
#print(query_all_articles())
#print(query_article_by_topic())
#delete_all_articles()
#edit_article_rating("try",9)
delet_by_rate(10)
print(query_all_articles())
