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
def createSurveyFolder(portal):
    """ create hSurveyFolder
    it has to be the last step from importVarious !
    """
    logger.info('****** start create Survey Folder ******')
    portal_ids = portal.contentIds()
    if 'surveys' not in portal_ids:
        _createObjectByType('Folder', portal,
                id='surveys', title='Surveys',
                description='Pe-Admission survey submission folder')
    #set the default view of the folder
    if 'surveys' in portal_ids:
        portal.surveys.setLayout('@@survey-index')
    logger.info('****** end create Survey folder ******')


#----------------------------------------------------------------------
def createGroups(portal):
    """Create the new groups for the survey management"""
    uf = getToolByName(portal, 'acl_users')
    gtool = getToolByName(portal, 'portal_groups')
    glist = (
        {'id':'SurveyManagers', 'title':'Survey Managers', 'roles':'Manager'},
        {'id':'FacultyReviewers', 'title':'Faculty Reviewers', 'roles':'Editor'},
        {'id':'AppliedMath', 'title':'Applied Mathematics', 'roles':'Editor'},
        {'id':'Biochemistry', 'title':'Biochemistry', 'roles':'Editor'},
        {'id':'ChemBioEngineering', 'title':'ChemBioEngineering', 'roles':'Editor'},
        {'id':'ComputerScience', 'title':'Computer Science', 'roles':'Editor'},
        {'id':'Ecology', 'title':'Ecology', 'roles':'Editor'},
        {'id':'Mechanical', 'title':'Mechanical Engineering', 'roles':'Editor'},
        {'id':'Molecular', 'title':'Molecular', 'roles':'Editor'},
        {'id':'ChemicalPhysics', 'title':'Chemical Physics', 'roles':'Editor'},
        )

    for i in glist:
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
    #wft.doActionFor(portal.surveys, 'publish_internally')

#----------------------------------------------------------------------
def hideMembersFolder(context):
    """set the setExcludeFromNav bit to true on the Members folder
    """
    portal = context.getSite()
    members = portal.Members
    members.setExcludeFromNav(True)
    members.update()

def rmStuff(context):
    """rm stuff in the portal root"""
    portal = context.getSite()
    stuff = ['events', 'news']
    for obj in stuff:
        if obj in portal.listFolderContents():
            portal.manage_delObjects(obj)


def importVarious(context):
    """Run the handlers for the default profile
    """
    if context.readDataFile('iqbio.pasurvey_various.txt') is None:
        return
    portal = context.getSite()
    createSurveyFolder(portal)
    setSurveyFolderContentRestrictions
    createGroups(portal)
    rmStuff(context)
    hideMembersFolder(context)
    setIntranetWorkflow(context)
    #updateRoleMappings(context)

