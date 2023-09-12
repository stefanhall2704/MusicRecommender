"""create ablum - artist relate table

Revision ID: c6957c14d6e5
Revises: 794a14c13516
Create Date: 2023-09-11 23:19:59.460467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6957c14d6e5'
down_revision: Union[str, None] = '794a14c13516'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ArtistRelatedAlbum',
        sa.Column('ID', sa.Integer(), nullable=False),
        sa.Column('ArtistID', sa.Integer(), nullable=False),
        sa.Column('AlbumID', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['ArtistID'], ['Artist.ID'], ),
        sa.ForeignKeyConstraint(['AlbumID'], ['Album.ID'], ),
        sa.PrimaryKeyConstraint('ID')
    )


def downgrade() -> None:
    op.drop_table('ArtistRelatedAlbum')
