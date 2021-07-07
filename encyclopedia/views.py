from django.shortcuts import render , redirect 
from django.db.models import Q 
from django.http import HttpResponseRedirect, HttpResponse
from django import forms 
import re

from . import util
import random 





def index(request):
    # Search functionality 
    if "q" in request.GET :
        q = request.GET["q"].lower()
        list_entries = []
        for i in util.list_entries():
            list_entries.append(i.lower())

        if q in list_entries :
            print("Total")
            return render(request, "encyclopedia/entry_page.html", {
            "page": util.get_entry(q),
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
                print("Try again")
                return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})

            
        else: 
            print("Error")
            return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


    else :
        print("cool")
        import random 
        choices = util.list_entries()
        choice_list = []
        for i in choices:
            choice_list.append(i)
        print(choice_list)
        random_choice = random.choice(choice_list)
        print(random_choice)

        return render(request ,"encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random_page": str(random_choice)
        })



def random(request):
    import random 
    choices = util.list_entries()
    choice_list = []
    for i in choices:
        choice_list.append(i)
    print(choice_list)
    random_page = random.choice(choice_list)
    print(random_page)
    return render(request ,"encyclopedia/entry_page.html",{
        "page": util.get_entry(random_page),
        "entry" : util.get_entry(random_page),
        "p_title": random_page
        } )

            



def entry_page(request , page):
    print(page)
    try :
        return render(request, "encyclopedia/entry_page.html", {
            "page": util.get_entry(page),
            "entry" : util.get_entry(page),
            "p_title": page
        })
    except :
        return render(request, "encyclopedia/pnf.html", {
            "p_title": str(page)
            })




def create(request):
    # Create functionality 
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


def edit(request, p_title):
    # Edit page functionality 
    object_to_modify = util.get_entry(p_title)
    print(object_to_modify)

    if request.method == "POST":
        new_text = request.POST.get('content')
        util.save_entry(p_title, new_text)
        print("Done")
        return render(request,"encyclopedia/entry_page.html", {
            "page": util.get_entry(p_title)
        }) 


    return render(request ,"encyclopedia/edit_page.html" , {
        "the_text": object_to_modify
        })


    









    
        





    







    








