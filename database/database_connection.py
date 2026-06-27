"""
Create database connection.
"""

import sqlite3
import os


def get_connection():
    """
    Connect to SQLite database.
    """
    # Use absolute path relative to project root to avoid database duplication
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(project_root, "road_damage.db")
    connection = sqlite3.connect(db_path)
    return connection


if __name__ == "__main__":
    conn = get_connection()
    print("Database connected successfully.")
    conn.close()