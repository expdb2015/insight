"""empty message

Revision ID: 0a7d298bcc36
Revises: 1f593ad2c634
Create Date: 2016-08-01 00:22:38.756733

"""

# revision identifiers, used by Alembic.
revision = '0a7d298bcc36'
down_revision = '1f593ad2c634'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assets', 'root_dir')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assets', sa.Column('root_dir', mysql.VARCHAR(length=64), nullable=True))
    ### end Alembic commands ###