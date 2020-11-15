from models import Transactions, Users
from connect import db

all_data = Transactions.query.all()
all_data1 = Users.query.all()
for row in all_data:
    print(f"{row.id}, {row.description}, {row.cashFlow}, {row.cat}, {row.date}, {row.amount}, {row.userId}")

for row in all_data1:
    print(f"{row.profile_image}")
