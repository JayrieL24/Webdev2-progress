# model/users.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
import bcrypt

UsersRouter = APIRouter(tags=["User"])

# CRUD operations

@UsersRouter.get("/User/", response_model=list)
async def read_users(
    db=Depends(get_db)
):
    query = "SELECT ID, Name,Course , Department, Role FROM user"
    db[0].execute(query)
    user = [{"ID": user[0], "Name": user[1], "Course": user[2], "Department":user[3], "Role": user[4]} for user in db[0].fetchall()]
    return user

@UsersRouter.get("/User/{UserID}", response_model=dict)
async def read_user(
    Find_ID: str,
    db=Depends(get_db)
):
    query = "SELECT ID, Name, Course, Department, Role FROM user WHERE ID = %s"
    db[0].execute(query, (Find_ID,))
    user = db[0].fetchone()
    
    if user:
        return{
        "ID": user[0],
        "Name": user[1],
        "Course": user[2],
        "Department": user[3],
        "Role": user[4],
        }
    raise HTTPException(status_code=404, detail="User not found")

@UsersRouter.post("/User/{CreateID}", response_model=dict)
async def create_user(
    ID: str = Form(...), 
    Name: str = Form(...), 
    Course: str = Form(...), 
    Department: str = Form(...),
    Role: str = Form(...),
    db=Depends(get_db)
):

    query = "INSERT INTO user (ID, Name, Course, Department, Role) VALUES (%s, %s, %s, %s, %s)"
    db[0].execute(query, (ID, Name, Course, Department, Role))
    db[1].commit()
    return {"ID": ID, "Name": Name, "Course": Course, "Department": Department, "Role": Role, "message": "User created successfully"}

    

@UsersRouter.put("/User/{UserID}", response_model=dict)
async def update_user(
    Find_ID: str,
    Name: str = Form(...),
    Course: str = Form(None),  
    Department: str = Form(...),
    Role: str = Form(...),
    db=Depends(get_db)
):
    # Update user information in the database 
    query = "UPDATE user SET Name = %s, Course = %s, Department = %s, Role = %s WHERE ID = %s"
    db[0].execute(query, (Name, Course, Department, Role, Find_ID))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "User updated successfully"}
    
    # If no rows were affected, user not found
    raise HTTPException(status_code=404, detail="User not found")

