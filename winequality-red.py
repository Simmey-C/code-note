import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['STHeiti']


def train_test_split(x, y, test_size = 0.2, random_state = 42):
    np.random.seed(random_state)
    n_sample = x.shape[0]
    test_sample = int(n_sample * test_size)
    index = np.random.permutation(n_sample)
    x_test = x[index[:test_sample]]
    x_train = x[index[test_sample:]]
    y_test = y[index[:test_sample]]
    y_train = y[index[test_sample:]]
    return x_train, x_test, y_train, y_test


def standardize(x_train, x_test):
    mean = np.mean(x_train, axis=0)
    std = np.std(x_train, axis=0)
    x_train_std = (x_train - mean) / std
    x_test_std = (x_test - mean) / std
    return x_train_std, x_test_std


class LinearRegression:
    def __init__(self, b = True):
        self.b = b
        self.theta = None

    def fit(self, x, y):
        if self.b :
            x = np.hstack([np.ones((x.shape[0], 1)), x])
        self.theta = np.linalg.inv(x.T @ x) @ x.T @ y

    def predict(self, x):
        if self.b :
            x = np.hstack([np.ones((x.shape[0], 1)), x])
        return x @ self.theta


    def mse(self, y_test, y_pred):
        return np.mean((y_test - y_pred)**2)

    def rmse(self, y_test, y_pred):
        return np.sqrt(self.mse(y_test, y_pred))

    def mae(self, y_test, y_pred):
        return np.mean(np.abs(y_test - y_pred))

    def r2_score(self, y_test, y_pred):
        ss_res = np.sum((y_test - y_pred)**2)
        ss_tot = np.sum((y_test - np.mean(y_test))**2)
        return 1 - (ss_res / ss_tot)



class LogisticRegression:
    def __init__(self, b = True, learning_rate = 0.01, n_iters = 10000):
        self.b = b
        self.theta = None
        self.learning_rate = learning_rate
        self.n_iters = n_iters

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, x, y):
        if self.b :
            x = np.hstack([np.ones((x.shape[0], 1)), x])
        n_sample, n_feature= x.shape
        self.theta = np.zeros(n_feature)
        for _ in range(self.n_iters):
            z = x @ self.theta
            y_prob = self.sigmoid(z)
            gradient = (1 / n_sample) * x.T @ (y_prob - y)
            self.theta -= self.learning_rate * gradient

    def predict_prob(self, x):
        if self.b :
            x = np.hstack([np.ones((x.shape[0], 1)), x])
        z = x @ self.theta
        y_prob = self.sigmoid(z)
        return y_prob

    def predict(self, x, threshold=0.5):
        y_prob = self.predict_prob(x)
        y_pred = (y_prob >= threshold).astype(int)
        return y_pred


    def confusion_matrix(self, y_test, y_pred):
        TP = np.sum((y_test == 1) & (y_pred == 1))  # 真好酒
        TN = np.sum((y_test == 0) & (y_pred == 0))  # 真坏酒
        FP = np.sum((y_test == 0) & (y_pred == 1))  # 假好酒 = 坏酒
        FN = np.sum((y_test == 1) & (y_pred == 0))  # 假坏酒 = 好酒
        return np.array([[TN, FP], [FN, TP]])

    def accuracy(self, y_test, y_pred):  # 准确率
        cm = self.confusion_matrix(y_test, y_pred)
        accuracy = (cm[0, 0] + cm[1, 1]) / np.sum(cm)
        return accuracy

    def precision(self, y_test, y_pred):  # 精确率
        cm = self.confusion_matrix(y_test, y_pred)
        precision = cm[1, 1] / (cm[1, 1] + cm[0, 1])
        return precision

    def recall(self, y_test, y_pred):  # 召回率
        cm = self.confusion_matrix(y_test, y_pred)
        recall = cm[1, 1] / (cm[1, 1] + cm[1, 0])
        return recall

    def f1_score(self, y_test, y_pred):  # F1值
        precision = self.precision(y_test, y_pred)
        recall = self.recall(y_test, y_pred)
        f1_score = 2 * precision * recall / (precision + recall)
        return f1_score

    def roc_auc(self, y_test, y_prob):
        sorted_index = np.argsort(-y_prob)
        y_test_sorted = y_test[sorted_index]
        y_pred_sorted = y_prob[sorted_index]

        n_pos = np.sum(y_test == 1)
        n_neg = np.sum(y_test == 0)
        tp = 0
        fp = 0
        tpr = []
        fpr = []

        for i in range(len(y_test_sorted)):
            if y_test_sorted[i] == 1:
                tp += 1
            else:
                fp += 1
            tpr.append(tp / n_pos)
            fpr.append(fp / n_neg)

        auc = 0
        for i in range(1,len(fpr)):
            auc += (fpr[i] - fpr[i-1]) * (tpr[i] + tpr[i-1]) / 2
        return tpr, fpr, auc


if __name__ =='__main__':
    wine = pd.read_csv('winequality-red.csv', sep=';')  # 返回DataFrame数据框
    x = wine.iloc[:, :-1].values  # 得到特征x的数组
    y = wine.iloc[:, -1].values  # 得到标签y的数组
    y1 = (y > 6).astype(int)  # 将标签y大于6的样本标记为1，否则标记为0

    x_train, x_test, y_train, y_test = train_test_split(x, y)
    x_train_std, x_test_std = standardize(x_train, x_test)
    y1_train = (y_train > 6).astype(int)
    y1_test = (y_test > 6).astype(int)


    # 线性回归模型
    model = LinearRegression()
    model.fit(x_train_std, y_train)
    y_pred = model.predict(x_test_std)

    # 逻辑回归模型
    model1 = LogisticRegression()
    model1.fit(x_train_std, y1_train)
    y1_prob = model1.predict_prob(x_test_std)
    y1_pred = model1.predict(x_test_std)


    # 评估线性回归模型
    print('线性回归模型评估结果：')
    print(f'均方误差： {model.mse(y_test, y_pred) : .4f}')
    print(f'均方根误差： {model.rmse(y_test, y_pred) : .4f}')
    print(f'平均绝对误差： {model.mae(y_test, y_pred) : .4f}')
    print(f'R-squared： {model.r2_score(y_test, y_pred) : .4f}')

    # 评估逻辑回归模型
    print('逻辑回归模型评估结果：')
    print(f'混淆矩阵： {model1.confusion_matrix(y1_test, y1_pred)}')
    print(f'准确率： {model1.accuracy(y1_test, y1_pred) : .4f}')
    print(f'精确率： {model1.precision(y1_test, y1_pred) : .4f}')
    print(f'召回率： {model1.recall(y1_test, y1_pred) : .4f}')
    print(f'F1值： {model1.f1_score(y1_test, y1_pred) : .4f}')
    tpr, fpr, auc = model1.roc_auc(y1_test, y1_prob)
    print(f'ROC-AUC： {auc : .4f}')


    # 线性回归模型：真实值 vs 预测值
    plt.figure(figsize=(5, 10))
    plt.subplot(2, 1, 1)
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("真实质量评分")
    plt.ylabel("预测质量评分")
    plt.title("线性回归：真实值 vs 预测值")

    # 逻辑回归模型：ROC曲线
    plt.subplot(2, 1, 2)
    plt.plot(fpr, tpr, label=f"AUC = {auc:.4f}")
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.title("逻辑回归：ROC曲线")
    plt.legend()
    plt.tight_layout()
    plt.savefig("task1_evaluation.png", dpi=300)
    plt.show()