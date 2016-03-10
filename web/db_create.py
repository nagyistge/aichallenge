from migrate.versioning import api
from web.config import SQLALCHEMY_DATABASE_URI
from web.config import SQLALCHEMY_MIGRATE_REPO
from web import db

import os.path
print("Creating new Battlebots databees")
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,
                        SQLALCHEMY_MIGRATE_REPO,
                        api.version(SQLALCHEMY_MIGRATE_REPO))
db.create_all()
