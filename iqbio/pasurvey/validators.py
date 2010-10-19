import inspect
from zope.interface import implements
from Products.validation import validation
from Products.validation.interfaces import ivalidator
from Products.validation.interfaces.IValidator import IValidator
from zope.app.component.hooks import getSite



# Now that we've defined a custom field validator, register it.
# Does it matter if I've registered it in the __init__.py?
#validation.register(isUniqueUnixUid('isUniqueUnixUid'))
