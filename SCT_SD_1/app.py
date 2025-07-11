from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    result=""

    if request.method=="POST":
        temp = float(request.form["temperature"])
        unit = request.form["unit"]

        if unit == "select":
            result="Please Select Unit"  
            

        elif unit == "celsius":
            f= (temp *9/5)+32
            k=temp +273.15
            result =f"Fahrenheit: {f:.2f} °F | Kelvin: {k:.2f} k"
        
        elif unit =="fahrenheit":
            c=(temp -32) *5/9
            k=(temp-32)*5/9 +273.15
            result =f"Celsius: {c:.2f} °C | Kelvin: {k:.2f} k"

        elif unit =="kelvin":
            c=temp-273.15
            f=(temp-273.15) * 9/5 +32
            result =f"Celsius: {c:.2f} °C | Fahrenheit: {f:.2f} k"

    return render_template("index.html",result=result)

if __name__ == "__main__":
    app.run(debug=True)