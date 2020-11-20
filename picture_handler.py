import os
from connect import db
from PIL import Image
from flask import url_for, current_app
from random import randint


def add_profile_pic(pic_upload, username, image_data):
    print("in add_profile_pic")
    filename = pic_upload.filename
    ext_type = filename.split(".")[-1]
    storage_filename = str(username) + "_" + str(randint(0, 100)) + "." + ext_type
    # storage_filename1 = str(username)+ str(randint(0,100)) #check
    # image_data1 = image_data.split('.')[:-1] #check
    # print(*image_data1)
    # print(storage_filename1)

    # if image_data1 != 'default_profile':
    #     os.remove(os.path.join(current_app.root_path,'static\profile_pics', image_data))
    #     db.session.delete(image_data)
    #     db.session.commit()

    filepath = os.path.join(
        current_app.root_path, "static\profile_pics", storage_filename
    )
    output_size = (500, 500)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
