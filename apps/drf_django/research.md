
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
201 - Created success status response (request has succeeded 
      and has led to the creation of a resource)
202 - Accepted response status code (the request has been accepted 
      for processing, but the processing has not been completed)
203 - The HTTP Status Code 203 means that the server is a 
      transforming proxy (such as a web accelerator) that received a 
      200 OK from its origin, but is returning a modified version of 
      the origin's response.
204 - No Content success status response (request has succeeded, but 
      that the client doesn't need to navigate away from its current 
      page.)


300 - Multiple Choices redirect status response code (the request has 
      more than one possible responses.)
301 - Moved Permanently redirect status response code (resource 
      requested has been definitively moved to the URL given by the 
      Location headers.)
302 - Found redirect status response code (resource requested has been 
      temporarily moved to the URL given by the Location header.)
303 - A 303 response to a GET request indicates that the origin server 
      does not have a representation of the target resource that can be 
      transferred by the server over HTTP.
304 - Not Modified client redirection response code indicates that there 
      is no need to retransmit the requested resources. It is an implicit 
      redirection to a cached resource.



400 - Bad Request response status code (server cannot or will not 
      process the request due to something that is perceived to be a 
      client error (for example, malformed request syntax, invalid 
      request message framing, or deceptive request routing))
401 - Unauthorized response status code (client request has not been 
      completed because it lacks valid authentication credentials 
      for the requested resource.)
402 - Payment Required is a nonstandard response status code that is 
      reserved for future use. ... Sometimes, this status code 
      indicates that the request cannot be processed until the client 
      makes a payment.
403 - Forbidden response status code (server understands the request 
      but refuses to authorize it. ... The access is permanently 
      forbidden and tied to the application logic, such as insufficient 
      rights to a resource.
404 - 404 not found, 404, 404 error, page not found or file not found 
      error message is a hypertext transfer protocol (HTTP) standard 
      response code, in computer network communications, to indicate 
      that the browser was able to communicate with a given server, 
      but the server could not find what was requested.



##    We can control the format of the response that we get back, either by using the Accept header:     ##
http http://127.0.0.1:8000/drf/snippet-list/v2/ Accept:application/json    # Request JSON
http http://127.0.0.1:8000/drf/snippet-list/v2/ Accept:text/html           # Request HTML


##   appending a format suffix:   ##
http http://127.0.0.1:8000/drf/snippet-list/v2.json    # JSON suffix
http http://127.0.0.1:8000/drf/snippet-list/v2.api     # Browsable API suffix


##     we can control the format of the request that we send, using the 'Content-Type' header.     ##
http --form POST http://127.0.0.1:8000/drf/snippet-list/v2/ code="print('POST using form data')"    # POST using form data
http --json POST http://127.0.0.1:8000/drf/snippet-list/v2/ code="print('POST using json')"         # # POST using JSON


##     