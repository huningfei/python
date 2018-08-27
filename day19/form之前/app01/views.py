from django.shortcuts import render,redirect
from app01 import models

# Create your views here.
def book_list(request):
    book_obj=models.Book.objects.all()
    return render(request,"book_list.html",{"book_obj":book_obj})

def add_book(request):
    if request.method=="GET":
        publisher_list=models.Publisher.objects.all()
        author_list=models.Author.objects.all()
        return render(request,"add_book.html",{"publisher_list":publisher_list,"author_list":author_list})
    else:
        title=request.POST.get("title")
        publish_data=request.POST.get("publish_date")
        phone=request.POST.get("phone")
        publisher=request.POST.get("publisher")
        authors=request.POST.getlist("authors")
        #去数据库创建
        book_obj=models.Book.objects.create(
            title=title,
            publisher_date=publish_data,
            publisher_id=publisher,
        )
        book_obj.authors.add(*authors)
        return redirect("/book_list/")
    
def edit_book(request,pk):
    book_obj = models.Book.objects.filter(id=pk).first()
    if request.method=="POST":     
        title = request.POST.get("title")
        publish_data = request.POST.get("publish_date")
        phone = request.POST.get("phone")
        publisher = request.POST.get("publisher")
        print(publisher)
        authors = request.POST.getlist("authors")
        book_obj.title=title
        book_obj.publish_date=publish_data
        book_obj.phone=phone
        book_obj.publisher_id=publisher
        book_obj.save()
        book_obj.authors.set(authors)
        return redirect("/book_list/")
    else:
        publisher_list=models.Publisher.objects.all()
        author_list=models.Author.objects.all()
        return render(request,"edit_book.html",locals())