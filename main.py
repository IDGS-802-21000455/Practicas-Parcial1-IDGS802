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



resistencia_colores = {
    'Negro': 0,
    'Cafe': 1,
    'Rojo': 2,
    'Naranja': 3,
    'Amarillo': 4,
    'Verde': 5,
    'Azul': 6,
    'Morado': 7,
    'Gris': 8,
    'Blanco': 9
}

tolerancia_colores = {
    'Oro': 5,
    'Plata': 10
}

def calcular_ResistenciaValor(color1, color2, color3):
    valor = (resistencia_colores[color1] * 10 + resistencia_colores[color2]) * 10 ** resistencia_colores[color3]
    return valor


def calcular_Tolerancia(tolerancia):
    return tolerancia_colores[tolerancia]

@app.route("/resistencia", methods=["GET", "POST"])
def resistencia():
    resistencia_form = forms.ResistenciaForm(request.form)
    resultado_resistencia = 0
    minvalor = 0
    maxvalor = 0
    color_codes = {
        'negro': '#000000',
        'cafe': '#8B4513',
        'rojo': '#FF0000',
        'naranja': '#FFA500',
        'amarillo': '#FFFF00',
        'verde': '#008000',
        'azul': '#0000FF',
        'morado': '#800080',
        'gris': '#808080',
        'blanco': '#FFFFFF',
        'oro': '#FFD700',  
        'plata': '#C0C0C0' 
    }

    color_resistencia = '' 
    porcentaje_tolerancia = 0  

    if request.method == 'POST' and resistencia_form.validate():
        color1 = resistencia_form.color1.data
        color2 = resistencia_form.color2.data
        color3 = resistencia_form.color3.data
        color_tolerancia = resistencia_form.tolerancia.data

        resultado_resistencia = calcular_ResistenciaValor(color1, color2, color3)
        tolerancia = calcular_Tolerancia(color_tolerancia)

        minvalor = resultado_resistencia * (1 - tolerancia / 100)
        maxvalor = resultado_resistencia * (1 + tolerancia / 100)

    
        porcentaje_tolerancia = tolerancia  

        if color_tolerancia == 'Oro':
            color_resistencia = 'Oro'
        elif color_tolerancia == 'Plata':
            color_resistencia = 'Plata'
        else:
            color_resistencia = 'Sin definir'  

        print(color1, color2, color3)
        print(f'Resultado Resistencia: {resultado_resistencia} ohms')
        print(f'Min Valor: {minvalor} ohms')
        print(f'Max Valor: {maxvalor} ohms')

    return render_template(
        'resistencia.html',
        form=resistencia_form,
        resultado_resistencia=resultado_resistencia,
        minvalor=minvalor,
        maxvalor=maxvalor,
        color_codes=color_codes,
        color_resistencia=color_resistencia,
        porcentaje_tolerancia=porcentaje_tolerancia  
    )


if __name__ == "__main__":
    app.run(debug=True)
    
