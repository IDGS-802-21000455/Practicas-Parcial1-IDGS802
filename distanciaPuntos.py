from flask import Flask,request,render_template
from math import sqrt
import forms


app=Flask(__name__)

@app.route("/")
def index():
    return render_template('distancia.html', form=forms.UserForm())

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    distancia_form = forms.UserForm(request.form)
    res = 0

    if request.method == 'POST' and distancia_form.validate():
        x1 = distancia_form.num1.data
        y1 = distancia_form.num2.data
        x2 = distancia_form.num3.data
        y2 = distancia_form.num4.data

       
        distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

        
        res = distancia

        return render_template('distancia.html', form=distancia_form, res=res)

    return render_template('distancia.html', form=distancia_form, res=res)

if __name__ == "__main__":
    app.run(debug=True)