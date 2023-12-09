from django.conf import settings
from django.http import HttpResponse
import redis

def index(request):
    r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,\
                           db=0, password=settings.REDIS_PASSWORD)
    r.set('mykey', 'myvalue')
    
    return HttpResponse("Data saved to Redis")
