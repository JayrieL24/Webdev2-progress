from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.admin import AdminRouter
from model.Borrower import BorrowerRouter
from model.items import ItemsRouter 
from model.BorrowedTransaction import BorrowedTransactionRouter
from model.users import UsersRouter


app = FastAPI()

# Include routers
app.include_router(AdminRouter, prefix="/api")
app.include_router(BorrowerRouter, prefix="/api")
app.include_router(ItemsRouter, prefix="/api")
app.include_router(BorrowedTransactionRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)