from flask import Flask, render_template,request

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    my_int = 18
    my_str = 'curry'
    my_list = [1, 5, 4, 3, 2]
    my_dict = {
        'name': 'durant',
        'age': 28
    }

    # render_template方法:渲染模板
    # 参数1: 模板名称  参数n: 传到模板里的数据
    return render_template('hello.html',
                           my_int=my_int,
                           my_str=my_str,
                           my_list=my_list,
                           my_dict=my_dict)


@app.route('/student')
def student():
   return render_template('student.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
  
if __name__ == '__main__':
    app.run(debug=True)