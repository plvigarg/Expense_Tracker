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
        if obj.date.year == today.year and obj.date.month == today.month and obj.date.day <= mydate:
            if obj.cashFlow == 2:
                amount += obj.amount

    return amount



def basic_graph():

    x = np.arange(31)
    y = [0]*31

    uid = current_user.id
    for obj in Transactions.query.filter_by(userId = uid).all():
        if obj.date.year == today.year and obj.date.month == today.month and obj.cashFlow == 2:
            y[obj.date.day] += obj.amount
    
    return x,y


def basic_graph2():

    x = np.arange(31)
    y = [0]*31

    for xi in x:
        y[xi] = expenditure(xi)
    
    return x,y

    


