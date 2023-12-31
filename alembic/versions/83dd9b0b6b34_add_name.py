"""add name

Revision ID: 83dd9b0b6b34
Revises: 6d074a1c3cb5
Create Date: 2023-09-04 10:45:27.129775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83dd9b0b6b34'
down_revision: Union[str, None] = '6d074a1c3cb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
