from django.shortcuts import render
from django.db.models import Q 
from django.http import HttpResponseRedirect, HttpResponse
from django import forms 
import re

from . import util





def index(request):
    if "q" in request.GET :
        q = request.GET["q"].lower()
        list_entries = []
        for i in util.list_entries():
            list_entries.append(i.lower())

        if q in list_entries :
            print("Total")
            return render(request, "encyclopedia/entry_page.html", {
            "page": util.get_entry(q)
        })

        elif any(q in i for i in list_entries):
            print("Maybe")
            try:
                list_queries = []
                for individual_list in list_entries :
                    if q in individual_list:
                        list_queries.append(individual_list)

                return render(request, "encyclopedia/index.html", {
        "list_queries": list_queries})
            except:
                print("yay , try again")
                return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})

            
        else: 
            print("Nothing")
            return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    else :
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})




def entry_page(request , page):
    try :
        return render(request, "encyclopedia/entry_page.html", {
            "page": util.get_entry(page),
            "entry" : util.get_entry(page)
        })
    except :
        return render(request, "encyclopedia/pnf.html", {})




def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        list_entries = util.list_entries()
        print(f'{title}:{content}')
        try:
            for entry in util.list_entries():
                if entry.lower() == title.lower() :
                    return HttpResponse("Unfortunately ,your page already exists")
            util.save_entry(title, content)
            return render(request , "encyclopedia/entry_page.html", {
                "page": util.get_entry(title),
                "entry" : util.get_entry(title)
                })
        except:
            return render(request , "encyclopedia/pnf.html", {})


    return render(request , "encyclopedia/pnf.html", {})









    
        





    







    








