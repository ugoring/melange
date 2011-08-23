# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import datetime
from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.schema import MetaData
from sqlalchemy.schema import Table

from melange.db.sqlalchemy.migrate_repo.schema import Boolean
from melange.db.sqlalchemy.migrate_repo.schema import create_tables
from melange.db.sqlalchemy.migrate_repo.schema import DateTime
from melange.db.sqlalchemy.migrate_repo.schema import drop_tables
from melange.db.sqlalchemy.migrate_repo.schema import from_migration_import
from melange.db.sqlalchemy.migrate_repo.schema import Integer
from melange.db.sqlalchemy.migrate_repo.schema import String
from melange.db.sqlalchemy.migrate_repo.schema import Text
from melange.ipam import models


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    ip_block_table = Table('ip_blocks', meta)
    Column('is_full', Boolean()).create(ip_block_table)


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine
    Table('ip_blocks', meta, autoload=True).columns["is_full"].drop()