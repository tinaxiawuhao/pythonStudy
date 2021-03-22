from django.http import HttpResponse
from testModel import models


def multi_add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))
    return HttpResponse(book)


def multi_add_book_2(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  获取出版社对象的id
    pk = pub_obj.pk
    #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    print(book, type(book))
    return HttpResponse(book)


def multi_add_book_3(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)
    return HttpResponse(book)


def multi_add_book_4(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    #  获取作者对象的id
    pk = chong.pk
    #  获取书籍对象
    book = models.Book.objects.filter(title="冲灵剑法").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    book.authors.add(pk)
    return HttpResponse(book)


# add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
# 注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
def add_1(request):
    book_obj = models.Book.objects.get(id=10)
    author_list = models.Author.objects.filter(id__gt=2)
    book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
    # 方式二：传对象 id
    book_obj.authors.add(*[1, 3])  # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中
    return HttpResponse("ok")


# add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
# 注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
def add_2(request):
    ying = models.Author.objects.filter(name="任盈盈").first()
    book = models.Book.objects.filter(title="冲灵剑法").first()
    ying.book_set.add(book)
    return HttpResponse("ok")


# create()：创建一个新的对象，并同时将它添加到关联对象集之中。
# 返回新创建的对象。
def create(request):
    pub = models.Publish.objects.filter(name="明教出版社").first()
    wo = models.Author.objects.filter(name="任我行").first()
    book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
    print(book, type(book))
    return HttpResponse("ok")


# remove()：从关联对象集中移除执行的模型对象。
# 对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。
def remove(request):
    author_obj = models.Author.objects.get(id=1)
    book_obj = models.Book.objects.get(id=11)
    author_obj.book_set.remove(book_obj)
    return HttpResponse("ok")


#  clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。
# 对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在。
# 无返回值。
def clear(request):
    book = models.Book.objects.filter(title="菜鸟教程").first()
    book.authors.clear()


# 查询主键为 1 的书籍的出版社所在的城市（正向）
def select_1(request):
    book = models.Book.objects.filter(pk=10).first()
    res = book.publish.city
    print(res, type(res))
    return HttpResponse("ok")


# 查询明教出版社出版的书籍名（反向）。
# 反向：对象.小写类名_set(pub.book_set) 可以跳转到关联的表(书籍表)。
# pub.book_set.all()：取出书籍表的所有书籍对象，在一个 QuerySet 里，遍历取出一个个书籍对象。
def select_2(request):
    pub = models.Publish.objects.filter(name="明教出版社").first()
    res = pub.book_set.all()
    for i in res:
        print(i.title)
    return HttpResponse("ok")


# 查询令狐冲的电话（正向）
# 正向：对象.属性 (author.au_detail) 可以跳转到关联的表(作者详情表)
def select_3(request):
    author = models.Author.objects.filter(name="令狐冲").first()
    res = author.au_detail.tel
    print(res, type(res))
    return HttpResponse("ok")


# 查询所有住址在黑木崖的作者的姓名（反向）。
# 一对一的反向，用 对象.小写类名 即可，不用加 _set。
# 反向：对象.小写类名(addr.author)可以跳转到关联的表(作者表)
def select_4(request):
    addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
    res = addr.author.name
    print(res, type(res))
    return HttpResponse("ok")


# 菜鸟教程所有作者的名字以及手机号（正向）。
# 正向：对象.属性(book.authors)可以跳转到关联的表(作者表)。
# 作者表里没有作者电话，因此再次通过对象.属性(i.au_detail)跳转到关联的表（作者详情表）。
def select_5(request):
    book = models.Book.objects.filter(title="菜鸟教程").first()
    res = book.authors.all()
    for i in res:
        print(i.name, i.au_detail.tel)
    return HttpResponse("ok")


# 查询任我行出过的所有书籍的名字（反向）。
def select_6(request):
    author = models.Author.objects.filter(name="任我行").first()
    res = author.book_set.all()
    for i in res:
        print(i.title)
    return HttpResponse("ok")


# 一对多
# 查询菜鸟出版社出版过的所有书籍的名字与价格。
def select_7(request):
    # 正向：属性名称__跨表的属性名称 反向：小写类名__跨表的属性名称
    res = models.Book.objects.filter(publish__name="菜鸟出版社").values_list("title", "price")
    # 反向：通过 小写类名__跨表的属性名称（book__title，book__price） 跨表获取数据。
    res = models.Publish.objects.filter(name="菜鸟出版社").values_list("book__title", "book__price")
    return HttpResponse("ok")


# 查询任我行出过的所有书籍的名字。
def select_8(request):
    # 正向：通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据：
    res = models.Book.objects.filter(authors__name="任我行").values_list("title")
    # 反向：通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：
    res = models.Author.objects.filter(name="任我行").values_list("book__title")
    return HttpResponse("ok")


# 查询任我行的手机号。
def select_9(request):
    # 正向：通过 属性名称__跨表的属性名称(au_detail__tel) 跨表获取数据。
    res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
    # 反向：通过 小写类名__跨表的属性名称（author__name） 跨表获取数据。
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")
    return HttpResponse("ok")
