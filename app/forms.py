from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class addProperty(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedroom = StringField('Number of Bedrooms', validators=[DataRequired()])
    bathroom = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    propertyType= SelectField('Type', choices= ['House', 'Apartment'])
    description= TextAreaField('Description',validators=[DataRequired()])
    photo=FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])