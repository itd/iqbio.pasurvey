jq(document).ready(function() {

    jq('#fieldset-0 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#fieldset-1 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#fieldset-2 label.horizontal').append(" <span class='req'>(required)</span>");

    // fieldset-3 is eco
    //jq('#fieldset-3 label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#formfield-form-widgets-ecofinancialaid label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#formfield-form-widgets-ecoundergradgpa label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#formfield-form-widgets-ecoundergradgpabio label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#formfield-form-widgets-ecocoursebio label.horizontal').append(" <span class='req'>(required)</span>");
    jq('#formfield-form-widgets-ecoresearchinterests label.horizontal').append(" <span class='req'>(required)</span>");

    // just need to supress one under chemical physics - fieldset-4
    jq('#fieldset-4 label.horizontal').append(" <span class='req'>(required)</span>");
    jq("div#formfield-form-widgets-chemphgre span.req").remove();
});
