from StringIO import StringIO

from five import grok
from Acquisition import aq_inner

from zope.component import getMultiAdapter

from Products.CMFCore.WorkflowCore import WorkflowException
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


class SurveyMigration(grok.View):
    """ Migration handler for survey folder
    """
    
    grok.context(IFolder)
    grok.require('cmf.ManagePortal')
    grok.name('migrate-surveys')
    
    @property
    def workflow(self):
        context = aq_inner(self.context)
        tools = getMultiAdapter((context, self.request), name=u'plone_tools')
        return tools.workflow()
    
    def update(self):
        context = aq_inner(self.context)
        self.submitCompletedSurveys(context)
            
    def submitCompletedSurveys(self, context):
        contentFilter = dict(review_state='draft', completed=1)
        self.surveys = context.getFolderContents(contentFilter, full_objects=True)
        self.migrated = 0
        self.failed = 0
        for survey in self.surveys:
            try:
                self.workflow.doActionFor(survey, "submit")
                self.migrated += 1
            except WorkflowException:
                # a workflow exception is risen if the state transition is not available
                # (the sampleProperty content is in a workflow state which
                # does not have a "submit" transition)
                self.failed += 1
                pass

