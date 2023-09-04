"""create post table

Revision ID: 4a7250f62d7c
Revises: 
Create Date: 2023-09-02 22:28:42.223074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7250f62d7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() :
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
