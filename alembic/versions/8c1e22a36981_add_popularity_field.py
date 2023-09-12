"""add popularity field

Revision ID: 8c1e22a36981
Revises: c3a90722e95f
Create Date: 2023-09-11 20:39:58.131212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c1e22a36981'
down_revision: Union[str, None] = 'c3a90722e95f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Artist', sa.Column("Popularity", sa.Integer, nullable=False))

def downgrade() -> None:
    op.drop_column('Artist', "Popularity")
