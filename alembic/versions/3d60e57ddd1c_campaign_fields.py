"""campaign fields

Revision ID: 3d60e57ddd1c
Revises: 4acd6655c53a
Create Date: 2015-05-07 16:02:23.034185

"""

# revision identifiers, used by Alembic.
revision = '3d60e57ddd1c'
down_revision = '4acd6655c53a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaign_phone_numbers',
    sa.Column('campaign_id', sa.Integer(), nullable=True),
    sa.Column('phone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign_campaign.id'], ),
    sa.ForeignKeyConstraint(['phone_id'], ['campaign_phone.id'], ),
    sa.UniqueConstraint('phone_id')
    )
    op.add_column(u'campaign_campaign', sa.Column('allow_call_in', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'campaign_campaign', 'allow_call_in')
    op.drop_table('campaign_phone_numbers')
    ### end Alembic commands ###
