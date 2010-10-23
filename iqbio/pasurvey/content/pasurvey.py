from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from zope.app.container.interfaces import IObjectAddedEvent
from Products.CMFCore.utils import getToolByName

from iqbio.pasurvey import _

from iqbio.pasurvey.vocabularies import biochem_research_interests_vocab, \
    facultyofinterest_vocab, degreeprograms_vocab, bio_chem_vocab, comp_sci_vocab
    chem_bio_vocab,

class IPasurvey(form.Schema):
    """A conference presenter. Presenters can be added anywhere.
    """
    fname = schema.TextLine(
            title=_(u"First Name"),
            description=_(u"Your legal first name"),
        )
    mname = schema.TextLine(
            title=_(u"Middle Name or Initial"),
            description=_(u""),
        )
    lname = schema.TextLine(
            title=_(u"Last Name / Sir Name"),
            description=_(u"Your legal last name"),
        )
    dob = schema.Date(
            title=_(u"Date of birth"),
            description=_(u""),
        )

    email = schema.TextLine(
            title=_(u"Email"),
            description=_(u"A valid email address where you can be reached."),
        )


    facultyofinterest  = schema.Choice(
        title=_(u"Faculty of interest"),
        description=_(u"Optional: Please indicate up to five faculty whose research interests you."),
        vocabulary = facultyofinterest_vocab,
        required=False,
        )

    facultyofinterestother = schema.TextLine(
        title = _u("Faculty of Interest (other)"),
        description = _(u"If you did not see the faculty you were interested in on the list, please write their name in here."),
        required=False,
        )

    degreeprogram1 = schema.Choice(
        title=_(u"First degree program of interest"),
        description=_(u"Remember this degree program. You will formally fill out the application on CU's Graduate School Application website for this degree program. The options are presented in the drop down menu (with their associated colleges)."),
        vocabulary = degreeprograms_vocab,
        required=False,
      )
    degreeprogram2 = schema.Choice(
        title=_(u"Second degree program of interest"),
        description=_(u""),
        vocabulary = degreeprograms_vocab,
        required=False,
       )
    degreeprogram3 = schema.Choice(
        title=_(u"Third degree program of interest"),
        description=_(u""),
        vocabulary = degreeprograms_vocab,
        required=False,
       )

    alsoapply = schema.Bool(
        title = _u("Apply to Department Also"),
        description = _(u"If you are not accepted by the IQ Biology program, would you like to be considered independently by one or more of your Degree Programs of Interest for admission directly to their program?"),
        )

    degreeprograms = schema.Choice(
        title = _u("Which Degree Programs?"),
        description = _(u"If so, please indicate which degree programs you would like your application considered by (up to three)."),
        vocabulary = degreeprograms_vocab,
        required=False,
        )

    biochem_research_interests = schema.Bool(
        title = _u("Biochemistry Research Interests"),
        description = _(u"Please check off as many of the research areas as interests you."),
        vocabulary = biochem_research_interests_vocab,
        required=False,
        )

#     xxxx = schema.Bool(
#        title = _(u""),
#        description = _(u""),
#        required=False,
#        )


    description = schema.Text(
            title=_(u""),
            description=_(u""),
        )

    bioteachingexperience = RichText(
            title=_(u"Teaching Experience"),
            description=_(u"Please list all previous teaching experience including the subject, start date, end date, and institution."),
            required=False
        )

    picture = NamedImage(
            title=_(u"Picture"),
            description=_(u"Please upload an image"),
            required=False,
        )


class View(grok.View):
    grok.context(IPasurvey)
    grok.require('zope2.View')
