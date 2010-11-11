from five import grok
from Acquisition import aq_inner

from zope.component import getMultiAdapter

from plone.folder.interfaces import IFolder

from iqbio.pasurvey.pasurvey import IPasurvey

class SubmissionStatus(grok.View):
    """ Index page for survey folder
    """

    grok.context(IFolder)
    grok.require('zope2.View')
    grok.name('submission-status')

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


    def isAnon(self):
        return self.portal_state.anonymous()


    def getSurveys(self):
        """ Get a list of the surveys """
        if self.isAnon(): return None

        surveys = self.catalog(object_provides=IPasurvey,)
        if surveys:
            return surveys

        return None


