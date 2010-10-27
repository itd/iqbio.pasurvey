/*  javascript for show/hide fields based on dropdown selected */

$(document).ready(function() {

    $.Biochemistry_fields = '#formfield-form-widgets-biochem_research_interests, \
                            #formfield-form-widgets-biochemteachingexperience, \
                            #formfield-form-widgets-biochemresearchexperience';
    $.ChemBioEngineering_fields = '#formfield-form-widgets-bioengfellowshipsupport, \
                                   #formfield-form-widgets-bioengresearchinterests, \
                                   #formfield-form-widgets-bioengducationalgoals';
    $.ComputerScience_fields = '#formfield-form-widgets-csinterests, \
                                #formfield-form-widgets-csfinancialaid';
    $.Ecology_fields = '#formfield-form-widgets-ecofinancialaid, \
                        #formfield-form-widgets-ecoundergradgpa, \
                        #formfield-form-widgets-ecoundergradgpabio, \
                        #formfield-form-widgets-ecogradgpa, \
                        #formfield-form-widgets-ecogradgpabio, \
                        #formfield-form-widgets-ecogre, \
                        #formfield-form-widgets-ecocoursebio, \
                        #formfield-form-widgets-ecocoursechem, \
                        #formfield-form-widgets-ecocoursemath, \
                        #formfield-form-widgets-ecocoursephysics, \
                        #formfield-form-widgets-ecocourseother, \
                        #formfield-form-widgets-ecoresearchinterests, \
                        #formfield-form-widgets-ecofaculty, \
                        #formfield-form-widgets-ecopublications';
    $.ChemicalPhysics_fields = '#formfield-form-widgets-chemphresearchinterests, \
                                #formfield-form-widgets-chemphexperimental, \
                                #formfield-form-widgets-chemphgpaphysics, \
                                #formfield-form-widgets-chemphgpamath, \
                                #formfield-form-widgets-chemphgpacombined, \
                                #formfield-form-widgets-chemphgpaoverall, \
                                #formfield-form-widgets-chemphgre';

    // hide all fields onload
    $.allFields = [$($.Biochemistry_fields),
                   $($.ChemBioEngineering_fields),
                   $($.ComputerScience_fields),
                   $($.Ecology_fields),
                   $($.ChemicalPhysics_fields)];
    $.each($.allFields, function() { this.css('display', 'none'); });

    $.viewMap = {'Biochemistry': $($.Biochemistry_fields),
                 'ChemBioEngineering': $($.ChemBioEngineering_fields),
                 'ComputerScience': $($.ComputerScience_fields),
                 'Ecology': $($.Ecology_fields),
                 'ChemicalPhysics': $($.ChemicalPhysics_fields)};
    // show by default/stored values (especially in EditForm)
    try {
        $.viewMap[$('#form-widgets-degreeprogram2').val()].show();
    } catch(err) {}
    try {
        $.viewMap[$('#form-widgets-degreeprogram3').val()].show();
    } catch(err) {}
    // onchange event
    $('#form-widgets-degreeprogram2, #form-widgets-degreeprogram3').change(function() {
        // hide all
        $.each($.viewMap, function() { this.hide(); });
        // show fields that matched values selected in degreeprogram2 and degreeprogram3
        try {
            $.viewMap[$('#form-widgets-degreeprogram2').val()].show();
        } catch(err) {
            //alert(err.toString());
        }
        $.viewMap[$('#form-widgets-degreeprogram3').val()].show();
    });
});

