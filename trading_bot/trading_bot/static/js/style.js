$(document).ready(function() {
    // Function to handle dropdown change event
    $('#id_limit_stop_values').on('change', function() {
        var selectedValue = $(this).val();

        // Show/hide divs based on selected value
        if (selectedValue === 'limit') {
            $('#stock-market-id').hide();
            $('#stop-loss-id').hide();
            $('#limit-price-stock').show();
        } else if (selectedValue === 'stop_loss') {
            $('#stock-market-id').hide();
            $('#stop-loss-id').show();
            $('#limit-price-stock').hide();
        } else if (selectedValue === 'market') {
            $('#stock-market-id').show();
            $('#limit-price-stock').hide();
            $('#stop-loss-id').hide();
        } else if (selectedValue === 'stop_loss') {
            $('#stop-loss-id').Show();
            $('#stock-market-id').hide();
            $('#limit-price-stock').hide();
            
        }
        // else {
        //     $('#stock-market-id').hide();
        //     $('#stop-loss-id').hide();
        //     $('#limit-price-stock').show();
        //     $('#stop-loss-id').hide();
        // }
    });

    // Trigger change event on page load (if needed)
    // $('#id_limit_stop_values').trigger('change');
});


function doNotRefereshPageOnSubmission() {
    var form = document.getElementById('market_form_submission');
    form.addEventListener("submit", function(e) {
        e.preventDefault(); // Prevent default form submission behavior
        // Optionally, perform additional actions on form submission
        // For example, you can fetch form data and make an AJAX request
    });
}