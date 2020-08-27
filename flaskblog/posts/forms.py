from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
