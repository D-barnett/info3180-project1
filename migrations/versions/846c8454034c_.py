"""empty message

Revision ID: 846c8454034c
Revises: b2d1ba7f2f50
Create Date: 2017-03-12 02:37:35.031720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846c8454034c'
down_revision = 'b2d1ba7f2f50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('user_profile', sa.Column('biography', sa.Text(), nullable=True))
    op.add_column('user_profile', sa.Column('gender', sa.String(length=8), nullable=True))
    op.add_column('user_profile', sa.Column('image', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'image')
    op.drop_column('user_profile', 'gender')
    op.drop_column('user_profile', 'biography')
    op.drop_column('user_profile', 'age')
    # ### end Alembic commands ###
