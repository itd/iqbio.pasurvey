from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.upgrade import _upgrade_registry
from Products.GenericSetup.registry import _profile_registry
from Products.CMFPlone.utils import _createObjectByType

import logging
logger = logging.getLogger(__name__)

def addInitialAdmins(site):
    rtool = getToolByName(site, 'portal_registration')
    members = [
        {'id':'test@tool.net',
         'email': 'test@tool.net',
         'password': 'iqbio'},
    ]
    rta = rtool.addMember
    for member in members:
        try:
            rta(
                id=member['id'],
                password=member['password'],
                roles=['Manager', 'Member'],
                properties={
                    'username': member['id'],
                    'email': member['email']
                },
            )
        except ValueError:
            already_taken = '\nlogin id %s already exists...\n\n'
            logger.debug(already_taken % (member['id'],))

#----------------------------------------------------------------------
GLIST = (
    {'id':'SurveyManagers', 'title':'Survey Managers', 'roles':'Manager'},
    {'id':'FacultyReviewers', 'title':'Faculty Reviewers', 'roles':'Member'},
    {'id':'AppliedMath', 'title':'Applied Mathematics', 'roles':'Member'},
    {'id':'Biochemistry', 'title':'Biochemistry', 'roles':'Member'},
    {'id':'ChemBioEngineering', 'title':'ChemBioEngineering', 'roles':'Member'},
    {'id':'ComputerScience', 'title':'Computer Science', 'roles':'Member'},
    {'id':'Ecology', 'title':'Ecology', 'roles':'Member'},
    {'id':'Mechanical', 'title':'Mechanical Engineering', 'roles':'Member'},
    {'id':'Molecular', 'title':'Molecular', 'roles':'Member'},
    {'id':'ChemicalPhysics', 'title':'Chemical Physics', 'roles':'Member'},
    )

def createGroups(portal):
    """Create the new groups for the survey management"""
    uf = getToolByName(portal, 'acl_users')
    gtool = getToolByName(portal, 'portal_groups')

    for i in GLIST:
        if not uf.searchGroups(id=i['id']):
            gtool.addGroup(i['id'], title=i['title'], roles=[i['roles']])


def setSurveyFolderContentRestrictions(context):
    """"""
    site = context.getParentNode()
    if not 'survey' in site.objectIds():
        createSurveyFolder(context)
    else:
        sfolder = site._getOb('surveys')
        # Add type restrictions
        logger.info('Restricting addable types in survey Folder \
            to iqbio.pasurvey.pasurvey (Pre-Admission Survey)')
        sfolder.setConstrainTypesMode(1)
        sfolder.setLocallyAllowedTypes(['iqbio.pasurvey.pasurvey', 'Page', 'Topic',])
        sfolder.setImmediatelyAddableTypes(['iqbio.pasurvey.pasurvey'])


def updateCatalog(context):
    """update the catalog"""
    logger.info('****** updateCatalog BEGIN ******')
    pc = getToolByName(context, 'portal_catalog')
    pc.refreshCatalog()
    logger.info('****** updateCatalog END ******')


def setIntranetWorkflow(context):
    """ Setting the initial workflow to intranet_workflow for now.
    """
    portal = context.getSite()
    wft = getToolByName(portal, "portal_workflow")
    wft.setDefaultChain('intranet_workflow')
    logger.info('\n\n  default workflow set to intranet_workflow \n\n')

def updateRoleMappings(context):
    """after workflow change, update the roles mapping. This is like pressing
    the button 'Update Security Setting' in the portal_workflow ZMI"""
    portal = context.getSite()
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()
    wft.doActionFor(portal.surveys, 'publish_internally')


#----------------------------------------------------------------------
def hideMembersFolder(context):
    """set the setExcludeFromNav bit to true on the Members folder
    """
    portal = context.getSite()
    members = portal.Members
    members.setExcludeFromNav(True)
    members.update()


#----------------------------------------------------------------------
def hideStuff(context):
    """rm stuff in the portal root"""
    portal = context.getSite()
    stuff = ['events', 'news']
    for obj in stuff:
        if obj in portal.listFolderContents():
            obj = portal.obj
            obj.setExcludeFromNav(True)
            obj.update()

def setWorkflowGroups(portal):
    wft = getToolByName(portal, "portal_workflow")
    wf = wft.get('iqbio.pasurvey.workflow', None)
    if wf:
        # add groups to manage
        for g in GLIST:
            wf.addGroup(g['id'])
        # map groups - roles in states
        facultyreview_state = wf.states['facultyreview']
        request = {'FacultyReviewers|Reviewer': 1, }
        facultyreview_state.setGroups(request)
        
        programreview_state = wf.states['programreview']
        request = {'AppliedMath|Editor': 1,
                   'Biochemistry|Editor': 1,
                   'ChemBioEngineering|Editor': 1,
                   'ComputerScience|Editor': 1,
                   'Ecology|Editor': 1,
                   'Mechanical|Editor': 1,
                   'Molecular|Editor': 1,
                   'ChemicalPhysics|Editor': 1}
        programreview_state.setGroups(request)
#    import pdb; pdb.set_trace()


#----------------------------------------------------------------------
def createSurveyFolder(portal):
    """ create SurveyFolder
    """
    logger.info('*start create Survey Folder')
    portal_ids = portal.contentIds()
    if 'surveys' not in portal_ids:
        _createObjectByType('Folder', portal,
                id='surveys', title='Surveys',
                description='Pe-Admission survey submission folder')
    logger.info('...Survey folder done')


#----------------------------------------------------------------------
def setSurveysFolderView(portal):
    """set the default view of the surveys folder"""
    portal_ids = portal.contentIds()
    if 'surveys' in portal_ids:
        portal.surveys.setLayout('@@survey-index')
        logger.info('> surveys folder default view set to @@survey-index')


#----------------------------------------------------------------------
def transitionSurveysFolderWorkflow(portal):
    """move the surveys folder to the published internally state"""
    portal_ids = portal.contentIds()
    if 'surveys' in portal_ids:
        surveys = portal.surveys
        wft = getToolByName(portal, 'portal_workflow')
        # check if folder can be transitioned to 'publish_internally'
        trans = wft.getTransitionsFor(surveys)
        trans = [i['id'] for i in trans]
        if 'publish_internally' in trans:
            wft.doActionFor(surveys, 'publish_internally')
            logger.info('* surveys folder transitioned to internally_published state')

#----------------------------------------------------------------------
def importVarious(context):
    """Run the handlers for the default profile
    """
    if context.readDataFile('iqbio.pasurvey_various.txt') is None:
        return
    portal = context.getSite()
    setSurveyFolderContentRestrictions
    createGroups(portal)
    hideStuff(context)
    hideMembersFolder(context)
    setIntranetWorkflow(context)
    setWorkflowGroups(portal)
    #updateRoleMappings(context)
    createSurveyFolder(portal)
    setSurveysFolderView(portal)
    transitionSurveysFolderWorkflow(portal)

