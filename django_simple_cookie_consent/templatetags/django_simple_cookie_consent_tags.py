from django.utils.translation import ugettext as _
from django import template
from django_simple_cookie_consent.models import CookieConsentSettings

register = template.Library()


COOKIE_MESSAGE = _('This website uses cookies to ensure you get the best experience on our website. ')
BUTTON_TEXT = _('Got It')
LINK_TEXT = _('Learn more')

@register.inclusion_tag('django_simple_cookie_consent/cookie_message.html')
def display_cookie_consent():
    cookie_settings = CookieConsentSettings.objects.first()
    if cookie_settings:
        return {
            'banner_colour': cookie_settings.banner_colour,
            'banner_text_colour': cookie_settings.banner_text_colour,
            'button_colour': cookie_settings.button_colour,
            'button_text_colour': cookie_settings.button_text_colour,
            'cookie_policy_link_text': cookie_settings.cookie_policy_link_text if cookie_settings.cookie_policy_link_text.strip()!='Learn more' else LINK_TEXT,
            'cookie_policy_link': cookie_settings.cookie_policy_link,
            'button_text': cookie_settings.button_text if cookie_settings.button_text.strip()!='Got it!' else BUTTON_TEXT,
            'message': cookie_settings.message if cookie_settings.message.strip()!="Do not change, go sources to have translation." else COOKIE_MESSAGE,
        }
    return {
        'no_cookie_settings': True
    }