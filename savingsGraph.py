from connect import db
from models import Transactions, Users
from flask_login import current_user
from datetime import datetime
from sqlalchemy import func
import numpy as np

today = datetime.today()


def expenditure(mydate):
    if mydate == 0:
        mydate = 12

    amount = 0
    uid = current_user.id
    for obj in Transactions.query.filter_by(userId=uid).all():
        if obj.date.year == today.year and obj.date.month == mydate:
            if obj.cashFlow == 2:
                amount += obj.amount

    return amount


def expenditure2(mydate):
    if mydate == 0:
        mydate = 12

    amount = 0
    uid = current_user.id
    for obj in Transactions.query.filter_by(userId=uid).all():
        if obj.date.year == today.year and obj.date.month <= mydate:
            if obj.cashFlow == 2:
                amount += obj.amount

    return amount


def savings():

    month = today.month

    x = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    y = [0] * 12

    for idx, xi in enumerate(x):
        y[idx] = current_user.budget - expenditure(idx + 1)

    return x, y


def savings2():

    month = today.month

    x = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    y = [0] * 12

    for idx, xi in enumerate(x):
        # saved = current_user.budget - expenditure(idx)
        y[idx] = current_user.budget * (idx + 1) - expenditure2(idx + 1)

    return x, y

