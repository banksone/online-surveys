from django.http import HttpResponse
from django.shortcuts import render
from os import environ
from pymongo import MongoClient
from bson.objectid import ObjectId

def index(request):
    
    skey = request.GET['skey']
    if (skey):
        dbserver = environ['DB_ADDRESS']
        dbport = environ['DB_PORT']
        
        client = MongoClient(dbserver, int(dbport))
        db = client.orange_cat
    
        #demo skey "5f5346a0bc92b6b1f6aa0e5c"
        answer = db.answers.find_one({"_id": ObjectId(skey)}) 
        
        if (answer):
            
            survey = db.surveys.find_one({"_id": ObjectId(answer['srv'])}) 
            
            if (survey):
                context = {
                    'id': skey,
                    'question_list': survey['questions'], 
                    'banner': survey['image'], 
                    'title': survey['name'], 
                    'submit': survey['submit']
                }
                
                #survay was saved already
                if ('done' in answer):
                    context['done'] = True
                    context.pop('question_list', None)
                    context.pop('submit', None)
                    return render(request, 'public/done.html', context)
        
    return render(request, 'public/index.html', context)

def save(request):
    
    id = request.POST['id']
    dbserver = environ['DB_ADDRESS']
    dbport = environ['DB_PORT']
    
    client = MongoClient(dbserver, int(dbport))
    db = client.orange_cat
    
    answer = db.answers.find_one({"_id": ObjectId(id)})     
    survey = db.surveys.find_one({"_id": ObjectId(answer['srv'])}) 
    
    survey
    
    context = {
        'banner': survey['image'], 
        'title': survey['name']
    }
    
    question_list = []
    questions = survey['questions']
    
    for q in questions:
        questionId = q['id']
        value = request.POST[questionId]
        answ = {}
        answ['id'] = questionId
        answ['value'] = value
        question_list.append(answ)
    
    db.answers.update({'_id': ObjectId(answer['_id'])},  {'$set': {"question_list": question_list, 'done': True}}) 

    return render(request, 'public/done.html', context)