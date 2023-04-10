"""create posts table

Revision ID: d62b4b88f657
Revises: 
Create Date: 2023-04-09 15:29:35.685762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd62b4b88f657'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable=True))
    pass



def downgrade():
    op.drop_table('posts')
    pass
