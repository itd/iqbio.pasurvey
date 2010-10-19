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



def uninstall(portal):
    out = StringIO()
    print >>out, "Un-installing iqbio.pasurvey"
    _runProfile('profile-iqbio.pasurvey:uninstall', portal)

