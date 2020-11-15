import os
from connect import db
from PIL import Image
from flask import url_for, current_app


def add_profile_pic(pic_upload, username, image_data):
    print("in add_profile_pic")
    new_filename = pic_upload.filename
    ext_type = new_filename.split('.')[-1]
    storage_filename = str(username)+'.'+ext_type
    storage_filename1 = str(username) #check
    image_data1 = image_data.split('.')[:-1] #check
    if image_data1 == storage_filename1:
        os.remove(os.path.join(current_app.root_path,'static\profile_pics', image_data))
        db.session.delete(image_data)
        db.session.commit()

    filepath = os.path.join(current_app.root_path,
                            'static\profile_pics', storage_filename) 
    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename