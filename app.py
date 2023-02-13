from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"

db=SQLAlchemy(app)

class Todo(db.Model):
    sno =db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    
    
   
@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
       title=request.form['title']
       desc=request.form['desc']
       todo=Todo(title=title,desc=desc)
       db.session.add(todo)
       db.session.commit()
       
    alltodos=Todo.query.all()
    return render_template("index.html",alltodos=alltodos)




if __name__ == "__main__":
    app.run(debug=True , port=8000)