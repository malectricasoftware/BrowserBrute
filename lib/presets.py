from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from os.path import exists
from os import mkdir
from contextlib import contextmanager

Base = declarative_base()

# Ensure the directory for the database exists
if not exists("dbs"):
    mkdir("dbs")

# Define the Preset model
class Preset(Base):
    __tablename__ = "Preset"
    name = Column("name", String, primary_key=True)
    browser = Column("browser", String)
    url = Column("url", String)
    userfield = Column("userfield", String)
    passwordfield = Column("passwordfield", String)
    formnumber = Column("formnumber", Integer)
    button = Column("button", String)
    targeturl = Column("targeturl", String)

    def __init__(self, name, browser, url, userfield, passwordfield, formnumber, button, targeturl):
        self.name = name
        self.browser = browser
        self.url = url
        self.userfield = userfield
        self.passwordfield = passwordfield
        self.formnumber = formnumber
        self.button = button
        self.targeturl = targeturl

# Database setup
engine = create_engine("sqlite:///dbs/presets.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

#manage context
@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
    finally:
        session.close()

#make preset
def make_preset(name, browser, url, userfield, passwordfield, formnumber, button, targeturl):
    p = Preset(name, browser, url, userfield, passwordfield, int(formnumber), button, targeturl)
    with get_session() as session:
        try:
            session.add(p)
        except Exception as e:
            print(f"Error adding preset: {e}")

#load preset
def load_preset(args):
	#with context manager
    with get_session() as session:

    	#query presets by preset name
        p = session.query(Preset).filter(Preset.name == args.presetname).first()

        #if one is found
        if p:

        	#attrs equal to the conlumn names from the preset model
            attrs = Preset.__table__.columns.keys()

            #for each column name in the preset model
            for attr in attrs:

            	#if the current column name is not already an argument
                if not hasattr(args, attr):

                	#set it as one
                    setattr(args, attr, getattr(p, attr))

        #error
        else:
            print(f"Preset '{args.presetname}' not found")

    #return args
    return args
