from connect import db
from models import Transactions
from flask_login import current_user
from datetime import datetime
from sqlalchemy import func
import numpy as np

today = datetime.today()


# def total_value(mydate):
#     amount = 0
#     uid = current_user.id
#     for obj in Transactions.query.filter_by(UserId = uid).all():
#         if mydate<=today:
#             if obj.cashFlow == 1:
#                 amount += obj.amount
#             if obj.cashFlow == 2:
#                 amount -= obj.amount

#     return amount



def basic_graph():

    x = np.arange(31)
    y = [0]*31

    uid = current_user.id
    for obj in Transactions.query.filter_by(userId = uid).all():
        if obj.date.month == today.month:
            y[obj.date.day] += obj.amount
    
    return x,y

    


