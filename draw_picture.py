from pyecharts import Bar
bar =Bar("我的第一个图表", "爬虫分析")
bar.add("二手物品发帖和数量", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [1, 2, 3, 4, 5, 6])
bar.render(path="static/charts/charts.png")


