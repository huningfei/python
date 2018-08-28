from django.shortcuts import render,redirect
from app01 import models
from app01.forms import BookForm
import datetime

# Create your views here.

def book_list(request):
    print(request.user.username,type(request.user))
    data=models.Book.objects.all()
    return render(request,"book_list.html",locals())


def add_book(request):
    form_obj=BookForm()
    if request.method=="POST":
        form_obj=BookForm(request.POST)
        if form_obj.is_valid(): #做数据有效性校验
            # 因为有多对多的字段，所以需要额外处理
            authors=form_obj.cleaned_data.pop("authors")
            # 创建新书籍对象
            book_obj=models.Book.objects.create(**form_obj.cleaned_data)
            # 讲书籍对象和作者建立关联
            book_obj.authors.add(*authors)

            return redirect("/book_list/")
    return render(request,"add_book.html",locals())

def edit_book(request,pk):
    book_obj=models.Book.objects.filter(id=pk).first()
    from django.forms import model_to_dict
    book_dict=model_to_dict(book_obj)
    book_dict["publisher_date"]=book_obj.publisher_date.strftime("%Y-%m-%d")

    form_obj=BookForm(book_dict)
    if request.method=="POST":
        form_obj=BookForm(request.POST)
        if form_obj.is_valid():
            book_obj.title=form_obj.cleaned_data.get("title")
            book_obj.publisher_id=form_obj.cleaned_data.get("publisher_date")
            book_obj.publisher_id=form_obj.cleaned_data.get("publisher")
            book_obj.save()
            book_obj.authors.set(form_obj.cleaned_data.get("authors"))
            return redirect("/book_list")
    return render(request,"edit_book.html",locals())

def del_book(request,pk):
     models.Book.objects.filter(id=pk).delete()
     return redirect("/book_list")


