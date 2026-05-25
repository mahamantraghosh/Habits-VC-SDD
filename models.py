import sqlite3

class HabitModel:
    def __init__(self, db_name="sdd_habits.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                is_done BOOLEAN NOT NULL CHECK (is_done IN (0, 1)),
                streak INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_habit(self, name):
        self.cursor.execute('INSERT INTO habits (name, is_done, streak) VALUES (?, 0, 0)', (name,))
        self.conn.commit()

    def get_all_habits(self):
        self.cursor.execute('SELECT id, name, is_done, streak FROM habits')
        return self.cursor.fetchall()

    def toggle_habit(self, habit_id):
        self.cursor.execute('SELECT is_done, streak FROM habits WHERE id = ?', (habit_id,))
        result = self.cursor.fetchone()
        if result:
            current_status, streak = result
            new_status = 0 if current_status == 1 else 1
            new_streak = streak + 1 if new_status == 1 else max(0, streak - 1)
            
            self.cursor.execute('''
                UPDATE habits SET is_done = ?, streak = ? WHERE id = ?
            ''', (new_status, new_streak, habit_id))
            self.conn.commit()

    def delete_habit(self, habit_id):
        self.cursor.execute('DELETE FROM habits WHERE id = ?', (habit_id,))
        self.conn.commit()