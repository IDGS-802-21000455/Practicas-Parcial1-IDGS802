from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('formulario.html')


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    resultado = None  # Inicializa resultado con un valor predeterminado
    
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        
        # Obtener la opción seleccionada del radio button
        opcion = request.form.get("radioOption")

        # Realizar la operación adecuada según la opción seleccionada
        if opcion == "suma":
            resultado = num1 + num2
        elif opcion == "resta":
            resultado = num1 - num2
        elif opcion == "multi":
            resultado = num1 * num2
        elif opcion == "div":
            resultado = num1 / num2

    return render_template("formulario.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)