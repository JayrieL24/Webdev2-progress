# model/admin.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

AdminRouter = APIRouter(tags=["Admin"])

@AdminRouter.get("/Admin", response_model=list)
async def read_Admin(
    db=Depends(get_db)
):
    query= "SELECT Admin_ID, ID, Lab_Assigned, Name FROM admin"
    db[0].execute(query)
    Admin = [{ "Admin_ID": Admin[0], "ID": Admin[1], "Lab_Assigned": Admin[2], "Name": Admin[3]} for Admin in db[0].fetchall()]
    return Admin

@AdminRouter.get("/Admin/{Admin_ID}", response_model=dict)
async def read_Admin(
    ID: str ,
    db=Depends(get_db)
):
    query = "SELECT Admin_ID, Lab_Assigned , Name FROM admin WHERE ID = %s"
    db[0].execute(query, (ID,))
    Admin = db[0].fetchone()
    
    if Admin:
        return{
        "Admin_ID": Admin[0],
        "Lab_Assigned": Admin[1],
        "Name": Admin[2],
        }
    raise HTTPException(status_code=404, detail="Admin not found")


@AdminRouter.post("/Admin",response_model=dict)
async def create_Admin(
     ID: str = Form(...),
     Lab_Assigned: str = Form(...),
     Name: str = Form(...),
     db=Depends(get_db)
):
    query="INSERT INTO admin ( ID, Lab_Assigned, Name) VALUES (%s,%s,%s) "
    db[0].execute(query, (ID,Lab_Assigned,Name)) 
    db[1].commit()

    db[0].execute("SELECT LAST_INSERT_ID()")
    new_admin_id = db[0].fetchone()[0]
    db[1].commit()

    return{
              "ID": ID,
              "Lab_Assigned": Lab_Assigned,
              "Name": Name,
    }

@AdminRouter.put("/Admin/{Admin}", response_model=dict)
async def update_Admin( 
     Admin_ID: str = Form(...),
     Lab_Assigned: str = Form(...),
     Name: str = Form(...),
     db=Depends(get_db)
):
   
    query = "UPDATE admin SET Lab_Assigned = %s, Name = %s  WHERE Admin_ID = %s "
    db[0].execute(query,( Lab_Assigned, Name, Admin_ID, ))
    
    if db[0].rowcount > 0 :
        db[1].commit()
        return{"message": "Admin Updated Successfully"}
    
    raise HTTPException(status_code=404, detail="Admin not found")


@AdminRouter.delete("Admin/{Admin}", response_model=dict)
async def delete_Admin(
     ID: int = Form(...),
     db=Depends(get_db)
): 
    try:
        query_check_Admin = "SELECT ID from admin WHERE ID = %s"
        db[0].execute(query_check_Admin,(ID,))
        existing_Admin= db[0].fetchone()
        
        if not existing_Admin:
            raise HTTPException(status_code=404, detail="Category not found")
        
        query_delete_Item = "DELETE FROM admin WHERE ID = %s"
        db[0].execute(query_delete_Item, (ID,))
        db[1].commit()
        
        return{"message": "Admin Deleted Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        db[0].close()