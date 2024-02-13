from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField, RadioField, IntegerField 
from wtforms import EmailField

class UserForm(Form):
    num1=IntegerField("num1")
    num2=IntegerField("num2")
    num3=IntegerField("num3")
    num4=IntegerField("num4")

class ResistenciaForm(Form):
    color1=SelectField(choices=[('Negro','Negro'),('Cafe', 'Cafe'),('Rojo','Rojo'),('Naranja','Naranja')
                                ,('Amarillo','Amarillo'),('Verde','Verde'),('Azul','Azul'),('Morado','Morado')
                                ,('Gris','Gris'),('Blanco','Blanco')])
    color2=SelectField(choices=[('Negro','Negro'),('Cafe', 'Cafe'),('Rojo','Rojo'),('Naranja','Naranja')
                                ,('Amarillo','Amarillo'),('Verde','Verde'),('Azul','Azul'),('Morado','Morado')
                                ,('Gris','Gris'),('Blanco','Blanco')])
    color3=SelectField(choices=[('Negro','Negro'),('Cafe', 'Cafe'),('Rojo','Rojo'),('Naranja','Naranja')
                                ,('Amarillo','Amarillo'),('Verde','Verde'),('Azul','Azul'),('Morado','Morado')
                                ,('Gris','Gris'),('Blanco','Blanco')])
    tolerancia=RadioField('Tolerancia',choices=[('Oro','Oro'),('Plata','Plata')])

        
    