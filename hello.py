from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


def wrap(text):
    return f'<center><h1>{text}</h1></center></br>'

@app.route("/")
def home():
    return redirect(url_for('login'))


@app.route('/hello/<name>/')
def hello_world(name=None):
    status = "Visitor"
    if name.lower() == "kaydee":
        name = "KayDee"
        status = "Owner"
    return f'<center><h1>Hello {name}</h1></center></br><center><h2>Status : {status}</h2></center>'

    
@app.route('/login/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      password = request.form["pass"]
      if not user in database:
          return wrap("User not found")
      elif password == database[user]:
          
          return redirect(url_for('hello_world',name = user))
      else:
          return wrap("Access Denied")
   else:
      return render_template('login.html')


database={"kaydee":"kamikaze","aditi":"yo"}

if __name__ == '__main__':
    

   app.run(debug = True)