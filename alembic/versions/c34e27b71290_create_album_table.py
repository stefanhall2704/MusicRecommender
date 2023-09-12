"""create album table

Revision ID: c34e27b71290
Revises: 8c1e22a36981
Create Date: 2023-09-11 23:14:13.781620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c34e27b71290'
down_revision: Union[str, None] = '8c1e22a36981'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

"""
Artist: Relationship to Artist ID
ID
Album Metrics:
Title: 'name'
Music Label: 'label'
Popularity
Release Date
Total Tracks
Tracks: relationship to Track table ID
Type: (example: album)
"""
def upgrade() -> None:
    op.create_table(
        "Album",
        sa.Column("ID", sa.Integer, primary_key=True),
        sa.Column("Title", sa.String(100), nullable=False),
        sa.Column("MusicLabel", sa.String(200), nullable=False),
        sa.Column("Popularity", sa.Integer, nullable=False),
        sa.Column("ReleaseDate", sa.String(100), nullable=False),
        sa.Column("TotalTracks", sa.Integer, nullable=False),
        sa.Column("Type", sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("Album")
