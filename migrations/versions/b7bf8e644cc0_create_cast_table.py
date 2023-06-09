"""create cast table

Revision ID: b7bf8e644cc0
Revises: c79820a8b0e9
Create Date: 2023-04-20 12:28:11.096385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7bf8e644cc0'
down_revision = 'c79820a8b0e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('castmembers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('production_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['production_id'], ['productions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('castmembers')
    # ### end Alembic commands ###
