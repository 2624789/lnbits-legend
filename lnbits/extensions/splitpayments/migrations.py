async def m001_initial(db):
    """
    Initial split payment table.
    """
    await db.execute(
        """
        CREATE TABLE splitpayments.targets (
            wallet TEXT NOT NULL,
            source TEXT NOT NULL,
            percent INTEGER NOT NULL CHECK (percent >= 0 AND percent <= 100),
            alias TEXT,

            UNIQUE (source, wallet)
        );
        """
    )


async def m002_change_percent_column(db):
    """
    Change percent type from integer to numeric
    """
    await db.execute(
        """
        ALTER TABLE splitpayments.targets
        DROP COLUMN percent;
        """
    )
    await db.execute(
        """
        ALTER TABLE splitpayments.targets
        ADD COLUMN percent NUMERIC NOT NULL CHECK (percent >= 0 AND percent <= 1);
        """
    )
