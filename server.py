from flask import Flask, request, Response
import sys
import json
import os
app = Flask(__name__)

@app.route("/save_image", methods = ['POST'])
def save_image():
    if request.method == 'POST':
        photo = request.files["photo"]
        folder = request.form["description"]

        if not os.path.exists(folder):
            os.makedirs(folder)
            photo.save("./"+folder+"/1.jpg")
        else:
            count = len(os.listdir(folder)) + 1
            photo.save("./"+folder+"/"+str(count)+".jpg")
            
        
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)