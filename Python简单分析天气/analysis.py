# 天气分析脚本

from PIL import Image, ImageDraw, ImageFont
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Geo
from pyecharts.charts import Grid, Liquid
from pyecharts.charts import Line
from pyecharts.charts import Map
from pyecharts.charts import Pie
from pyecharts.charts import Radar

from Get_Weather import Query

qr = Query()


# 天气预报图
def draw_weather_pic(city_name):
	data = qr.get_data(city_name)
	weather = data['weather']
	temperature = data['Ltemperature'] + '~' + data['Htemperature'] + '℃'
	img = Image.open('./mask.jpg')
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(u'./font/simkai.ttf', size=50)
	draw.text((img.size[0]/6, img.size[1]/5), temperature, font=font, fill=(0, 177, 106))
	draw.text((img.size[0]/3, img.size[1]/5+150), weather, font=font, fill=(0, 128, 131))
	img.save('results/weather.jpg','jpeg')
	print('[INFO]:draw_weather_pic done...')

# 柱状图
def DrawBar(city_names):
	bar = Bar()
	values1 = []
	values2 = []
	for cn in city_names:
		data = qr.get_data(cn)
		values1.append(data['Htemperature'])
		values2.append(data['Ltemperature'])
	bar.add_xaxis(city_names)
	bar.add_yaxis('最高气温', values1)
	bar.add_yaxis('最低气温', values2)
	bar.set_global_opts(title_opts=opts.TitleOpts(title="城市气温柱状图", subtitle="我是副标题"),toolbox_opts=opts.ToolboxOpts())
	# bar.render_notebook()
	bar.render('results/weatherBar.html')


# 地理坐标系
def DrawGeo(city_names):
	faker={}
	for cn in city_names:
		temp = qr.get_data(cn)
		faker[cn]=temp["rh"]

	c = (
		Geo()
			.add_schema(maptype="china")
			.add("geo", [list(z) for z in zip(faker.keys(), faker.values())])
			.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
			.set_global_opts(title_opts=opts.TitleOpts(title="全国主要城市空气质量"))
			.render("results/weatherGeo.html")
	)


# 折线图
def DrawLine(city_names):
	line = Line()
	hMap={}
	lMap={}
	for cn in city_names:
		data = qr.get_data(cn)
		hMap[cn] = data['Htemperature']
		lMap[cn] = data['Ltemperature']

	line.add_xaxis(xaxis_data=list(hMap.keys()))  # xaxis_data -- x轴数据
	# series_name -- 名称    y_axis -- y轴数据    areastyle_opts -- 产生面积阴影 （opacity -- 透明度 0-1由浅至深）
	line.add_yaxis(series_name="高气温", y_axis=list(hMap.values()), areastyle_opts=opts.AreaStyleOpts(opacity=0.1))
	line.add_yaxis(series_name="低气温", y_axis=list(lMap.values()), areastyle_opts=opts.AreaStyleOpts(opacity=0.2))
	line.set_global_opts(title_opts=opts.TitleOpts(title="标题"))  # 标题
	line.render('results/weatherLine.html')


# 水球图
def DrawLiquid(city_name):
	data = int(qr.get_data(city_name)['SD'].strip('%')) / 100
	l1 = (
		Liquid()
			.add("lq", [data], center=["60%", "50%"])
			.set_global_opts(title_opts=opts.TitleOpts(title='%s城市湿度' % city_name))
	)

	grid = Grid().add(l1, grid_opts=opts.GridOpts())
	grid.render("results/weatherLiquid.html")



# 地图
def DrawMap(city_names):
	values = {}
	for cn in city_names:
		data = qr.get_data(cn)
		values[cn]=data['Htemperature']

	c = (
		Map()
			.add("温度", [list(z) for z in zip(values.keys(), values.values())], "china")
			.set_global_opts(title_opts=opts.TitleOpts(title="最高温度"))
			.render("results/weatherMap.html")
	)


# 饼图
def DrawPie(city_names):
	values = {}
	for cn in city_names:
		data = qr.get_data(cn)
		values[cn] = data['rh']

	c = (
		Pie()
			.add("", [list(z) for z in zip(values.keys(), values.values())])
			.set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
			.set_global_opts(title_opts=opts.TitleOpts(title="部分城市相对气压饼图"))
			.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
			.render("results/weatherPie.html")
	)


# 雷达图
def DrawRadar():
	v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
	v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
	(
		Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
			.add_schema(
			schema=[
				opts.RadarIndicatorItem(name="销售（sales）", max_=6500),
				opts.RadarIndicatorItem(name="管理（Administration）", max_=16000),
				opts.RadarIndicatorItem(name="信息技术（Information Technology）", max_=30000),
				opts.RadarIndicatorItem(name="客服（Customer Support）", max_=38000),
				opts.RadarIndicatorItem(name="研发（Development）", max_=52000),
				opts.RadarIndicatorItem(name="市场（Marketing）", max_=25000),
			],
			splitarea_opt=opts.SplitAreaOpts(
				is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
			),
			textstyle_opts=opts.TextStyleOpts(color="#fff"),
		)
			.add(
			series_name="预算分配（Allocated Budget）",
			data=v1,
			linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
		)
			.add(
			series_name="实际开销（Actual Spending）",
			data=v2,
			linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),
		)
			.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
			.set_global_opts(
			title_opts=opts.TitleOpts(title="基础雷达图"), legend_opts=opts.LegendOpts()
		)
			.render("results/weatherRadar.html")
	)





if __name__ == '__main__':
	# city_names = ['上海', '北京', '南京', '杭州', '天津', '武汉']
	city_names = ['上海', '北京', '南京', '杭州', '天津', '武汉', '苏州', '哈尔滨', '长春', '深圳', '西安', '南宁', '包头', '合肥', '成都', '乌鲁木齐', '西宁']
	# city_names = ['北京', '天津', '上海', '重庆',
	# 			  '石家庄', '太原', '沈阳', '长春',
	# 			  '哈尔滨', '南京', '杭州', '合肥',
	# 			  '福州', '南昌', '济南', '郑州',
	# 			  '武汉', '长沙', '广州', '成都']
	draw_weather_pic('济南')
	DrawBar(city_names)
	DrawGeo(city_names)
	DrawLine(city_names)
	DrawLiquid('北京')
	DrawMap(city_names)
	DrawPie(city_names)
	DrawRadar()
