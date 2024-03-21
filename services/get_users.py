from database.database import connection
from fastapi import HTTPException
import json

def GetUsers():
    # Example: Fetch item from MySQL database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    item = cursor.fetchall()
    cursor.close()
    if not item:
        raise HTTPException(status_code=404, detail="Users not found")
    response = []
    for user in item:
        fields = {
            'userid': user[0],
            'uuid': user[1],
            'email': user[2],
            'username': user[3],
            'firstname': user[5],
            'lastname': user[6],
        }
        response.append(fields)
    return json.loads(json.dumps(response))