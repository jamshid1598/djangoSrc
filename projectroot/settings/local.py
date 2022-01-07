
# django-jet-reboost settings
from django.utils.translation import gettext_lazy as _

# configuration django-jet
# https://jet.readthedocs.io/en/latest/config_file.html#jet-default-theme
# JET_DEFAULT_THEME='light-gray' # options: 'default', 'green', 'light-violet', 'light-green', 'light-blue', 'light-gray'

# https://jet.readthedocs.io/en/latest/config_file.html#jet-themes
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# https://jet.readthedocs.io/en/latest/config_file.html#compact-menu
JET_SIDE_MENU_COMPACT = True # default False

# https://jet.readthedocs.io/en/latest/config_file.html#custom-menu
# JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
#     {'label': _('General'), 'app_label': 'core', 'items': [
#         {'name': 'help.question'},
#         {'name': 'pages.page', 'label': _('Static page')},
#         {'name': 'city'},
#         {'name': 'validationcode'},
#         {'label': _('Analytics'), 'url': 'http://example.com', 'url_blank': True},
#     ]},
#     {'label': _('Users'), 'items': [
#         {'name': 'core.user'},
#         {'name': 'auth.group'},
#         {'name': 'core.userprofile', 'permissions': ['core.user']},
#     ]},
#     {'app_label': 'banners', 'items': [
#         {'name': 'banner'},
#         {'name': 'bannertype'},
#     ]},
# ]


"""
django-jet == 1.0.8 package is not compatible with django >= 3.0.0

grep -ril "from six import python_2_unicode_compatible" \
    ~/Documents/django/djangoSrc | xargs sed -i  \
    's@from six import python_2_unicode_compatible@from six import python_2_unicode_compatible@g'
"""


