from .models import Site

class VisitForm(Form):
    browser = fields.StringField()
    date = fields.DateField()
    event = fields.StringField()
    url = fields.StringField()
    ip_address = fields.StringField('IP Address')
    site = QuerySelectField(query_factory=lambda: Site.query.all())
