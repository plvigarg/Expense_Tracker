from connect import db
from models import Transactions
from flask_login import current_user
from datetime import datetime
from sqlalchemy import func
import numpy as np

today = datetime.today()

def totalBal():

    amount = 0
    uid = current_user.id
    for obj in Transactions.query.filter_by(userId = uid).all():
        if obj.cashFlow == 2:
            amount -= obj.amount
        if obj.cashFlow == 1:
            amount += obj.amount

    return amount


def leftBal():

    amount = 0
    budget = current_user.budget
    uid = current_user.id
    for obj in Transactions.query.filter_by(userId = uid).all():
        if obj.date.month == today.month:
            if obj.cashFlow == 2:
                amount += obj.amount

    return (budget - amount)