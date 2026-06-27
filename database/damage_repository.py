"""
Repository for managing road damage records in the SQLite database.
"""

from datetime import datetime
from database.database_connection import get_connection
from database.create_tables import create_damage_table

# Automatically ensure the database table is initialized
try:
    create_damage_table()
except Exception as e:
    print(f"Error initializing database table: {e}")


def insert_damage(image_name, damage_type, confidence, severity, latitude, longitude):
    """
    Insert a new damage record into the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO damages (
            image_name,
            damage_type,
            confidence,
            severity,
            latitude,
            longitude,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            image_name,
            damage_type,
            confidence,
            severity,
            latitude,
            longitude,
            timestamp
        )
    )

    connection.commit()
    connection.close()
    print(f"Record for '{damage_type}' inserted successfully.")


def get_all_damages():
    """
    Retrieve all damage records from the database.
    Returns a list of dictionaries.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, image_name, damage_type, confidence, severity, latitude, longitude, timestamp FROM damages")
    rows = cursor.fetchall()
    
    damages = []
    for row in rows:
        damages.append({
            "id": row[0],
            "image_name": row[1],
            "damage_type": row[2],
            "confidence": row[3],
            "severity": row[4],
            "latitude": row[5],
            "longitude": row[6],
            "timestamp": row[7]
        })

    connection.close()
    return damages


def delete_damage(damage_id):
    """
    Delete a damage record by ID.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM damages WHERE id = ?", (damage_id,))
    connection.commit()
    connection.close()
    print(f"Record with ID {damage_id} deleted successfully.")


def get_damage_count():
    """
    Get the total number of damage records.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM damages")
    count = cursor.fetchone()[0]

    connection.close()
    return count
