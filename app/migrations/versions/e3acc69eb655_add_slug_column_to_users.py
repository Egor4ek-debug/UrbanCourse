"""Add slug column to users

Revision ID: e3acc69eb655
Revises: fcce2a0d2c52
Create Date: 2024-12-08 23:27:21.092540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3acc69eb655'
down_revision: Union[str, None] = 'fcce2a0d2c52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_index('ix_tasks_slug', table_name='tasks')
    op.drop_index('ix_tasks_user_id', table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('content', sa.VARCHAR(), nullable=True),
    sa.Column('priority', sa.INTEGER(), nullable=True),
    sa.Column('completed', sa.BOOLEAN(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('slug', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tasks_user_id', 'tasks', ['user_id'], unique=False)
    op.create_index('ix_tasks_slug', 'tasks', ['slug'], unique=1)
    op.create_index('ix_tasks_id', 'tasks', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=1)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
