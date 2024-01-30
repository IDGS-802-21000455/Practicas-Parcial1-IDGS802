from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField, RadioField, IntegerField
from wtforms import EmailField

class UserForm(Form):
    num1=IntegerField("num1")
    num2=IntegerField("num2")
    num3=IntegerField("num3")
    num4=IntegerField("num4")
    
    