"""create genre - artist relate table

Revision ID: 1d523f4c5703
Revises: c6957c14d6e5
Create Date: 2023-09-11 23:40:48.170878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d523f4c5703'
down_revision: Union[str, None] = 'c6957c14d6e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ArtistRelatedGenre',
        sa.Column('ID', sa.Integer(), nullable=False),
        sa.Column('ArtistID', sa.Integer(), nullable=False),
        sa.Column('GenreID', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['ArtistID'], ['Artist.ID'], ),
        sa.ForeignKeyConstraint(['GenreID'], ['Genre.ID'], ),
        sa.PrimaryKeyConstraint('ID')
    )


def downgrade() -> None:
    op.drop_table('ArtistRelatedGenre')
