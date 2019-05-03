from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')


class BlogFormI(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    pitch = TextAreaField('Blog Content:', validators=[Required()], render_kw={
                          'class': 'form-control', 'rows': 15})
    submit = SubmitField('Submit')


class EmailFormI(FlaskForm):
    email = StringField('Enter your email', validators=[Required(), Email()])
    subscribe = SubmitField('Subscribe')
