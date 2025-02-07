import os
from main import app

def get_image(id):
    for image_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in image_name:
            return image_name

    return 'missingno.jpg'

def remove_image(id):
    image = get_image(id)
    print(image)
    if image != "missingno.jpg":
        os.remove(os.path.join(app.config['UPLOAD_PATH'], image))
