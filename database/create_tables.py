"""
Create database tables.
"""

from database.database_connection import get_connection


def create_damage_table():
    """
    Create damage table with the required schema.
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Create damages table if it does not exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS damages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT,
            damage_type TEXT,
            confidence REAL,
            severity TEXT,
            latitude REAL,
            longitude REAL,
            timestamp TEXT
        )
        """
    )

    connection.commit()
    connection.close()
    print("Table 'damages' created successfully.")


if __name__ == "__main__":
    create_damage_table()