# model/borrower.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

BorrowerRouter = APIRouter(tags=["Borrower"])

@BorrowerRouter.get("/Borrower", response_model=list)
async def read_borrowers(
    db=Depends(get_db)

):
    query="SELECT * from borrower"
    db[0].execute(query)
    borrower = [{"BorrowerID": borrower[0], "ID": borrower[1], "Borrowed_Date": borrower[2], "Status": borrower[3]} for borrower in db [0].fetchall()] 
    return borrower

@BorrowerRouter.get("/Borrower/{Borrower_ID}", response_model=dict)
async def read_borrower(
  find_ID: str ,
  db=Depends(get_db)
):
    query="SELECT BorrowerID, Borrowed_Date, Status FROM borrower WHERE ID = %s"
    db[0].execute(query, (find_ID,))
    borrower = db[0].fetchone()
    
    if borrower:
        return{
            "BorrowerID": borrower[0],
            "Borrowed_Date": borrower[1],
            "Status": borrower[2],
        }
    raise HTTPException(status_code=404, detail="Borrower not found")

@BorrowerRouter.put("/Borrower/{Borrower_Update}", response_model=dict)
async def update_borrower( 
     Find_ID: str = Form(...),
     Status: str = Form(...),
     db=Depends(get_db)
):
   
    query = "UPDATE borrower SET Status = %s WHERE ID = %s "
    db[0].execute(query,(Status, Find_ID, ))
    
    if db[0].rowcount > 0 :
        db[1].commit()
        return{"message": "Borrower Updated Successfully"}
    
    raise HTTPException(status_code=404, detail="Borrower not found")

@BorrowerRouter.delete("Borrower/{Borrower_Delete}", response_model=dict)
async def delete_Admin(
     Find_ID: str = Form(...),
     db=Depends(get_db)
): 
    try:
        query_check_Borrower = "SELECT BorrowerID from borrower WHERE BorrowerID = %s"
        db[0].execute(query_check_Borrower,(Find_ID,))
        existing_Borrower= db[0].fetchone()
        
        if not existing_Borrower:
            raise HTTPException(status_code=404, detail="Borrower not found")
        
        query_delete_Borrower= "DELETE FROM borrower WHERE BorrowerID = %s"
        db[0].execute(query_delete_Borrower, (Find_ID,))
        db[1].commit()
        
        return{"message": "Borrower Deleted Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        db[0].close()