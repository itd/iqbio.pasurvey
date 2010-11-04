from five import grok
from Acquisition import aq_inner

from zope.component import getMultiAdapter

from plone.folder.interfaces import IFolder

from iqbio.pasurvey.pasurvey import IPasurvey

class SurveyIndex(grok.View):
    """ Index page for survey folder
    """
    
    grok.context(IFolder)
    grok.require('zope2.View')
    grok.name('survey-index')
    
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
    
    def getUserName(self):
        member = self.portal_state.member()
        if member:
            return member.getId()
        
    def getSurvey(self):
        """ Get the created survey """
        if self.isAnon(): return None
        
        surveys = self.catalog(object_provides=IPasurvey.__identifier__, Creator=self.getUserName())
        if surveys:
            return surveys[0]
        
        return None
        
    def getSurveyUrl(self, survey):
        if survey:
            return survey.getURL() + '/edit'
        else:
            return self.context.absolute_url() + '/++add++iqbio.pasurvey.pasurvey'


