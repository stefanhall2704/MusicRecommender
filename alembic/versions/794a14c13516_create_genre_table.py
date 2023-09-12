"""create genre table

Revision ID: 794a14c13516
Revises: c34e27b71290
Create Date: 2023-09-11 23:18:43.563564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '794a14c13516'
down_revision: Union[str, None] = 'c34e27b71290'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Genre",
        sa.Column("ID", sa.Integer, primary_key=True),
        sa.Column("Name", sa.String(100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("Genre")
