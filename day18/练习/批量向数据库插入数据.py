import os
import django
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "练习.settings")
    django.setup()
    from app01 import models
    # 创建500个书籍对象
    book_list=[models.Book(title="贝多芬第{}交响曲".format(i),publisher_id=i) for i in range (500)]
    # 批量提交到数据库
    models.Book.objects.bulk_create(book_list)

     #批量添加出版社
    # publisher_list = [models.Publisher(name="沙河第{}出版社".format(i)) for i in range(502)]
    # models.Publisher.objects.bulk_create(publisher_list, batch_size=30)