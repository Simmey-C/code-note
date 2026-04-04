import requests

wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_data = requests.get(wine_url).content
with open("winequality-red.csv", "wb") as f:
    f.write(wine_data)
print("红酒数据集下载完成")

iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = requests.get(iris_url).content
with open("iris.csv", "wb") as f:
    f.write(iris_data)
print("鸢尾花数据集下载完成")