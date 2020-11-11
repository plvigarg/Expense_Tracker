from models import Transactions, Users
from connect import db

all_data = Transactions.query.all()
for row in all_data:
    print(f"{row.id}, {row.description}, {row.cashFlow}, {row.cat}, {row.date}, {row.amount}, {row.userId}")
