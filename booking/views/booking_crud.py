from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from common.views import *
from common.forms import *
from collections import namedtuple
from booking.models import *
from booking.forms import *
import json

@login_required
@user_passes_test(back_office_user, 'jbook_login')
def booking_new(request):
    return manage_booking(request, None)


@login_required
@user_passes_test(back_office_user, 'jbook_login')
def booking_edit(request, pk):
    return manage_booking(request, pk)


# http://stackoverflow.com/questions/29758558/inlineformset-factory-create-new-objects-and-edit-objects-after-created
# https://gist.github.com/ibarovic/3092910
@transaction.atomic
def manage_booking(request, booking_id=None):
    js_dict = {}
    del_request = None
    config = get_form_edit_config(booking_id, None, Booking, request, 'booking_search')

    if booking_id is not None:
        del_msg = 'You have successfully deleted the ' + config.class_name + ' ' + str(config.primary_entity)
        del_request = handle_delete_request(request, config, '/booking_search', del_msg)
    if del_request is not None:
        return del_request
    elif request.method == "POST":
        primary_entity_form = PropertyForm(request.POST, request.FILES, instance=config.primary_entity, prefix=config.class_name,
                                           is_edit_form=config.is_edit_form, cancel_url=config.cancel_url, save_text=config.save_text)
        if primary_entity_form.is_valid():
            created_primary_entity = primary_entity_form.save(commit=False)
            apply_auditable_info(created_primary_entity, request)
            created_primary_entity.save()
            action = get_form_edit_url(None, created_primary_entity.id, config.class_name)
            return redirect(action)
    else:
        primary_entity_form = PropertyForm(instance=config.primary_entity, prefix=config.class_name, is_edit_form=config.is_edit_form,
                                           cancel_url=config.cancel_url, save_text=config.save_text)

    if anonymous_user(request.user) == False and booking_id is None:
        add_msg = 'Adding a new ' + config.class_name
        msg_once_only(request, add_msg, settings.WARN_MSG_TYPE)


    primary_entity_form_errors = form_errors_as_array(primary_entity_form)
    form_errors = primary_entity_form_errors
    set_deletion_status_in_js_data(js_dict, request.user, admin_user)
    js_dict['show_log'] = show_log(request)
    set_deletion_status_in_js_data(js_dict, request.user, back_office_user)
    js_data = json.dumps(js_dict)

    return render(request, 'booking_edit.html', {'form': primary_entity_form,
                                                           'js_data' : js_data,
                                                           'config' : config,
                                                           'form_errors': form_errors,})

def show_log(request):
    return request is None or (anonymous_user(request.user) == False and back_office_user(request.user) == False)
