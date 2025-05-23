"""Category model2

Revision ID: a21fb155f0a9
Revises: c50b62e5d148
Create Date: 2025-01-23 11:41:49.932776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a21fb155f0a9'
down_revision: Union[str, None] = 'c50b62e5d148'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_uz', sa.String(), nullable=False),
    sa.Column('name_ru', sa.String(), nullable=False),
    sa.Column('name_en', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###
