from django.http import HttpResponse

StopExisting = "eu estou morrendo" 
get_mad="isso não acaba logo"


def mrMeeseeks(request, task):
    if task and task.is_complete:
        task.object.create()
        return HttpResponse ("I,m Mr. Meeseeks, look at me!")

    while not task.is_complete:
        task.object.create()
        get_mad()
        HttpResponse("Existence is pain!!!")
        ''' Existence is pain!!! '''
    else:
        StopExisting()
    