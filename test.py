from models import Transactions, Users
from connect import db

all_data = Transactions.query.all()
print(all_data)