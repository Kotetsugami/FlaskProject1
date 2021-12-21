from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from FlaskProjectPackage.models import News


class CreateNews(FlaskForm):
    def validate_title(self, title_to_check):
        news = News.query.filter_by(title=title_to_check.data).first()
        if news:
            raise ValidationError('Title already exists!')
        else:
            return True

    def validate_desc(self, desc_to_check):
        news = News.query.filter_by(description=desc_to_check.data).first()
        if news:
            raise ValidationError('Description already exists!')
        else:
            return True

    title = StringField(label='Title:', validators=[Length(min=2, max=60), DataRequired()])
    description = StringField(label="Description:", validators=[Length(min=2, max=8096), DataRequired()])
    category = StringField(label="Category:", validators=[Length(min=2, max=30), DataRequired()])
    author = StringField(label="Author:", validators=[Length(min=2, max=60), DataRequired()])
    submit = SubmitField(label="Create News")


class DeleteNews(FlaskForm):
    def validate_title(self, title_to_check):
        news = News.query.filter_by(title=title_to_check.data).first()
        if not news:
            raise ValidationError('Title does not exist!')

    title = StringField(label='Title:', validators=[Length(min=2, max=60), DataRequired()])
    submit = SubmitField(label="Delete News")


class ChangeNews(FlaskForm):
    def validate_title(self, title_to_check):
        news = News.query.filter_by(title=title_to_check.data).first()
        if not news:
            raise ValidationError('Title does not exist!')

    title = StringField(label='Title:', validators=[Length(min=2, max=60), DataRequired()])
    description = StringField(label="Description:", validators=[Length(min=2, max=8096), DataRequired()])
    submit = SubmitField(label="Change News")


class GetNews(FlaskForm):
    def validate_title(self, title_to_check):
        news = News.query.filter_by(title=title_to_check.data).first()
        if not news:
            raise ValidationError('Title does not exist!')

    title = StringField(label='Title:', validators=[Length(min=2, max=60), DataRequired()])
    submit = SubmitField(label="Get News")