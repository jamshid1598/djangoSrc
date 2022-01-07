from projectroot.settings.base import *



# Override default project settings


try:
    from projectroot.settings.local import *
except:
    print("if project is on development progress, than you should create local.py file for local settings")


