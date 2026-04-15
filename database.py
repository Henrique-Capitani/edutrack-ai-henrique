import sqlite3
from datetime import datetime
from pathlib import Path

DB_FILE = Path(__file__).parent / "subjects.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id TEXT NOT NULL,
                name TEXT NOT NULL,
                code TEXT,
                description TEXT,
                is_active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def get_subjects(owner_id: str):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM subjects WHERE owner_id = ? ORDER BY name COLLATE NOCASE",
            (owner_id,),
        ).fetchall()
    return [dict(row) for row in rows]


def add_subject(owner_id: str, name: str, code: str, description: str, is_active: bool):
    timestamp = datetime.utcnow().isoformat()
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO subjects (owner_id, name, code, description, is_active, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (owner_id, name.strip(), code.strip(), description.strip(), int(is_active), timestamp, timestamp),
        )
        conn.commit()
    return cursor.lastrowid


def delete_subject(subject_id: int, owner_id: str):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM subjects WHERE id = ? AND owner_id = ?",
            (subject_id, owner_id),
        )
        conn.commit()


def update_subject(subject_id: int, owner_id: str, name: str, code: str, description: str, is_active: bool):
    timestamp = datetime.utcnow().isoformat()
    with get_connection() as conn:
        conn.execute(
            """
            UPDATE subjects
            SET name = ?, code = ?, description = ?, is_active = ?, updated_at = ?
            WHERE id = ? AND owner_id = ?
            """,
            (name.strip(), code.strip(), description.strip(), int(is_active), timestamp, subject_id, owner_id),
        )
        conn.commit()
