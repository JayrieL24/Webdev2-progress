# model/BorrowedTransaction.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

BorrowedTransactionRouter = APIRouter(tags=["Transaction"])

@BorrowedTransactionRouter.get("/Transaction", response_model=list)
async def get_Transaction(
db=Depends(get_db)

): 
    query = "SELECT TransactionID, ID, ItemID, BorrowedDate, Status from borrowedtrasnaction JOIN borrower "
    db[0].execute(query)
    Transaction = [{"ID": Transaction[0], "ItemID": Transaction[1], "BorrowedDate": Transaction[2], "Status": Transaction[3]} for Transaction in db[0].fetchall()]
    return Transaction