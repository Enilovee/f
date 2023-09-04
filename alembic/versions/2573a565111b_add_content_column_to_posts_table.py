"""add content column to posts table

Revision ID: 2573a565111b
Revises: 4a7250f62d7c
Create Date: 2023-09-03 08:54:55.232294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2573a565111b'
down_revision: Union[str, None] = '4a7250f62d7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
