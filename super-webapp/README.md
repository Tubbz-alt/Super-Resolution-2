# Super-Resolution Web App

This is a web-app using pre-trained SRCNN model. On giving an image as input, it reconstructs a higher resolution image of the same.
It currently only supports .bmp images, will try to add other formats in future

## Installation

### To run on locally:

<ul><li>Clone the repository</li>
    <li>Open the app.py file, in the folder.</li>
    <li>Change the 
        Location of Upload folder and output folder acc to your file system
    </li>
   <li>Install the requirements :
     
         pip3 install -r requirements.txt
</li>
   <li>To run the application:
    
           python3 app.py
   </li>
   </ul>

##### The model runs on pre-trained weights, taken from the following repo : https://github.com/MarkPrecursor/SRCNN-keras

##### The web app is heavily isnpired by : https://medium.com/towards-artificial-intelligence/building-a-super-resolution-image-web-app-57e26886cb45

# FUTURE TODOS

Adding other models to the fold and trying to give a full fledged web app deployed on a server
