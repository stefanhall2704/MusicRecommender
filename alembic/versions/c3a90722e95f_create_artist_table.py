"""create artist table

Revision ID: c3a90722e95f
Revises: 
Create Date: 2023-09-11 20:09:21.187861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c3a90722e95f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Artist",
        sa.Column("ID", sa.Integer, primary_key=True),
        sa.Column("Name", sa.String(50), nullable=False),
        sa.Column("ArtistID", sa.String(100), nullable=False),
        sa.Column("Followers", sa.Integer, nullable=False),
        sa.Column("Genre", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("Artist")
