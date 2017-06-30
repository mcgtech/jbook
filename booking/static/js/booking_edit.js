$(function(){
    setup_datepickers();
});

function setup_datepickers()
{
    var options = get_basic_date_picker_options();

    $("#id_booking-from_date").datepicker(options);
    $("#id_booking-to_date").datepicker(options);
}