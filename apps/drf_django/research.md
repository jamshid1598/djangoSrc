
##########################################################
#         recommended packages to work with drf          #
##########################################################

python3 -m pip install djangorestframework==3.12.4     # django-rest-framework
python3 -m pip install django-filter==21.1             # filtering support
python3 -m pip install Markdown==3.3.6                 # markdown support for browsable API
python3 -m pip install django-guardian==2.4.0          # django-guardian object level permission support




##########################################################
#   anf global settings for REST framework are kept in   #
#  single configuration dictionary named REST_FRAMEWORK  #
##########################################################

REST_FRAMEWORK = {
    .......
    .......
    .......
}


##########################################################
#       serializers define the API representation        #
##########################################################

from rest_framework import serializers
from django.contrib.auth.models import User

class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']




##########################################################
#           Viewsets define the view behavior            #
##########################################################

from rest_framework import viewsets
from django.contrib.auth.models import User

class ExampleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ExampleSerializer



##########################################################
#       routers provide an easy way of automatically     #
#                  determining the URL onf               #
##########################################################

from rest_framework import routers
from django.urls import path, include

router = routers.DefoultRouter()
router.register(r"users", ExampleViewSet)


##########################################################
#     Wire up our API using automatic URL routing.       #
##########################################################

urlpatters = [
    .....
    path('', include(router.urls)),
    .....
    .....

]



#  STATUS CODE #

200 - OK success status response code (request has succeeded)
201 - Created success status response (request has succeeded and has led to the creation of a resource)
202 - Accepted response status code (the request has been accepted for processing, but the processing has not been completed)
204 - No Content success status response (request has succeeded, but that the client doesn't need to navigate away from its current page)




400 - 
404 - 