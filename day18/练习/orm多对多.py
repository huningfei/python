import os
if __name__=='__main__':
    if __name__ == '__main__':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "练习.settings")

        import django

        django.setup()
        from app01 import models

        # add方法和set方法
        '''
        author_obj=models.Author.objects.first()
        ret=author_obj.books.first().title
        print(ret)

        author_obj.books.set([2,502,503,501]) # 为作者添加三本书 作者id在前，书名id在后
        author_obj.books.add(504) # add在原来的基础上增加  set删除原来的然后在设置新的
        ret=author_obj.books.all().values_list("title")
        print(ret)
        '''

     #查询操作
    # 查询第一个作者写过书的名字
    #1 基于对象的查询正向查找
    ret=models.Author.objects.first().books.all().values("title")
    print(ret)
    #基于对象的反向查找  # 默认按照表名_set.all()
    ret = models.Book.objects.last().authors.all().values("name")
    print(ret)


    #基于queryset的双下滑线查询
    # ret = models.Author.objects.filter(id=2).values("books__title") #查询id为2作者写的书
    # print(ret)

    # 基于queryset的双下滑线的反向查找，由书找作者（两张写法）
    res=models.Book.objects.filter(id=504).values_list("authors__name")
    res1=models.Book.objects.filter(id=504).values("authors__name")
    # print(res,res1)

