$(document).ready(function() {
    // Initialize date picker
    $('#id_date').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
        todayHighlight: true
    });
	// Increment and Decrement Hours
    $('#increment-hours').click(function(e){
        // Stop acting like a button
        e.preventDefault();
        // Get its current value
        var currentVal = parseInt($('#hoursWorked').val());
        // If is not undefined
        if (!isNaN(currentVal)) {
            // Increment
            $('#hoursWorked').val(currentVal + 1);
        } else {
            // Otherwise put a 0 there
            $('#hoursWorked').val(0);
        }
    });
    // This button will decrement the value till 0
    $(".decrement-hours").click(function(e) {
        // Stop acting like a button
        e.preventDefault();
        // Get its current value
        var currentVal = parseInt($('#hoursWorked').val());
        // If it isn't undefined or its greater than 0
        if (!isNaN(currentVal) && currentVal > 0) {
            // Decrement one
            $('#hoursWorked').val(currentVal - 1);
        } else {
            // Otherwise put a 0 there
            $('#hoursWorked').val(0);
        }
    });
});