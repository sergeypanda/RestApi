from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

#some examples of custom validators
class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Password must contain at least 1 digit"), code='passw_no_number')

    def get_help_text(self):
        return _("Password must contain at least 1 digit")


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Password must contain at least 1 uppercase letter, A-Z."),code='password_no_upper')

    def get_help_text(self):
        return _("Password must contain at least 1 uppercase letter")
