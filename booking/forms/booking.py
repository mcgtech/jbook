from common.forms import *
from booking.models import *
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab, Div

class PropertyForm(EditForm, AuditableForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
                TabHolder(
                    Tab('General',
                        'state',
                        Div(Div('property', 'from_date', 'to_date', css_class="col-sm-6"), Div('adults', 'children', 'infants', css_class="col-sm-6"), css_class='row'),),
                    Tab(
                        'Log',
                        'created_by',
                        'created_on',
                        'modified_by',
                        'modified_on'
                    )))
        self.prepare_required_field('property', 'Property')
        self.prepare_required_field('from_date', 'From')
        self.prepare_required_field('to_date', 'To')
        self.prepare_required_field('adults', 'Adults')
        self.fields['children'].required = False
        self.fields['infants'].required = False

    # if I make the following field required in the model, then as I am using tabs, the default form validation for
    # required fields in crispy forms for bootstrap shows a popover against the offending field when save is clicked
    # and if that tab is not on display then the user will not see the error, hence I took the following approach:
    # validate required fields and display error at field level
    def clean_property(self):
        return validate_required_field(self, 'property', 'property')

    def clean_from_date(self):
        return validate_required_field(self, 'from_date', 'from')

    def clean_to_date(self):
        return validate_required_field(self, 'to_date', 'to')

    def clean_adults(self):
        return validate_required_field(self, 'adults', 'adults')

    class Meta(AuditableForm.Meta):
        model = Booking
        fields = get_auditable_fields() + ('state', 'property', 'from_date', 'to_date', 'adults', 'children', 'infants',)
        AuditableForm.Meta.widgets['from_date'] = forms.DateInput(format=(settings.DISPLAY_DATE), attrs={'class':'datepicker'})
        AuditableForm.Meta.widgets['to_date'] = forms.DateInput(format=(settings.DISPLAY_DATE), attrs={'class':'datepicker'})
