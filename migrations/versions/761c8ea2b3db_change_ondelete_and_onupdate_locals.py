"""change ondelete and onupdate locals

Revision ID: 761c8ea2b3db
Revises: 4e73d0b97781
Create Date: 2021-01-15 15:50:30.031948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '761c8ea2b3db'
down_revision = '4e73d0b97781'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('sorcerers_guild_id_fkey', 'sorcerers', type_='foreignkey')
    op.create_foreign_key(None, 'sorcerers', 'guilds', ['guild_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sorcerers', type_='foreignkey')
    op.create_foreign_key('sorcerers_guild_id_fkey', 'sorcerers', 'guilds', ['guild_id'], ['id'])
    # ### end Alembic commands ###
