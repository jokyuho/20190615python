from flask import Flask, render_template, request, redirect
import db, urllib.request, comment, lionking
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.route('/insertform')
def insertform():
    return render_template('customer.html')

@app.route('/insert', methods=['POST'])
def insert_user():
    user = request.form.to_dict()
    print(list(user.values()))
    db.insert_users(list(user.values()))
    return redirect('/list')

@app.route('/list')
def list_user():
    users=db.all_users()
    return render_template('list.html',users=users)

@app.route('/content/<userid>')
def content_user(userid):
    user=db.one_user(userid)
    return render_template('content.html',user=user)

@app.route('/delete/<userid>')
def delete_user(userid):
    db.delete_user(userid)
    return redirect('/list')

@app.route('/updateform/<userid>')
def updateform(userid):
    user=db.one_user(userid)
    return render_template('updateform.html',user=user)

@app.route('/update',methods=['POST'])
def update_user():
    user = request.form.to_dict()
    print(user)
    db.update_user(user)
    return redirect('/list')

@app.route('/secondpage1.html')
def second1():
      return render_template('secondpage1.html')

@app.route('/secondpage2.html')
def second2():
      return render_template('secondpage2.html')

@app.route('/secondpage3.html')
def second3():
      return render_template('secondpage3.html')

@app.route('/usercomment')
def list_usercomment():
    comment.commentmade()
    items=db.users_comment()
    return render_template('usercomment.html',items=items)

if __name__ == '__main__':
    app.run(debug=True)