from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

<<<<<<< HEAD:wepost_main/views/views.py

# Create your views here.
def index(requset):
    return render(requset,'base.html')

=======
<<<<<<< HEAD:wepost_main/views/views.py
# Create your views here.
def index(requset):
    return render(requset,'base.html')
=======
>>>>>>> cff26924c6841450a47de7efcad0801cab9b76be:wepost_main/views/sample_view.py

# test response
def test(request: HttpRequest):
    return render(request, 'wepost_main/test.html')
<<<<<<< HEAD:wepost_main/views/views.py

=======
>>>>>>> fix_conflict:wepost_main/views/sample_view.py
>>>>>>> cff26924c6841450a47de7efcad0801cab9b76be:wepost_main/views/sample_view.py
