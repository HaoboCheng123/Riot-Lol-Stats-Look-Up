"""Third migration

Revision ID: 21f42920b92f
Revises: dfdd22366e2c
Create Date: 2022-07-23 02:49:20.535723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21f42920b92f'
down_revision = 'dfdd22366e2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('sex', sa.String(length=20), nullable=False))
    op.drop_column('profile', 'height')
    op.drop_column('profile', 'school')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('school', sa.VARCHAR(length=20), nullable=False))
    op.add_column('profile', sa.Column('height', sa.INTEGER(), nullable=False))
    op.drop_column('profile', 'sex')
    # ### end Alembic commands ###
