from five import grok
#from zope import schema
from zope.schema import Text, TextLine, Choice, Bool, Datetime
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
    fname = schema.TextLine(
            title=(u"First Name"),
            description=(u"Your legal first name"),
        )


class View(grok.View):
    grok.context(IPasurvey)
    grok.require('zope2.View')
