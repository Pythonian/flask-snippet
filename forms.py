from models import Snippet


class SnippetForm(wtforms.Form):
    title = wtforms.StringField('Title',
                                validators=[DataRequired()])
    body = wtforms.TextAreaField('Body',
                                 validators=[DataRequired()])
    status = wtforms.SelectField(
        'Entry status',
        choices=(
            (Snippet.STATUS_PUBLIC, 'Public'),
            (Snippet.STATUS_DRAFT, 'Draft')),
        coerce=int)

    def save_entry(self, entry):
        self.populate_obj(entry)
        entry.generate_slug()
        return entry
