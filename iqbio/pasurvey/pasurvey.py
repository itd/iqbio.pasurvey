from datetime import datetime
from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter

from plone.app.content.interfaces import INameFromTitle
from zope.interface import implements

from zope import schema
from zope.schema import Text, TextLine, Choice, Bool, Datetime, Date, List, Float, Int
from zope.schema.interfaces import RequiredMissing
from plone.directives import form
from plone.directives import dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from zope.event import notify

from zope.app.container.interfaces import IObjectAddedEvent
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

from z3c.form.interfaces import IAddForm, IEditForm, IDisplayForm, HIDDEN_MODE
from z3c.form.browser.checkbox import CheckBoxFieldWidget, CheckBoxWidget, SingleCheckBoxFieldWidget
from z3c.form.browser.textlines import TextLinesFieldWidget

from z3c.relationfield.schema import RelationList, RelationChoice, List
from plone.formwidget.contenttree import ObjPathSourceBinder

from z3c.form import button, form as z3cform

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary

from iqbio.pasurvey import _

#import iqbio.pasurvey.vocabularies
from iqbio.pasurvey.vocabularies import biochem_research_interests_vocab, comp_sci_financial_aid_vocab
from iqbio.pasurvey.vocabularies import facultyofinterest_vocab, degreeprograms_vocab, yes_no_vocab
from iqbio.pasurvey.vocabularies import bio_chem_vocab, comp_sci_vocab, chem_bio_vocab, exp_or_theoretical_vocab
from iqbio.pasurvey.vocabularies import degreeprograms_lite_vocab
from iqbio.pasurvey.validators import validate_email, validate_decimal


def choiceVocabConstraint(value):
    """Check that the value selected is not blank
    """
    if value is None:
        raise Invalid(_(u"Selecting a First and Second Degree Program is required."))
    return True


