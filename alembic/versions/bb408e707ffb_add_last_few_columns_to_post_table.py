"""add last few columns to post table 

Revision ID: bb408e707ffb
Revises: a141b0428c26
Create Date: 2023-09-03 21:19:07.218914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb408e707ffb'
down_revision: Union[str, None] = 'a141b0428c26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op. add_column('posts', sa.Column(
        'published',sa.Boolean(), nullable=False, server_default= 'TRUE'
    ),)
    op.add_column('posts', sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text(
            'NOW()')),)
        
   
    pass


def downgrade() -> None:
    op.drop_column('posts','published'),
    op.drop_column('posts','created_at')
    pass
