from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse



class BlockUser(MiddlewareMixin):
    def process_request(self, request):
        print("user id+", request.user.id)
        # if request.user.id == 1:
        #     return HttpResponse("You are Blocked")