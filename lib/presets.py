from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from os.path import exists
from os import mkdir

Base=declarative_base()

if not exists("dbs"):
	mkdir("dbs")

class Preset(Base):
	__tablename__ = "Preset"
	name = Column("name", String, primary_key = True)
	browser = Column("browser", String)
	url = Column("url", String)
	userfield = Column("userfield", String)
	passwordfield = Column("passwordfield", String)
	formnumber = Column("formnumber", Integer)
	button = Column("button", String)
	targeturl = Column("targeturl", String)

	def __init__(self,name,browser,url,userfield,passwordfield,formnumber,button,targeturl):
		self.name=name
		self.browser=browser
		self.url=url
		self.userfield=userfield
		self.passwordfield=passwordfield
		self.formnumber=formnumber
		self.button=button
		self.targeturl=targeturl

engine = create_engine("sqlite:///dbs/presets.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def make_preset(name,browser,url,userfield,passwordfield,formnumber,button,targeturl):
	p=Preset(name,browser,url,userfield,passwordfield,int(formnumber),button,targeturl)
	try:
		session.add(p)
		session.commit()
	except Exception as e:
		print(e)

def load_preset(args):
	p=session.query(Preset).filter(Preset.name==args.presetname).first()
	attrs=["browser","url","userfield","passwordfield","formnumber","button","targeturl"]
	for attr in attrs:
		if not hasattr(args,attr):
			setattr(args,attr,getattr(p,attr))
	return args
