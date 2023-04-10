"""add last few columns tomposts table

Revision ID: b46da8bcc734
Revises: 180242733e1c
Create Date: 2023-04-09 17:28:52.106850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b46da8bcc734'
down_revision = '180242733e1c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column("posts", sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')
    ),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
