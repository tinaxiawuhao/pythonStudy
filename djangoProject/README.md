### 创建项目
```
django-admin.py startproject HelloWorld
```
### 启动服务器
```
python manage.py runserver 127.0.0.1:8000
```
### 定义模型
```
django-admin.py startapp testModel
```

1. settings.py中修改
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testModel',               # 添加此项
)
```

2. 路由分发
```python
from django.contrib import admin
from django.urls import path,include # 从 django.urls 引入 include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("testModel/", include("testModel.urls")),
]
```
```python
from django.urls import path,re_path
from testModel import views

urlpatterns = [
    path('insertdb/', views.insertdb),
    re_path("^xxx/(?P[0-9]{4})/$", views.xxx), 
]
```
### 创建原始表结构
```
python manage.py migrate
```

1. 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
```
import pymysql
pymysql.install_as_MySQLdb()
```

2. models.py创建模型
```python
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32) # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE) # 出版社名称
    pub_date = models.DateField() # 出版时间
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
```
### 模型变更刷新
```
python manage.py makemigrations testModel
```
### 创建自定义表结构
```
python manage.py migrate testModel
```

### 数据库单表操作
```python
from django.http import HttpResponse
from testModel.models import Test,Book


# 数据库操作
def insertdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 数据库操作
def selectdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Test.objects.order_by('name')[0:2]

    # 数据排序
    response5 = Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    response6 = Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作
def updatedb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


# 数据库操作
def deletedb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


def add_book(request):
    book = Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")


def create_book(request):
    books = Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
    print(books, type(books)) # Book object (18)
    return HttpResponse("<p>数据添加成功！"+books+"</p>")


def find_book(request):
    books = Book.objects.all()
    print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    return HttpResponse("<p>查找成功！"+books+"</p>")


