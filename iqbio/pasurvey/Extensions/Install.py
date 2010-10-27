import os
from StringIO import StringIO
from App.Common import package_home
from zope.i18nmessageid import MessageFactory
import transaction
from Products.CMFCore.utils import getToolByName

PRODUCT_DEPENDENCIES = ('',)
EXTENSION_PROFILES = ('iqbio.pasurvey:default',)

from iqbio.pasurvey.config import product_globals as GLOBALS

def install(self, reinstall=False):
    portal_quickinstaller = getToolByName(self, 'portal_quickinstaller')
    portal_setup = getToolByName(self, 'portal_setup')
    for product in PRODUCT_DEPENDENCIES:
        if reinstall and portal_quickinstaller.isProductInstalled(product):
            portal_quickinstaller.reinstallProducts([product])
            transaction.savepoint()
        elif not portal_quickinstaller.isProductInstalled(product):
            portal_quickinstaller.installProduct(product)
            transaction.savepoint()
    for extension_id in EXTENSION_PROFILES:
        portal_setup.runAllImportStepsFromProfile('profile-%s' % extension_id, purge_old=False)
        product_name = extension_id.split(':')[0]
        portal_quickinstaller.notifyInstalled(product_name)
        transaction.savepoint()


def uninstall(portal):
    out = StringIO()
    print >>out, "Un-installing iqbio.pasurvey"
    _runProfile('profile-iqbio.pasurvey:uninstall', portal)

