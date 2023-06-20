"""Migrate

Revision ID: b32b5cb53f87
Revises: f67a0d1bae17
Create Date: 2023-04-01 18:56:46.496112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b32b5cb53f87'
down_revision = 'f67a0d1bae17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publishers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1500), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('publisher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['publisher_id'], ['publishers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publisher_author',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('publisher_author')
    op.drop_table('books')
    op.drop_table('publishers')
    op.drop_table('authors')
    # ### end Alembic commands ###
