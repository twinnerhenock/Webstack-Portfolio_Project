"""add content column to posts table

Revision ID: 5443199cbf4d
Revises: d62b4b88f657
Create Date: 2023-04-09 16:04:20.197871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5443199cbf4d'
down_revision = 'd62b4b88f657'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
