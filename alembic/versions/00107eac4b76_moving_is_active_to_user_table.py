"""Moving us_active to user table

Revision ID: 00107eac4b76
Revises: 100d8ab94699
Create Date: 2022-12-31 12:16:41.898341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "00107eac4b76"
down_revision = "100d8ab94699"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("profiles", "is_active")
    op.add_column("users", sa.Column("is_active", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_active")
    op.add_column(
        "profiles",
        sa.Column(
            "is_active", sa.BOOLEAN(), autoincrement=False, nullable=True
        ),
    )
    # ### end Alembic commands ###
