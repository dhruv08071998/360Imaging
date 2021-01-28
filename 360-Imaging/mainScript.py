import os.path
from flask import Flask, jsonify, request, make_response, url_for, redirect, send_from_directory
import cv2
import os
from os import listdir
from os.path import isfile, join
from random import randint


UPLOAD_FOLDER = './upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/imageUploads/<int:id>', methods=['GET', 'POST'])
def upload_file(id):
    mainFile = str(id) + ".txt"
    if os.path.exists(mainFile) == True:
        f = open(mainFile, "r+")
        ids = f.read(5)
        if int(ids) != 0:
            if request.method == 'POST':
                if 'file1' not in request.files:
                    return 'there is no file1 in form!'
                file1 = request.files['file1']
                path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
                file1.save(path)
                totalImg = int(ids)
                totalImg = totalImg - 1
                f.seek(0)
                f.write(str(totalImg))
                f.truncate()
                tmp = {"status": True, "path": path, "title": totalImg}
                if totalImg == 0:
                    result = stichhingImg(id)
                    if result["status"]:
                        print("hiiiii")
                        os.remove(mainFile)
                        return jsonify(result)
                else:
                    return jsonify(tmp)

        elif int(ids) == 0:
            return jsonify({"msg":"limit is already reached"})

    else:
        result = {"status": False, "msg": "mentioned files not found"}
        return jsonify(result)

def stichhingImg(id):
    mainFolder = 'upload'
    path = mainFolder + '/'
    images = []
    myList = os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg, (0, 0), None, 0.2, 0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
        cv2.imwrite("static/result"+str(id)+".png", result)
        res = {"status": 1, "path": url_for('static',filename='result'+str(id)+'.png')}
        deleteFiles('upload')
    else:
        print('Panorama Generation Unsuccessful')
        res = {"status": 0}
    return res

@app.route('/totalNumber/<int:n>')

def declareNumberOfImages(n):
    val = randint(100,999)
    fileName = str(val)+".txt"
    file1 = open(fileName, "w")
    file1.write(str(n))
    result = {"status": True, "loc": fileName.split(".")[0]}
    return jsonify(result)

def deleteFiles(n):
    onlyfiles = [f for f in listdir(n) if isfile(join(n, f))]
    for file in onlyfiles:
        os.remove("upload/" + file)

if __name__ == '__main__':
    app.run(debug=True)