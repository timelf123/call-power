"""call_session_referral_code

Revision ID: 7f361698d677
Revises: ae2d9ad59424
Create Date: 2017-10-12 19:50:43.278732

"""

# revision identifiers, used by Alembic.
revision = '7f361698d677'
down_revision = 'ae2d9ad59424'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calls_session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('referral_code', sa.String(length=64), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calls_session', schema=None) as batch_op:
        batch_op.drop_column('referral_code')

    ### end Alembic commands ###