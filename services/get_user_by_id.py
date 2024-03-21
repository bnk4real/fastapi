from database.database import connection
import json

def GetUserById(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE userid = %s", (user_id,))
    item = cursor.fetchone()
    cursor.close()
    return json.loads(json.dumps(item))