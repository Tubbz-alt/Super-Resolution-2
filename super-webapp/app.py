from flask import Flask
from flask import render_template
from flask import request
import os
import cv2
from src.predict import modcrop,shave,predict
from src.util import psnr,mse,compare_images,prepare_images
from PIL import Image
app=Flask(__name__)

'''
Specify the folder where you will keep the input image and where you
would want the output to be saved
'''
UPLOAD_FOLDER = '/Users/ammarpathan/Desktop/SuperResolution/Super-Resolution/super-webapp/static/input/'

OUTPUT_FOLDER = '/Users/ammarpathan/Desktop/SuperResolution/Super-Resolution/super-webapp/static/output/'

pred=0.0
@app.route("/",methods=['GET','POST'])
def upload_predict():
    if request.method == 'POST':
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(UPLOAD_FOLDER,image_file.filename)
            image_file.save(image_location)
            img=prepare_images(image_location,2)
            ref, degraded, output, scores=predict(img,image_file.filename)
            output_image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            output_image = Image.fromarray(output_image)
            output_location = os.path.join(OUTPUT_FOLDER,image_file.filename)

            output_image.save(output_location)
            return render_template('index.html',image_name=image_file.filename,psnr=scores[1][0],mse=scores[1][1],ssim=scores[1][2])
            
    return render_template('index.html',image_name=None,psnr=0,mse=0,ssim=0)

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)

