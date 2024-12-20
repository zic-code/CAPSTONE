"""Add company_name column to Stocks

Revision ID: 59a421e7c4e7
Revises: 
Create Date: 2024-10-31 02:16:34.298001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59a421e7c4e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stocks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('sector', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stocks', schema=None) as batch_op:
        batch_op.drop_column('sector')
        batch_op.drop_column('company_name')

    # ### end Alembic commands ###
