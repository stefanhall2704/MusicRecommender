"""add album_id field to Album table

Revision ID: f1cfa747ee20
Revises: f742dae99335
Create Date: 2023-09-18 21:01:19.599441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1cfa747ee20'
down_revision: Union[str, None] = 'f742dae99335'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Album', sa.Column("AlbumID", sa.String(100), nullable=False))


def downgrade() -> None:
    op.drop_column('Album', "AlbumID")
