"""Track

Revision ID: f742dae99335
Revises: 1d523f4c5703
Create Date: 2023-09-17 21:15:23.282754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f742dae99335'
down_revision: Union[str, None] = '1d523f4c5703'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('Track',
    # sa.Column('ID', sa.Integer(), nullable=False),
    # sa.Column('Title', sa.String(length=200), nullable=False),
    # sa.Column('DurationMS', sa.Integer(), nullable=False),
    # sa.Column('Explicit', sa.Boolean(), nullable=False),
    # sa.Column('TrackID', sa.String(length=100), nullable=False),
    # sa.Column('SpotifyURL', sa.String(length=150), nullable=False),
    # sa.Column('AlbumID', sa.Integer(), nullable=False),
    # sa.Column('ArtistID', sa.Integer(), nullable=False),
    # sa.ForeignKeyConstraint(['AlbumID'], ['Album.ID'], ),
    # sa.ForeignKeyConstraint(['ArtistID'], ['Artist.ID'], ),
    # sa.PrimaryKeyConstraint('ID')
    # )
    # op.create_index(op.f('ix_Artist_ID'), 'Artist', ['ID'], unique=False)
    # op.create_unique_constraint('unique_artist_id', 'Artist', ['ArtistID'])
    # op.create_unique_constraint(None, 'Artist', ['ArtistID'])
    # op.drop_constraint(None, 'ArtistRelatedAlbum', type_='foreignkey')
    # op.drop_constraint(None, 'ArtistRelatedAlbum', type_='foreignkey')
    # op.create_index(op.f('ix_ArtistRelatedGenre_ID'), 'ArtistRelatedGenre', ['ID'], unique=False)
    # # ### end Alembic commands ###


def downgrade() -> None:
    pass
    # op.drop_table('Track')
    # # ### end Alembic commands ###
