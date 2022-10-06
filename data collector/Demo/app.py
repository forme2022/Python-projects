from typing import Text

from sqlalchemy.sql.functions import count
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:911911@localhost:5433/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        #content=file.read()
        #print(content)
        file.save(secure_filename("upload"+file.filename))
        with open("upload"+file.filename,"a") as f:
            f.write("This was addded later")
        print(file)
        print(type(file))
        #print(email,height)
        #send_email(email,height,average_height)

        #print(db.session.query(Data).filter(Data.email_==email).count()) 
        
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    #pass
    return send_file("upload"+file.filename, attachment_filename='yourfile.csv', as_attachment=True)


if __name__ == "__main__":
    app.debug=True
    app.run()
