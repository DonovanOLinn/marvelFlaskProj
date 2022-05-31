"""empty message

Revision ID: adb466d407cb
Revises: 
Create Date: 2022-05-30 19:31:42.754821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adb466d407cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('marvel_character', sa.Column('owner_id', sa.String(length=80), nullable=True))
    op.drop_constraint('marvel_character_parent_id_fkey', 'marvel_character', type_='foreignkey')
    op.create_foreign_key(None, 'marvel_character', 'user', ['owner_id'], ['id'])
    op.drop_column('marvel_character', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('marvel_character', sa.Column('parent_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'marvel_character', type_='foreignkey')
    op.create_foreign_key('marvel_character_parent_id_fkey', 'marvel_character', 'user', ['parent_id'], ['id'])
    op.drop_column('marvel_character', 'owner_id')
    # ### end Alembic commands ###