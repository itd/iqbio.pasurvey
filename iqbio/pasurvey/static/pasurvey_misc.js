jq(document).ready(function() {
    // Tried doing something cool. Gave up.
    var fsList = ['#fieldset-0 label.horizontal',
        '#fieldset-1 label.horizontal',
        '#fieldset-2 label.horizontal',
        '#fieldset-3 label.horizontal',
        '#fieldset-4 label.horizontal'];

    jq('#fieldset-0 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#fieldset-1 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#fieldset-2 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#fieldset-3 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#fieldset-4 label.horizontal').append(" <span class='req'>(required)</span>");
});
