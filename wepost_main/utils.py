from django.http import HttpResponse

import json


def JsonResponse(response):
    return HttpResponse(json.dumps(response), content_type="application/json")