def exclude_book(request):
    books = Book.objects.exclude(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = Book.objects.exclude(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse("<p>查找成功！"+books+"</p>")


def get_book(request):
    books = Book.objects.get(pk=5)
    books = Book.objects.get(pk=18)  # 报错，没有符合条件的对象
    books = Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
    print(books, type(books))  # 模型类的对象
    return HttpResponse("<p>查找成功！"+books+"</p>")


def order_by_book(request):
    books = Book.objects.order_by("price") # 查询所有，按照价格升序排列
    books = Book.objects.order_by("-price") # 查询所有，按照价格降序排列
    return HttpResponse("<p>查找成功！"+books+"</p>")


def reverse_book(request):
    # 按照价格升序排列：降序再反转
    books = Book.objects.order_by("-price").reverse()
    return HttpResponse("<p>查找成功！"+books+"</p>")


def count_book(request):
    books = Book.objects.count() # 查询所有数据的数量
    books = Book.objects.filter(price=200).count() # 查询符合条件数据的数量
    return HttpResponse("<p>查找成功！"+books+"</p>")


def first_book(request):
    books = Book.objects.first() # 返回所有数据的第一条数据
    books = Book.objects.last()  # 返回所有数据的最后一条数据
    return HttpResponse("<p>查找成功！"+books+"</p>")


def exists_book(request):
    books = Book.objects.exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
    books = Book.objects.count().exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    books = Book.objects.first().exists()
    return HttpResponse("<p>查找成功！"+books+"</p>")


def values_book(request):
    # 查询所有的id字段和price字段的数据
    books = Book.objects.values("pk","price")
    print(books[0]["price"],type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse("<p>查找成功！"+books+"</p>")


def values_list_book(request):
    # 查询所有的price字段和publish字段的数据
    books = Book.objects.values_list("price","publish")
    print(books)
    print(books[0][0],type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse("<p>查找成功！"+books+"</p>")


def distinct_book(request):
    # 查询一共有多少个出版社
    books = Book.objects.values_list("publish").distinct() # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
    books = Book.objects.distinct()
    return HttpResponse("<p>查找成功！"+books+"</p>")


def filter_book(request):
    books = Book.objects.filter(publish='菜鸟出版社', price=300)
    # 查询价格为200或者300的数据
    books = Book.objects.filter(price__in=[200,300])
    # 查询价格大于200的数据
    books = Book.objects.filter(price__gt=200)
    # 查询价格大于等于200的数据
    books = Book.objects.filter(price__gte=200)
    # 查询价格小于300的数据
    books = Book.objects.filter(price__lt=300)
    # 查询价格小于等于300的数据
    books = Book.objects.filter(price__lte=300)
    # 包含
    books = Book.objects.filter(title__contains="菜")
    # 不区分大小写
    books = Book.objects.filter(title__icontains="python")
    # 以...开头
    books = Book.objects.filter(title__startswith="菜")
    # 以...结尾
    books = Book.objects.filter(title__endswith="教程")
    books = Book.objects.filter(pub_date__year=2008)
    books = Book.objects.filter(pub_date__month=10)
    books = Book.objects.filter(pub_date__day=1)
    return HttpResponse("<p>查找成功！</p>")


def update_book(request):
    books = Book.objects.filter(pk__in=[7,8]).update(price=888)
    return HttpResponse(books)

```
### 数据库多表操作
```python
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

```
### 数据库聚合查询
```python
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数
from testModel import models
from django.db.models import F
from django.db.models import Q


def query(request):
    # 计算所有图书的平均价格:
    res = models.Book.objects.aggregate(Avg("price"))
    print(res, type(res))
    # 计算所有图书的数量、最贵价格和最便宜价格:
    res = models.Book.objects.aggregate(c=Count("id"), max=Max("price"), min=Min("price"))
    print(res, type(res))
    # 统计每一个出版社的最便宜的书的价格：
    # <QuerySet [{'name': '菜鸟出版社', 'in_price': Decimal('100.00')}, {'name': '明教出版社', 'in_price': Decimal('300.00')}]>
    res = models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
    print(res)
    # 统计每一本书的作者个数：
    # < QuerySet[{'title': '菜鸟教程', 'number': 1}, {'title': '吸星大法', 'number': 1}, {'title': '冲灵剑法', 'number': 1}] >
    res = models.Book.objects.annotate(number=Count("authors__name")).values("title", "number")
    print(res)
    # 统计每一本以"菜"开头的书籍的作者个数：
    res = models.Book.objects.filter(title__startswith="菜").annotate(c=Count("authors__name")).values("title", "c")
    print(res)
    # 统计不止一个作者的图书名称：
    # < QuerySet[{'title': '菜鸟教程', 'c': 1}, {'title': '吸星大法', 'c': 1}, {'title': '冲灵剑法', 'c': 1}] >
    res = models.Book.objects.annotate(c=Count("authors__name")).filter(c__gt=0).values("title", "c")
    print(res)
    # 根据一本图书作者数量的多少对查询集QuerySet进行降序排序:
    res = models.Book.objects.annotate(c=Count("authors__name")).order_by("-c").values("title", "c")
    print(res)
    # 查询各个作者出的书的总价格:
    res = models.Author.objects.annotate(all=Sum("book__price")).values("name", "all")
    print(res)


def query_2(request):
    # F动态获取对象字段的值，可以进行运算。
    # Django支持F()对象之间以及F()对象和常数之间的加减乘除和取余的操作。
    # 修改操作（update）也可以使用F()函数。
    # 查询工资大于年龄的人：
    book = models.Emp.objects.filter(salary__gt=F("age")).values("name", "age")
    print(book)
    # 将每一本书的价格提高100元:
    res = models.Book.objects.update(price=F("price") + 100)
    print(res)


def query_3(request):
    # 之前构造的过滤器里的多个条件的关系都是 and，如果需要执行更复杂的查询（例如 or 语句），就可以使用 Q 。
    # Q 对象可以使用 & | ~ （与 或 非）操作符进行组合。
    # 优先级从高到低：~ & |。
    # 可以混合使用 Q 对象和关键字参数，Q 对象和关键字参数是用"and"拼在一起的（即将逗号看成 and ），但是 Q 对象必须位于所有关键字参数的前面。
    # 查询价格大于 350 或者名称以菜开头的书籍的名称和价格。
    res = models.Book.objects.filter(Q(price__gt=350) | Q(title__startswith="菜")).values("title", "price")
    print(res)
    # 查询以"菜"结尾或者不是 2010 年 10 月份的书籍:
    res = models.Book.objects.filter(Q(title__endswith="菜") | ~Q(Q(pub_date__year=2010) & Q(pub_date__month=10)))
    print(res)
    # 查询出版日期是 2004 或者 1999 年，并且书名中包含有"菜"的书籍。
    # Q 对象和关键字混合使用，Q 对象要在所有关键字的前面:
    res = models.Book.objects.filter(Q(pub_date__year=2004) | Q(pub_date__year=1999), title__contains="菜")
    print(res)  
```