import sqlite3

class data_base():
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.request = self.connection.cursor()

    def create_table_information(self):
        self.request.execute('CREATE TABLE IF NOT EXISTS information(id INTEGER PRIMARY KEY, nickname TEXT, level TEXT, time INTEGER)')
        self.connection.commit()
    def insert_info(self, nickname, level, time):
        self.request.execute('INSERT INTO information (nickname, level, time) VALUES(?, ?, ?)', (nickname, level, time))
        self.connection.commit()
    def print_all_information(self):
        self.request.execute('SELECT * FROM information')
        info = self.request.fetchall()

        for i in info:
            print(i)
    def close_data_base(self):
        self.connection.close()

    def delete_info(self, del_id):
        self.request.execute('DELETE FROM information WHERE id = ?', (del_id, ))
        self.connection.commit()

    def edit(self, id, new_nickname, new_level, new_time):
        self.request.execute('UPDATE information SET nickname = ?, level = ?, time = ? WHERE id = ?', (new_nickname, new_level, new_time, id))
        self.connection.commit()

    def get_all_data(self):
        self.request.execute('SELECT * FROM information')
        info = self.request.fetchall()
        return info

    def get_players_level(self, level):
        self.request.execute('SELECT * FROM information WHERE level = ? ORDER BY time', (level,))
        info = self.request.fetchall()
        return info
