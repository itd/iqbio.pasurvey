from five import grok
from zope import schema
from zope.schema import Text, TextLine, Choice, Bool, Datetime, Date
from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from zope.event import notify

from zope.app.container.interfaces import IObjectAddedEvent
from Products.CMFCore.utils import getToolByName

from z3c.form.browser import checkbox
from z3c.form.browser.textlines import TextLinesFieldWidget

from iqbio.pasurvey import _


#import iqbio.pasurvey.vocabularies
from iqbio.pasurvey.vocabularies import biochem_research_interests_vocab, comp_sci_financial_aid_vocab
from iqbio.pasurvey.vocabularies import facultyofinterest_vocab, degreeprograms_vocab, yes_no_vocab
from iqbio.pasurvey.vocabularies import bio_chem_vocab, comp_sci_vocab, chem_bio_vocab


class IPasurvey(form.Schema):
    """
    The schema for the survey form
    """
    fname = TextLine(
            title=_(u"First Name"),
            description=_(u"Your legal first name"),
        )
    mname = TextLine(
            title=_(u"Middle Name or Initial"),
            description=_(u""),
        )
    lname = TextLine(
            title=_(u"Last Name / Sir Name"),
            description=_(u"Your legal last name"),
        )
    dob = Date(
            title=_(u"Date of birth"),
            description=_(u""),
        )

    email = TextLine(
            title=_(u"Email"),
            description=_(u"A valid email address where you can be reached."),
        )


    facultyofinterest  = Choice(
        title=_(u"Faculty of interest"),
        description=_(u"Optional: Please indicate up to five faculty whose research interests you."),
        vocabulary = facultyofinterest_vocab,
        required=False,
        )

    facultyofinterestother = TextLine(
        title = _u("Faculty of Interest (other)"),
        description = _(u"If you did not see the faculty you were interested in on the list, please write their name in here."),
        required=False,
        )

    degreeprogram1 = Choice(
        title=_(u"First degree program of interest"),
        description=_(u"Remember this degree program. You will formally fill out the application on CU's Graduate School Application website for this degree program. The options are presented in the drop down menu (with their associated colleges)."),
        vocabulary = degreeprograms_vocab,
        required=True,
      )
    degreeprogram2 = Choice(
        title=_(u"Second degree program of interest"),
        description=_(u""),
        vocabulary = degreeprograms_vocab,
        required=True,
       )
    degreeprogram3 = Choice(
        title=_(u"Third degree program of interest"),
        description=_(u""),
        vocabulary = degreeprograms_vocab,
        required=True,
       )

    alsoapply = Choice(
        title = _u("Apply to Department Also"),
        description = _(u"If you are not accepted by the IQ Biology program, would you like to be considered independently by one or more of your Degree Programs of Interest for admission directly to their program?"),
        vocabulary = [u'Yes',u'No'],
        )

    degreeprograms = Choice(
        title = _u("Which Degree Programs?"),
        description = _(u"If so, please indicate which degree programs you would like your application considered by (up to three)."),
        vocabulary = degreeprograms_vocab,
        required=False,
        )

    # ---------- conditional questions if "Biochemistry" is selected ---------
    biochem_research_interests = Choice(
        title = _u("Biochemistry Research Interests"),
        description = _(u"Please check off as many of the research areas as interests you."),
        vocabulary = biochem_research_interests_vocab,
        required=False,
        )

    biochemteachingexperience = Text(
        title = _u("Teaching Experience"),
        description = _(u"Please list all previous teaching experience including the subject, start date, end date, and institution."),
        )

    biochemresearchexperience = Text(
            title=_(u"Research Experience"),
            description=_(u"Please list all previous research experience including the project name/short description, start date, end date, and institution/company."),
        )

    # ---------- conditional questions if "ChemBioEngineering" is selected ---------
    form.widget(bioengfellowshipsupport=CheckBoxField)
    bioengfellowshipsupport = Bool(
        title = _(u"Fellowship Support"),
        description = _(u"Have you applied for or do you have any other fellowship support? (check for 'yes')"),
        required = False,
        )

    bioengresearchinterests = Choice(
        title = _(u"Research Interests"),
        description = _(u"Check multiple boxes (up to three):"),
        required=False,
        vocabulary = chem_bio_vocab,
        )

    bioengducationalgoals = Text(
        title = _(u"Educational Goals"),
        description = _(u"write in - 2,000 characters max"),
        required = False,
        min_length = None,
        max_length = 2000,
        )

    # ---------- conditional questions if "ComputerScience" is selected ---------

    form.widget(csinterests=CheckBoxFieldWidget)
    csinterests = Choice(
        title = _(u"Your Interests"),
        description = _(u"Which areas represented at the University of Colorado are you interested in? Please pick up to three areas."),
        required=False,
        vocabulary = comp_sci_vocab,
        )
    csfinancialaid = Choice(
        title = _(u"Financial Aid (select one)"),
        description = _(u"Indicate your need for financial aid (Students accepted to the IQ Biology program will have two years of funding through the IQ Biology program guaranteed)."),
        required = False,
        vocabulary = comp_sci_financial_aid_vocab,
        )


    # ---------- conditional questions if "Ecology" is selected ---------

    ecofinancialaid = Choice(
        title = _(u"Financial Aid"),
        description = _(u"Will you be requesting a financial support in the form of a fellowship teaching assistantship or research assistantship beyond what is provided for IQ Biology students? (Students accepted to the IQ Biology program will have two years of funding through the IQ Biology program guaranteed)."),
        required = False,
        vocabulary = yes_no_vocab,
        )

    ecoundergradgpa = TextLine(
        title = _(u"Undergraduate GPA (overall)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0. (up to 1 decimal place.)"),
        required = False,
        )
    ecoundergradgpabio = TextLine(
        title = _(u"Undergraduate GPA: biological science courses only"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0. (up to 1 decimal place.)"),
        required = False,
        )


    ecogradgpa = TextLine(
        title = _(u"Overall Graduate GPA (optional)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0.  If you have not yet taken any graduate level courses, leave this question blank."),
        required = False,
        )
    ecogradgpabio = TextLine(
        title = _(u"Graduate GPA: biological science courses only (optional)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0.  If you have not yet taken any graduate level courses, leave this question blank."),
        required = False,
        )

    ecogre = TextLine(
        title = _(u"GRE Score: Biology Subject Exam (optional)"),
        description = _(u"If you have taken a Biology Subject Exam please write in the name of the exam, your raw score, your percentile, and the month and year (MM/YY) you took the test."),
        required = False,
        )


    ecocoursebio = Text(
        title = _(u"Biology Courses"),
        description = _(u"Please list the names of biology courses you have taken (and your grade in each course). "),
        required = False,
        )


    ecocoursechem = Text(
        title = _(u"Chemistry Courses"),
        description = _(u"Please list the names of chemistry courses you have taken (and your grade in each course). "),
        required = False,
        )


    ecocoursemath = Text(
        title = _(u"Math and Statistics Courses"),
        description = _(u"Please list the names of math and statistics courses you have taken (and your grade in each course). "),
        required = False,
        )

    ecocoursephysics = Text(
        title = _(u"Physics Courses"),
        description = _(u"Please list the names of physics courses you have taken (and your grade in each course). "),
        required = False,
        )


    ecocourseother = Text(
        title = _(u"Other Sciences and Relevant Courses"),
        description = _(u"Please list the names of other science and relevant courses you have taken and your grade in each course. "),
        required = False,
        )


    ecoresearchinterests = Text(
        title = _(u"Research Interests"),
        description = _(u"In what area or areas of biology would you like to work? Is there any specific topic or group of organisms with which you are most interested? (1-2 paragraphs)"),
        required = False,
        )


    ecofaculty = Text(
        title = _(u"Faculty"),
        description = _(u"Have you made contact with any Ecology or Evolutionary Biology Faculty? Whose research interests you? Please list names of a few faculty."),
        required = False,
        )


    ecopublications = Text(
        title = _(u"Publications"),
        description = _(u"Please list the complete citations of any scientific publication that you have authored."),
        required = False,
        )

    #----- if ChemicalPhysics is chosen ----------------------------

    chemphresearchinterests  = Text(
        title = _(u"Research Interests"),
        description = _(u"Please write in a few phrases that describe your area(s) of interest or specialization."),
        required = False,
        )

    form.widget(chemphexperimental=CheckBoxFieldWidget)
    chemphexperimental = Choice(
        title = _(u"Research Interests: Experimental or Theoretical"),
        description = _(u"Check one or both boxes depending on your interests."),
        required=False,
        vocabulary = exp_or_theoretical_vocab,
        )

    chemphgpaphysics = TextLine(
        title = _(u"Undergraduate GPA: Physics courses only"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        )

    chemphgpamath = TextLine(
        title = _(u"Undergraduate GPA: Math courses only"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        )

    chemphgpacombined = TextLine(
        title = _(u"Undergraduate GPA: Combined math and physics courses "),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        )

    chemphgpaoverall = TextLine(
        title = _(u"Undergraduate GPA: overall (all courses)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        )

    chemphgre = Text(
        title = _(u"GRE SCore: Physics Subject Exam (optional)"),
        description = _(u"If you have taken a Physics Subject Exam please write in the name of the exam, your raw score, your percentile, and the month and year (MM/YY) you took the test."),
        required = False,
        min_length = None,
        max_length = None,
        )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # The following fields are for the various departments to     #
    # comment and accept/notaccept an applicant                   #


    #-- prefix the following with each dept's identifier ------------
#    accepted = Choice(
#        title = _(u"Accepted?"),
#        description = _(u"Would you accept this person into your program?"),
#        required=False,
#        vocabulary = yes_no_vocab,
#        )
#
#    acceptancedate = Datetime(
#        title = _(u"Acceptance Date"),
#        description = _(u"If this person might be accepted into your program, please enter the date and time of this conditional determination."),
#        required = False,
#        )
#
#    notaccepteddate = Datetime(
#        title = _(u"Not Accepted Date"),
#        description = _(u"If this person WILL NOT be accepted into your program, please enter the date and time of this determination."),
#        required = False,
#        )
#
#    comments = TextLine(
#        title = _(u"PROGRAM Comments"),
#        description = _(u"Please optionally enter any comments supporting your Acceptance or Not Acceptance decision."),
#        required = False,
#        )


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # The following fields are for the overall management of the process  #



class View(grok.View):
    grok.context(IPasurvey)
    grok.require('zope2.View')
