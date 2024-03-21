from fastapi import FastAPI
from router import routes as appRouter

app = FastAPI()

# Include routes using the appRouter function
app.include_router(appRouter.router)

# @app.get("/users/{user_id}")
# async def read_item(user_id: int):
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     item = cursor.fetchone()
#     cursor.close()
#     return item

# @app.get("/users/")
# async def main():
#     srv = GetUsers()
#     return srv

# @app.post("/items/")
# async def create_item(name: str):
#     # Example: Insert item into MySQL database
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
#     connection.commit()
#     cursor.close()
#     return {"message": "Item created successfully"}