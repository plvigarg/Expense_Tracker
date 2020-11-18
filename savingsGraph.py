from connect import db
from models import Transactions
from flask_login import current_user
from datetime import datetime
from sqlalchemy import func
import numpy as np

today = datetime.today()

def expenditure(mydate):
    amount = 0
    uid = current_user.id
    for obj in Transactions.query.filter_by(userId = uid).all():
        if obj.date.year == today.year and obj.date.month == mydate:
            if obj.cashFlow == 2:
                amount += obj.amount

    return amount





def savings():

    month = today.month
    # if today.month == 1:
    #     def bug():
    #        array = [0]*12
    #        return array

    #     budget_array = bug()


    # budget_array[month] = current_user.budget

    # budget = current_user.budget

    x = np.arange(12)
    y = [0]*12

    for xi in x:
        y[xi] = current_user.budget - expenditure(xi)
    
    return x,y