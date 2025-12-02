from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = 'create_posts_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('category', sa.String(100), nullable=False),
        sa.Column(
            'created_date',
            sa.TIMESTAMP(),
            server_default=text("CURRENT_TIMESTAMP")
        ),
        sa.Column(
            'updated_date',
            sa.TIMESTAMP(),
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
        ),
        sa.Column('status', sa.String(100), nullable=False),
        sa.CheckConstraint(
            "status IN ('publish', 'draft', 'thrash')",
            name="status_check"
        )
    )


def downgrade():
    op.drop_table('posts')
