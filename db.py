
import sqlite3

# Create database
def create_table():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats (user TEXT, bot TEXT)''')
    conn.commit()
    conn.close()

# Save chat history
def save_chat(user, bot):
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO chats (user, bot) VALUES (?, ?)", (user, bot))
    conn.commit()
    conn.close()

# Retrieve chat history
def retrieve_chats():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM chats ORDER BY rowid DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return rows

# Initialize DB
if __name__ == "__main__":
    create_table()
