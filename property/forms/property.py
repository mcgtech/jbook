from common.forms import *
from property.models import *
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab, Div

class PropertyForm(EditForm, AuditableForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
                TabHolder(
                    Tab('Main',
                        Div(Div('name', 'type', 'code', css_class="col-sm-6"), Div('short_description','description', css_class="col-sm-6"), css_class='row'),),
                    Tab('Booking Details',
                        Div(Div('start_day', css_class="col-sm-6"), Div('booking_rule', css_class="col-sm-6"), css_class='row'),),
                    Tab(
                        'Log',
                        'created_by',
                        'created_on',
                        'modified_by',
                        'modified_on'
                    )))
        self.prepare_required_field('name', 'Name')
        self.prepare_required_field('type', 'Type')
        self.prepare_required_field('code', 'Code')
        self.prepare_required_field('short_description', 'Short Description')
        self.prepare_required_field('description', 'Description')
        self.prepare_required_field('start_day', 'Start Day')
        self.prepare_required_field('booking_rule', 'Booking Rule')

    # if I make the following field required in the model, then as I am using tabs, the default form validation for
    # required fields in crispy forms for bootstrap shows a popover against the offending field when save is clicked
    # and if that tab is not on display then the user will not see the error, hence I took the following approach:
    # validate required fields and display error at field level
    def clean_name(self):
        return validate_required_field(self, 'name', 'name')

    def clean_type(self):
        return validate_required_field(self, 'type', 'type')

    def clean_code(self):
        return validate_required_field(self, 'code', 'code')

    def clean_short_description(self):
        return validate_required_field(self, 'short_description', 'short description')

    def clean_description(self):
        return validate_required_field(self, 'description', 'description')

    def clean_start_day(self):
        return validate_required_field(self, 'start_day', 'start day')

    def clean_booking_rule(self):
        return validate_required_field(self, 'booking_rule', 'booking rule')



    class Meta(AuditableForm.Meta):
        model = Property
        fields = get_auditable_fields() + ('type', 'name', 'code', 'start_day', 'booking_rule', 'short_description', 'description',)
