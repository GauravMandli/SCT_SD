from flask import Flask , render_template,request,session,redirect,url_for
print("Guess Game app running...")
import random

app=Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/",methods=["GET","POST"])

def index():

    if "number" not in session:
        session["number"]=random.randint(1,100)
        session["tries"]=0
    
    result=""

    if request.method=="POST":
        guess = request.form.get("guess")

        if guess:
            session["tries"] +=1
            guess = int(guess)
            secret=session["number"]

            if guess < secret:
                result = "Too low! Try again"

            elif guess > secret:
                result= "Too high! Try again"

            else:
                result = f"Correct ! You Gusse it {session['tries']} tries."
                session.pop("number")
                session.pop("tries")
    
    return render_template("index.html",result=result)

if __name__ == "__main__":
    app.run(debug=True) 