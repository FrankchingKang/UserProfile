from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class UpperLowercaseValidator:
    def validate(self, password, user=None):
        if not (any(char.isupper() for char in password) and \
            any(char.islower() for char in password)):
            raise ValidationError(_('must use of both uppercase and lowercase letters'))

    def get_help_text(self):
        return 'must use of both uppercase and lowercase letters'

class DigitValidator:
    def validate(self, password, user=None):
        if not (any(char.isdigit() for char in password)):
            raise ValidationError(_('must include one or more numerical digits'))

    def get_help_text(self):
        return 'must include one or more numerical digits'

class SpecialCharValidator:
    def validate(self, password, user=None):
        Special_char = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char in Special_char for char in password):
            raise ValidationError(_('must include one or more of special characters, such as @, #, $'))

    def get_help_text(self):
        return 'must include one or more of special characters, such as @, #, $'
