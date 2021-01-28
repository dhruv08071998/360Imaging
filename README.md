# 360Imaging

## Getting Started

### Minimum Requirement

OpenCV library
Flask Library
Pycharm
Python 3.0

### Environment

* There is one build environment available.

1) 360-Imaging

### Software architectural pattern

Functional Oriented pattern

### Features
-  Stiching images through Image processing by openCV

## List of  Third parties 
* for Flask framework: https://github.com/pallets/flask
* for openCV: https://github.com/opencv/opencv


##  mainScript.py
 - Handled the total number of image we want to process.
 - Handle .txt and image file for image processing
 - Performed Stich function for generate 360 Image
 
 ##  static folder
  - This folder contain 360 image after processing.
  
 ##  upload folder
   - This folder contain images for processing. That is uploaded by phone.
   - after processing all images will be removed by script.
   
 ##  .txt file(e.g 312.txt)
   - This file handles total number of images.
   - This file updated after each image will be uploded to server.
   - After result generation file will be deleted by script.
   
# List of  APIs

 * /totalNumber/ (GET) - This api is used for informing server that how many images user want to process .
    e.g:  'http://127.0.0.1:5000/totalNumber/5'
 * /imageUploads/ (POST) - This api is used for uploading images to server. Along with that add a unique code that is received by previous API.
   e.g:   'http://127.0.0.1:5000/imageUploads/764'
 

## Authors and acknowledgment
Dhruv Upadhyay
