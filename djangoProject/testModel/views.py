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
