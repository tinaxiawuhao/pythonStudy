from django import forms
from django.core.exceptions import ValidationError
from testModel import models
from django.shortcuts import render, HttpResponse, redirect


class EmpForm(forms.Form):
    name = forms.CharField(min_length=5, label="姓名", error_messages={"required": "该字段不能为空!",
                                                                     "min_length": "用户名太短。"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(max_digits=5, decimal_places=2, label="工资")
    r_salary = forms.DecimalField(max_digits=5, decimal_places=2, label="请再输入工资")

    def clean_name(self):  # 局部钩子
        val = self.cleaned_data.get("name")

        if val.isdigit():
            raise ValidationError("用户名不能是纯数字")
        elif models.Emp.objects.filter(name=val):
            raise ValidationError("用户名已存在！")
        else:
            return val

    def clean(self):  # 全局钩子 确认两次输入的工资是否一致。
        val = self.cleaned_data.get("salary")
        r_val = self.cleaned_data.get("r_salary")

        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认工资是否一致。")


def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})