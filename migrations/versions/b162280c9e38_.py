"""empty message

Revision ID: b162280c9e38
Revises: 5a469a258312
Create Date: 2025-04-03 10:44:19.893247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b162280c9e38'
down_revision = '5a469a258312'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('follower', schema=None) as batch_op:
        batch_op.drop_constraint('follower_user_from_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('follower_user_to_id_fkey', type_='foreignkey')

    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_constraint('media_post_id_fkey', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.create_foreign_key('media_post_id_fkey', 'post', ['post_id'], ['id'])

    with op.batch_alter_table('follower', schema=None) as batch_op:
        batch_op.create_foreign_key('follower_user_to_id_fkey', 'user', ['user_to_id'], ['id'])
        batch_op.create_foreign_key('follower_user_from_id_fkey', 'user', ['user_from_id'], ['id'])

    # ### end Alembic commands ###
