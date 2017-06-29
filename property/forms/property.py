from common.forms import *
from .property import *
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab

class PropertyForm(EditForm, AuditableForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
                TabHolder(
                    Tab('Main',
                        'type', 'name'),
                    Tab(
                        'Log',
                        'created_by',
                        'created_on',
                        'modified_by',
                        'modified_on'
                    )))


    class Meta(AuditableForm.Meta):
        model = Property
        fields = get_auditable_fields() + ('type', 'name',)
