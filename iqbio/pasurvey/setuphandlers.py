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
    logger.info('****** end create Survey folder ******')


#----------------------------------------------------------------------
def createGroups(portal):
    """Create the new groups for the survey management"""
        # Set up groups
    uf = getToolByName(portal, 'acl_users')
    gtool = getToolByName(portal, 'portal_groups')
    if not uf.searchGroups(id='FacultyReviewers'):
        gtool.addGroup('FacultyReviewers', title='FacultyReviewers', roles=['Editor'])
    if not uf.searchGroups(id='SurveyManagers'):
        gtool.addGroup('SurveyManagers', title='SurveyManagers', roles=['Manager'])
    if not uf.searchGroups(id='ProgramReviewers'):
        gtool.addGroup('ProgramReviewers', title='ProgramReviewers', roles=['Editor'])


def importVarious(context):
    """Run the handlers for the default profile
    """
    if context.readDataFile('iqbio.pasurvey_various.txt') is None:
        return
    portal = context.getSite()
    createSurveyFolder(portal)
    createGroups(portal)

