import os
from StringIO import StringIO
from App.Common import package_home
from zope.i18nmessageid import MessageFactory
from Products.CMFCore.utils import getToolByName
#from Products.FacultyStaffDirectory.extenderInstallation import localAdaptersAreSupported, installExtender, uninstallExtender
#from Products.hpcfsdextender.person import PersonExtender
#from Products.hpcfsdextender.person import HPCPersonModifier

from iqbio.pasurvey.config import product_globals as GLOBALS

#_adapterName = 'hpcfsdextender'

def _runProfile(profile, portal):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profile)

def install(portal):
    out = StringIO()
    print >>out, "Installing iqbio.pasurvey"
    _runProfile('profile-iqbio.pasurvey:default', portal)

    # Set up groups
    uf = getToolByName(site, 'acl_users')
    gtool = getToolByName(site, 'portal_groups')
    if not uf.searchGroups(id='FacultyReviewers'):
        gtool.addGroup('FacultyReviewers', title='FacultyReviewers', roles=['Editor'])
    if not uf.searchGroups(id='SurveryManagers'):
        gtool.addGroup('SurveryManagers', title='SurveryManagers', roles=['Manager'])
    if not uf.searchGroups(id='ProgramReviewers'):
        gtool.addGroup('ProgramReviewers', title='ProgramReviewers', roles=['Editor'])


def uninstall(portal):
    out = StringIO()
    print >>out, "Un-installing iqbio.pasurvey"
    _runProfile('profile-iqbio.pasurvey:uninstall', portal)

