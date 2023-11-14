"""empty message

Revision ID: 16a81ced67fa
Revises: 3ae56ae3765b
Create Date: 2023-11-14 14:59:33.036491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a81ced67fa'
down_revision = '3ae56ae3765b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('climate', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('created', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('diameter', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_column('diameter')
        batch_op.drop_column('created')
        batch_op.drop_column('climate')

    # ### end Alembic commands ###