class IPasurvey(form.Schema):
    """
    The schema for the survey form
    """

    fname = schema.TextLine(
            title=_(u"First Name"),
            description=_(u"Your legal first name"),
            required = True,
        )
    mname = schema.TextLine(
            title=_(u"Middle Name or Initial"),
            description=_(u""),
            required = False,
        )
    lname = schema.TextLine(
            title=_(u"Last Name / Sir Name"),
            description=_(u"Your legal last name"),
            required = True,
        )
    dob = Date(
            title=_(u"Date of birth"),
            description=_(u""),
        )

    email = TextLine(
            title=_(u"Email"),
            description=_(u"A valid email address where you can be reached."),
            constraint=validate_email,
        )

    form.widget(facultyofinterest=CheckBoxFieldWidget)
    facultyofinterest  = List(
        title=_(u"Faculty of interest"),
        description=_(u"Optional: Please indicate up to five faculty whose research interests you."),
        value_type=Choice(vocabulary = facultyofinterest_vocab),
        max_length=5,
        )

    facultyofinterestother = TextLine(
        title = _(u"Faculty of Interest (other)"),
        description = _(u"If you did not see the faculty you were interested in on the list, please write their names in here."),
        required=False,
        )

    howdidyouhear = TextLine(
        title=_(u"How did you hear about IQ Biology?"),
        description = _(u""),
        required=False,
        )

    degreeprogram1 = Choice(
        title=_(u"First Degree Program of Interest"),
        description=_(u"Remember this degree program. You will formally fill out the application on CU's Graduate School Application website for this degree program. The options are presented in the drop down menu (with their associated colleges)."),
        vocabulary = degreeprograms_vocab,
        constraint = choiceVocabConstraint,
      )
    degreeprogram2 = Choice(
        title=_(u"Second Degree Program of Interest"),
        description=_(u""),
        vocabulary = degreeprograms_vocab,
        constraint = choiceVocabConstraint,
       )
    degreeprogram3 = Choice(
        title=_(u"Third Degree Program of Interest"),
        description=_(u""),
        vocabulary = degreeprograms_vocab,
        required=False,
       )

    alsoapply = Choice(
        title = _(u"Consideration by individual degree program(s)?"),
        description = _(u"If you are not accepted by the IQ Biology program, would you like to be considered independently by one or more of your Degree Programs of Interest for admission directly to their program?"),
        vocabulary = yes_no_vocab,
        constraint = choiceVocabConstraint,
        )

    form.widget(degreeprograms=CheckBoxFieldWidget)
    degreeprograms = List(
        title = _(u"Which Degree Programs?"),
        description = _(u"If so, please indicate which degree programs you would like to consider your application (up to three)."),
        value_type = Choice(vocabulary = degreeprograms_lite_vocab),
        required=False,
        max_length=3,
        )

    # ---------- conditional questions if "Biochemistry" is selected ---------
    form.fieldset('Biochemistry',
                  label = _(u"Supplementary Information for the Biochemistry Degree Program"),
                  fields = ['biochem_research_interests',
                            'biochemteachingexperience',
                            'biochemresearchexperience'])

    form.widget(biochem_research_interests=CheckBoxFieldWidget)
    biochem_research_interests = List(
        title = _(u"Biochemistry Research Interests"),
        description = _(u"Please check off as many of the research areas as interest you."),
        value_type = Choice(vocabulary = biochem_research_interests_vocab),
        required=False,
        )

    biochemteachingexperience = Text(
        title = _(u"Teaching Experience"),
        description = _(u"Please list all previous teaching experience including the subject, start date, end date, and institution."),
        required=False,
        )

    biochemresearchexperience = Text(
            title=_(u"Research Experience"),
            description=_(u"Please list all previous research experience including the project name/short description, start date, end date, and institution/company."),
            required=False,
        )

    # ---------- conditional questions if "ChemBioEngineering" is selected ---------
    form.fieldset('ChemBioEngineering',
                  label = _(u"Supplementary Information for the Chemical and Biological Engineering Degree Program"),
                  fields = ['bioengfellowshipsupport',
                            'bioengresearchinterests',
                            'bioengducationalgoals'])

    form.widget(bioengfellowshipsupport=CheckBoxFieldWidget)
    bioengfellowshipsupport = Bool(
        title = _(u"Fellowship Support"),
        description = _(u"Have you applied for or do you have any other fellowship support? (check for 'yes')"),
        required = False,
        )

    form.widget(bioengresearchinterests=CheckBoxFieldWidget)
    bioengresearchinterests = List(
        title = _(u"Research Interests"),
        description = _(u"Check multiple boxes (up to three):"),
        required=False,
        value_type = Choice(vocabulary = chem_bio_vocab),
        max_length = 3,
        )

    bioengducationalgoals = Text(
        title = _(u"Educational Goals"),
        description = _(u"write in - 2,000 characters max"),
        required = False,
        min_length = None,
        max_length = 2000,
        )

    # ---------- conditional questions if "ComputerScience" is selected ---------
    form.fieldset('ComputerScience',
                  label  = _(u"Supplementary Information for the Computer Science Degree Program"),
                  fields = ['csinterests',
                            'csfinancialaid',])

    form.widget(csinterests=CheckBoxFieldWidget)
    csinterests = List(
        title = _(u"Your Interests"),
        description = _(u"Which areas represented at the University of Colorado are you interested in? Please pick up to three areas."),
        required=False,
        value_type=Choice(vocabulary = comp_sci_vocab),
        max_length=3,
        )

    csfinancialaid = Choice(
        title = _(u"Financial Aid (select one)"),
        description = _(u"Indicate your need for financial aid (e.g., Research or Teaching Assistantships) after your second year. Students accepted to the IQ Biology program will have the first two years of funding guaranteed through the IQ Biology program. "),
        required = False,
        vocabulary = comp_sci_financial_aid_vocab,
        )

    # ---------- conditional questions if "Ecology" is selected ---------
    form.fieldset('Ecology',
                  label = _(u"Supplementary Information for the Ecology and Evolutionary Biology Degree Program"),
                  fields = ['ecofinancialaid',
                            'ecoundergradgpa',
                            'ecoundergradgpabio',
                            'ecogradgpa',
                            'ecogradgpabio',
                            'ecogre',
                            'ecocoursebio',
                            'ecocoursechem',
                            'ecocoursemath',
                            'ecocoursephysics',
                            'ecocourseother',
                            'ecoresearchinterests',
                            'ecofaculty',
                            'ecopublications',])

    ecofinancialaid = Choice(
        title = _(u"Financial Aid"),
        description = _(u"Will you be requesting financial support in the form of a fellowship teaching assistantship or research assistantship beyond what is provided for IQ Biology students? (Students accepted to the IQ Biology program will have two years of funding through the IQ Biology program guaranteed)."),
        required = False,
        vocabulary = yes_no_vocab,
        )

    ecoundergradgpa = Float(
        title = _(u"Undergraduate GPA (overall)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0. (up to 1 decimal place.)"),
        required = False,
        constraint = validate_decimal,
        )

    ecoundergradgpabio = Float(
        title = _(u"Undergraduate GPA: biological science courses only"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0. (up to 1 decimal place.)"),
        required = False,
        constraint = validate_decimal,
        )

    ecogradgpa = Float(
        title = _(u"Overall Graduate GPA (optional)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0.  If you have not yet taken any graduate level courses, leave this question blank."),
        required = False,
        constraint = validate_decimal,
        )
    ecogradgpabio = Float(
        title = _(u"Graduate GPA: biological science courses only (optional)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0.  If you have not yet taken any graduate level courses, leave this question blank."),
        required = False,
        constraint = validate_decimal,
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
        description = _(u"Please list the names of other science and relevant courses you have taken (and your grade in each course). "),
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
        description = _(u"Please list the complete citations of any scientific publications that you have authored."),
        required = False,
        )

    #----- if ChemicalPhysics is chosen ----------------------------
    form.fieldset('ChemicalPhysics',
                  label  = u"Supplementary Information for the Chemical Physics Degree Program",
                  fields = ['chemphresearchinterests',
                  		    'chemphexperimental',
                            'chemphgpaphysics',
                            'chemphgpamath',
                            'chemphgpacombined',
                            'chemphgpaoverall',
                            'chemphgre'])

    chemphresearchinterests  = Text(
        title = _(u"Research Interests"),
        description = _(u"Please write in a few phrases that describe your area(s) of interest or specialization."),
        required = False,
        )

    form.widget(chemphexperimental=CheckBoxFieldWidget)
    chemphexperimental = List(
        title = _(u"Research Interests: experimental or theoretical"),
        description = _(u"Check one or both boxes depending on your interests."),
        required=False,
        value_type=Choice(vocabulary = exp_or_theoretical_vocab),
        )

    chemphgpaphysics = Float(
        title = _(u"Undergraduate GPA: physics courses only"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        constraint = validate_decimal,
        )

    chemphgpamath = Float(
        title = _(u"Undergraduate GPA: math courses only"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        constraint = validate_decimal,
        )

    chemphgpacombined = Float(
        title = _(u"Undergraduate GPA: combined math and physics courses "),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        constraint = validate_decimal,
        )

    chemphgpaoverall = Float(
        title = _(u"Undergraduate GPA: overall (all courses)"),
        description = _(u"Calculate your GPA based on the following scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0."),
        required = False,
        constraint = validate_decimal,
        )

    chemphgre = Text(
        title = _(u"GRE Score: Physics Subject Exam (optional)"),
        description = _(u"If you have taken a Physics Subject Exam please write in the name of the exam, your raw score, your percentile, and the month and year (MM/YY) you took the test."),
        required = False,
        min_length = None,
        max_length = None,
        )

    form.fieldset('review',
                  label = 'Review',
                  fields = ['faculty_comments',
                            'assignedreviewers',
                            'program1_accepted',
                            'program1_acceptancedate',
                            'program1_comments',
                            'program2_accepted',
                            'program2_acceptancedate',
                            'program2_comments',
                            'program3_accepted',
                            'program3_acceptancedate',
                            'program3_comments',
                            ])

    form.omitted(IAddForm, 'faculty_comments')
    dexterity.write_permission(faculty_comments='Review portal content')
    faculty_comments = Text(
        title = _(u"Faculty Review Comments"),
        description = _(u"Please optionally enter any comments supporting your Acceptance or Not Acceptance decision."),
        required = False,
        )

#    form.omitted(IAddForm, 'assignedreviewers')
#    assignedreviewers = schema.List(
#        title = _(u"Assigned Reviewers"),
#        default = [],
#        #source = GroupMembers('FacultyReviewers'),
#        value_type=schema.Choice(...)
#        required = False,
#        )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # The following fields are for the various departments to     #
    # comment and accept/notaccept an applicant                   #

    #-- prefix the following with each dept's identifier ------------
    form.omitted(IAddForm, 'program1_accepted')
    program1_accepted = Choice(
        title = _(u"First Degree Program: Accepted?"),
        description = _(u"Would you accept this person into your program?"),
        required=False,
        vocabulary = yes_no_vocab,
        )
    form.mode(program1_acceptancedate='hidden')
    program1_acceptancedate = Datetime(
        title = _(u"First Degree Program: Acceptance Date"),
        description = _(u"If this person might be accepted into your program, please enter the date and time of this conditional determination."),
        required = False,
        )
    form.omitted(IAddForm, 'program1_comments')
    program1_comments = Text(
        title = _(u"First Degree Program: Comments"),
        description = _(u"Please optionally enter any comments supporting your Acceptance or Not Acceptance decision."),
        required = False,
        )

    form.omitted(IAddForm, 'program2_accepted')
    program2_accepted = Choice(
        title = _(u"Second Degree Program: Accepted?"),
        description = _(u"Would you accept this person into your program?"),
        required=False,
        vocabulary = yes_no_vocab,
        )
    form.mode(program2_acceptancedate='hidden')
    program2_acceptancedate = Datetime(
        title = _(u"Second Degree Program: Acceptance Date"),
        description = _(u"If this person might be accepted into your program, please enter the date and time of this conditional determination."),
        required = False,
        )
    form.omitted(IAddForm, 'program2_comments')
    program2_comments = Text(
        title = _(u"Second Degree Program: Comments"),
        description = _(u"Please optionally enter any comments supporting your Acceptance or Not Acceptance decision."),
        required = False,
        )

    form.omitted(IAddForm, 'program3_accepted')
    program3_accepted = Choice(
        title = _(u"Third Degree Program: Accepted?"),
        description = _(u"Would you accept this person into your program?"),
        required=False,
        vocabulary = yes_no_vocab,
        )
    form.mode(program3_acceptancedate='hidden')
    program3_acceptancedate = Datetime(
        title = _(u"Third Degree Program: Acceptance Date"),
        description = _(u"If this person might be accepted into your program, please enter the date and time of this conditional determination."),
        required = False,
        )
    form.omitted(IAddForm, 'program3_comments')
    program3_comments = Text(
        title = _(u"Third Degree Program: Comments"),
        description = _(u"Please optionally enter any comments supporting your Acceptance or Not Acceptance decision."),
        required = False,
        )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # The following fields are for the overall management of the process  #

    form.mode(completed='hidden')
    completed = Int(
        title = _(u"Is completed?"),
        description = _(u"Identify that your form was completed."),
        required = False,
        default = 0,
        )


# Now we need to compute the title.
# An accompanying adapter is in configure.zcml
class INameFromPersonNames(INameFromTitle):
    def title():
        """Return a processed title"""


class NameFromPersonNames(object):
    implements(INameFromPersonNames)

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        mname =""
        if self.context.mname:
            mname = '_' + self.context.mname
        return "%s_%s%s" % (self.context.lname, self.context.fname, mname )


class View(dexterity.DisplayForm):
    """The view. Will pull a template from <modulename>_templates/view.pt,
        and will be called 'view' unless otherwise stated.
        """
    grok.context(IPasurvey)
    grok.require('zope2.View')

    def getRolesOfUser(self):
        """A hack to determine if the current user is an admin or editor,
        or a normal user so we can display info in the view"""
        context = aq_inner(self)
        mt = getToolByName(context, 'portal_membership')
        memb = mt.getAuthenticatedMember()
        roles = memb.getRolesInContext(self)
        allowed = ['Editor','Manager']
        is_allowed = set(allowed).intersection( set(roles) )
        is_allowed = list(is_allowed)
        retval = False
        if len(is_allowed) == True:
            retval = True
        return retval

    def isComplete(self):
        data, errors = self.extractData()
        if data['completed'] == 1:
            retval = True
        else:
            retval = False
        return retval


# fields that cannot be skipped when "Save As Draft"
ALWAYS_REQUIRED_FIELDS = ('fname', 'alsoapply', 'lname', 'email','dob', 'degreeprogram1', 'degreeprogram2',)

class AddForm(dexterity.AddForm):
    grok.name('iqbio.pasurvey.pasurvey')
    # extends fields, buttons and handlers from base class
    z3cform.extends(dexterity.AddForm)

    def isRequiredError(self, error):
        if isinstance(error, RequiredMissing):
            # some fields are always required
            if error.__str__() not in ALWAYS_REQUIRED_FIELDS:
                return True
        return False

    ### override handlers from plone.dexterity.browser.add.DefaultAddForm
    @button.buttonAndHandler(_('Save As Draft'), name='save')
    def handleAdd(self, action):
        data, errors = self.extractData()
        # skip RequiredMissing errors
        errors = [e for e in errors if not self.isRequiredError(e.error)]
        if errors:
            self.status = self.formErrorsMessage
            # advoid required errors to be displayed then
            for name, widget in self.widgets.items():
                if widget.error and self.isRequiredError(widget.error.error):
                    self.widgets[name].error = None
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            IStatusMessage(self.request).addStatusMessage(_(u"Item created"),
                                                          "info")

    def update(self):
        super(AddForm, self).update()

        survey = self.getSurvey()
        if survey:
            # redirect to EditForm if survey was created
            self.request.response.redirect(survey.getURL() + '/edit')
            return None

    @property
    def catalog(self):
        context = aq_inner(self.context)
        tools = getMultiAdapter((context, self.request), name=u'plone_tools')
        return tools.catalog()

    @property
    def portal_state(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        return portal_state

    def getUserName(self):
        member = self.portal_state.member()
        if member:
            return member.getId()

    def getSurvey(self):
        """ Get the created survey """
        surveys = self.catalog(object_provides=IPasurvey.__identifier__, Creator=self.getUserName())
        if surveys:
            return surveys[0]

        return None


class EditForm(dexterity.EditForm):
    grok.context(IPasurvey)
    grok.require('zope2.View')
    # extends fields, buttons and handlers from base class
    z3cform.extends(dexterity.EditForm)

    def update(self):
        super(EditForm, self).update()

        groups = []
        for group in self.groups:
            # condition to show/hide Review fieldset
            if group.__name__ == 'review':
                state = self.getReviewState()
                # always show if user is Manager
                if self.checkPermission('Manage Portal'):
                    groups.append(group)
                elif state == 'programreview' or \
                    (state == 'facultyreview' and self.checkPermission('Review portal content')):
                    for name, widget in group.widgets.items():
                        if not self.isProgramReviewable(name, state):
                            widget.mode = HIDDEN_MODE
                    groups.append(group)
            # temporary disable ownership fieldset
            elif group.__name__ <> 'ownership':
                groups.append(group)

        self.groups = tuple(groups)

    def isProgramReviewable(self, name, review_state):
        """ Check whether the current user can review the selected programs
        """
        username = self.getUserName()
        if name.startswith('program1_'):
            value = self.fields['degreeprogram1'].field.get(self.context)
            if self.isUserInGroup(username, value):
                return True
        elif name.startswith('program2_'):
            value = self.fields['degreeprogram2'].field.get(self.context)
            if self.isUserInGroup(username, value):
                return True
        elif name.startswith('program3_'):
            value = self.fields['degreeprogram3'].field.get(self.context)
            if self.isUserInGroup(username, value):
                return True
        elif review_state == 'facultyreview':
            return True

        return False

    def isUserInGroup(self, userid, groupid):
        if groupid:
            members = self.gtool.getGroupMembers(groupid)
            if userid in members:
                return True
        return False

    def getReviewState(self):
        wftool = self.tools.workflow()
        # Returns workflow state object
        status = wftool.getStatusOf("iqbio.pasurvey.workflow", self.context)
        # Plone workflows use variable called "review_state" to store state id
        # of the object state
        if status and status.has_key("review_state"):
            return status["review_state"]
        else:
            return None

    def checkPermission(self, permission):
        membership = self.tools.membership()
        return membership.checkPermission(permission, self.context)

    def getRolesOfUser(self):
        """A hack to determine if the current user is a Manager or Editor.
        We'll use this to allow Editor's only if the form has been submitted
        since the workflow is not yet in place.
        Sorry. I know it's a horrible hack.
        """
        context = aq_inner(self)
        mt = getToolByName(context, 'portal_membership')
        memb = mt.getAuthenticatedMember()
        roles = memb.getRolesInContext(self)
        allowed = ['Editor','Manager']
        is_allowed = set(allowed).intersection( set(roles) )
        is_allowed = list(is_allowed)
        retval = False
        if len(is_allowed) == True:
            retval = True
        return retval

    # custom buttons
    @button.buttonAndHandler(_('Save As Draft'), name='save')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        # set program acceptancedate automatically
        if data.get('program1_accepted', None):
            data['program1_acceptancedate'] = datetime.now()
        if data.get('program2_accepted', None):
            data['program2_acceptancedate'] = datetime.now()
        if data.get('program3_accepted', None):
            data['program3_acceptancedate'] = datetime.now()
        self.applyChanges(data)

        # send email to user when saved as draft
        self.notifyUser(data['email'])

        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"), "info")
        self.request.response.redirect(self.context.absolute_url())

    def notifyUser(self, email):
        """Send a message to the submitter"""
        mail_host = getToolByName(self.context, 'MailHost')

        portal = self.portal_state.portal()
        sender_email = portal.getProperty('email_from_address')
        sender_name = portal.getProperty('email_from_name')

        if sender_email:
            sender = '%s <%s>' % (sender_name, sender_email)
        else:
            return

        subject = "IQ Biology Survey Form Submission"
        #message = "A survey for %s was created here %s" % (self.context.title, self.context.absolute_url())
        message= """Thank you for saving your IQ Biology Survey and Supplementary Information.

If you have not done so already, please continue to the
Graduate School Application Website at:

https://soaprod.cusys.edu/degreeprog/applyDEGREEPROG_CUBLD/login.action

...to fill out your application for your
"First Department of Interest".

Remember to return to the IQ Biology Survey and
Supplementary Information site to edit information
on your survey and provide the necessary supplementary
information for your Degree Programs of Interest
before the deadline.

You may use this link to return back to the IQ Biology Survey
site to enter in your Supplementary Information and edit any
of your information as needed:

http://iqbiology.colorado.edu/survey/

After you have completed your IQ Biology Survey and
Supplementary Information, press the "Submit Survey"
button.

After you do that, your information will be delivered
to IQ Biology and will no longer be available for edit.

Please review the Application Instructions:

http://iqbiology.colorado.edu/application/instructions

...to be sure that your entire application is complete
by the deadline on January 5th, 2011.

Please contact us http://iqbiology.colorado.edu/contact-us
if you have any questions.


Thank you,

The IQ Biology Program
IQBiology.colorado.edu



Note: You will recieve one of these reminder messages
      every time you edit your survey form.

        """
        if email:
            mail_host.send(message, email, sender, subject)

    @button.buttonAndHandler(_(u'Submit Survey'), name='submit')
    def handleSubmit(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # set the survey completed manually
        data['completed'] = 1
        self.applyChanges(data)

        # redirect to workflow submit url
        submit_url = '%s/content_status_modify?workflow_action=submit' % self.context.absolute_url()
        self.request.response.redirect(submit_url)

    @property
    def portal_state(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        return portal_state

    @property
    def tools(self):
        context = aq_inner(self.context)
        tools = getMultiAdapter((context, self.request), name=u'plone_tools')
        return tools

    @property
    def gtool(self):
        return getToolByName(self.context, 'portal_groups')

    def getUserName(self):
        member = self.portal_state.member()
        if member:
            return member.getId()


class Printable(grok.View):
    """ dexterity.DisplayForm A printable view for a survey
    """

    grok.context(IPasurvey)
    grok.require('zope2.View')
    grok.name('printable')


