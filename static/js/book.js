// Script for the BOOK functionality

// Implement datetimepicker 
$('input:eq(3)').datetimepicker({
    timepicker: true,
    datepicker: true,
    format: 'm/d/y H:i',
    value: '09:45',
    step: 15,
    yearStart: 2021,
    minDate:new Date(),
    minTime:'11:00',
    maxTime:'21:45',
});


