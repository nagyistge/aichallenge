from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from battlebots import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

import battlebots.database.listeners
