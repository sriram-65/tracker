from flask import Flask , Blueprint , request , redirect , jsonify , render_template , session
from admin.tools import Check_Password


Use = Blueprint("User" , __name__)

@Use.route("/" , methods=['POST' , 'GET'])
def User():
    try:
        if request.method=='POST':
             password = request.form.get("password")
             res = Check_Password(password)
             if res!=True:
                 return render_template("index.html" , er="Invalid")
             session['Authenticated'] = True
             return redirect("/")
        
        if session.get("Authenticated"):
                return render_template("index.html" , isverifed=True)
        else:
                return render_template("index.html" , isverifed=False)

    except:
        return "Server Error" , 500
    

@Use.route('/logout')
def Logout():
     session.clear()
     return redirect('/')
