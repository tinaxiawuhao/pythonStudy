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