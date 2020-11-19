from connect import db
from models import Transactions
from flask_login import current_user
from datetime import datetime
from sqlalchemy import func

today = datetime.today()



def xyfunc():
    x_axis = [
        "Miscellaneous",
        "Housing",
        "Transportation",
        "Food",
        "Utilities",
        "Insurance",
        "Medical & Healthcare",
        "Personal Spending",
        "Recreation & Entertainment",
    ]

    y_axis = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    uid = current_user.id
    for obj in Transactions.query.filter_by(userId=uid, cashFlow=2).all():
        if obj.date.year == today.year and obj.date.month == today.month:
            if obj.cat == x_axis[0]:
                y_axis[0] += obj.amount
            elif obj.cat == x_axis[1]:
                y_axis[1] += obj.amount
            elif obj.cat == x_axis[2]:
                y_axis[2] += obj.amount
            elif obj.cat == x_axis[3]:
                y_axis[3] += obj.amount
            elif obj.cat == x_axis[4]:
                y_axis[4] += obj.amount
            elif obj.cat == x_axis[5]:
                y_axis[5] += ojb.amount
            elif obj.cat == x_axis[6]:
                y_axis[6] += obj.amount
            elif obj.cat == x_axis[7]:
                y_axis[7] += obj.amount
            elif obj.cat == x_axis[8]:
                y_axis[8] += obj.amount
            else:
                continue

    return x_axis, y_axis
