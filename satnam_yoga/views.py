from django.http import HttpResponse
import os


def serveFile(request):
    filename = open(os.path.dirname(os.path.realpath(__file__)) + "\\E418E9768C32CF77F5A45100D28DDE3B.txt", 'r')
    content= filename.read()
    filename.close()
    response = HttpResponse(content, content_type='text/plain')
    return response
