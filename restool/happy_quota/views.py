from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, enter your leads here")


def add_leads_here(request, project_id):
    return HttpResponse("You should add leads here" % project_id)


def lead_added(request, project_id):
    response = "Your lead was added"
    return HttpResponse(response % project_id)



def lead_detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)