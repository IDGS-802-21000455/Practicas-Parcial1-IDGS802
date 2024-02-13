from flask import Flask, request, render_template
from math import sqrt
from flask_wtf import Form
from wtforms import SelectField, RadioField
import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('resistencia.html', form=forms.ResistenciaForm())

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

