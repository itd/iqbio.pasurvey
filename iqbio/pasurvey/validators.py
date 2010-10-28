import re
from zope import schema

from iqbio.pasurvey import _

class InvalidEmailAddress(schema.ValidationError):
    __doc__ = _(u"Your e-mail address is invalid")
    regex = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

def validate_email(value):
    if not re.match(InvalidEmailAddress.regex, value) or value.endswith('.'):
        raise InvalidEmailAddress
    return True

class InvalidDecimal(schema.ValidationError):
    __doc__ = _(u"Only accept numbers up to 1 decimal place")

def validate_decimal(value):
    """ only up to 1 decimal place """
    n = str(value)
    if '.' in n:
        if len(n.split('.')[-1]) > 1:
            raise InvalidDecimal
    return True
