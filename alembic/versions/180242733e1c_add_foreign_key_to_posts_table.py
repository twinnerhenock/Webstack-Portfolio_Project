"""add foreign key to posts table

Revision ID: 180242733e1c
Revises: 9cb07c7570bf
Create Date: 2023-04-09 17:18:22.344451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '180242733e1c'
down_revision = '9cb07c7570bf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_down('posts', 'owner_id')
    pass
