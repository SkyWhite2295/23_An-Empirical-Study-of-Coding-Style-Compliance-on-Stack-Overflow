# 导入第三方模块

import pandas as pd

import matplotlib.pyplot as plt

# 读取数据集

y1 = pd.read_csv('D:/北工大/2021第一学期/毕设/python/Scripts/answer/RQ3.4sum_all_new_vioratio_py.csv', encoding='gb2312', low_memory=False)
y2 = pd.read_csv('D:/北工大/2021第一学期/毕设/python/Lib/site-packages/answer/RQ3.4sum_all_new_vioratio_c.csv', encoding='gb2312', low_memory=False)
y3 = pd.read_csv('D:/北工大/2021第一学期/毕设/JavaScript/answer/js_reports/RQ3.4sum_all_new_vioratio_js.csv', encoding='gb2312', low_memory=False)
# y4 = pd.read_csv('C_RQ3_grouping_vio=7~15.csv', encoding='gb2312')
# y5 = pd.read_csv('C_RQ3_grouping_vio大于15.csv', encoding='gb2312')
# y6 = pd.read_csv('RQ3_sum_all_new.csv', encoding='gb2312')

# 检查属性值是否有缺失

any(y1.VioRatio.isnull())
any(y2.VioRatio.isnull())
any(y3.VioRatio.isnull())
# any(y4.ViewCount.isnull())
# any(y5.ViewCount.isnull())
# any(y6.Score.isnull())

# 不妨删除含有缺失属性值的观察

y1.dropna(subset=['VioRatio'], inplace=True)
y2.dropna(subset=['VioRatio'], inplace=True)
y3.dropna(subset=['VioRatio'], inplace=True)
# y4.dropna(subset=['ViewCount'], inplace=True)
# y5.dropna(subset=['ViewCount'], inplace=True)
# y6.dropna(subset=['Score'], inplace=True)
# 设置图形的显示风格

plt.style.use('ggplot')
# print(y2.CommentCount)
# 设置中文和负号正常显示

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'

plt.rcParams['axes.unicode_minus'] = False


# 绘图：整体属性值的箱线图
data = pd.DataFrame({"python": y1.VioRatio, "C/C++": y2.VioRatio, "JavaScript": y3.VioRatio, })
                     # "2": y2.ViewCount, "3": y3.ViewCount, "4": y4.ViewCount, "5": y5.ViewCount, })
# data.boxplot()
data.boxplot(
            patch_artist=True,  # 要求用自定义颜色填充盒形图，默认白色填充

            showmeans=True,  # 以点的形式显示均值

            boxprops={'color': 'black', 'facecolor': 'pink'},  # 设置箱体属性，填充色和边框色

            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'color': 'black'},  # 设置异常值属性，点的形状、填充色和边框色

            meanprops={'marker': 'D', 'markerfacecolor': 'orange'},  # 设置均值点的属性，点的形状、填充色

            medianprops={'linestyle': '--', 'color': 'green'})  # 设置中位数线的属性，线的类型和颜色


# 设置y轴的范围

plt.ylim(-0.5, 6)

# 设置箱线图的横坐标标题
plt.xlabel("ViolationRatio")

# 去除箱线图的上边框与右边框的刻度标签

plt.tick_params(top='off', right='off')

# 显示图形

plt.show()