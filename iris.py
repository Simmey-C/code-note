import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['STHeiti']


def standardize(x):
    mean = np.mean(x, axis=0)
    std = np.std(x, axis=0)
    return (x - mean) / std

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))


class kmeans:
    def __init__(self, n_clusters=3, random_state=42, max_iter=100, tol=1e-4,):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None
        self.labels = None

    def fit(self, x):
        np.random.seed(self.random_state)
        n_samples, n_features = x.shape

        random_indices = np.random.permutation(n_samples)[:self.n_clusters]
        self.centroids = x[random_indices].copy()

        for k in range(self.max_iter):
            self.labels = np.zeros(n_samples)
            for i in range(n_samples):
                distances = [euclidean_distance(centroid, x[i]) for centroid in self.centroids]
                self.labels[i] = np.argmin(distances)

            new_centroids = np.zeros((self.n_clusters, n_features))
            for i in range(self.n_clusters):
                sample =  x[self.labels == i]
                if len(sample) > 0:
                    new_centroids[i] = np.mean(sample, axis=0)
                else:
                    new_centroids[i] = x[np.random.randint(n_samples)]

            centroid_distance = np.sum([euclidean_distance(new_centroids[i], self.centroids[i]) for i in range(self.n_clusters)])
            self.centroids = new_centroids
            if centroid_distance < self.tol:
                break


def silhouette_score(x, labels):
    n_samples = x.shape[0]
    silhouette_vals = np.zeros(n_samples)

    for i in range(n_samples):
        same_cluster = x[labels == labels[i]]
        if len(same_cluster) == 1:
            a_i = 0
        else:
            a_i = np.mean([euclidean_distance(x[i], sample) for sample in same_cluster if
                           not np.array_equal(sample, x[i])])

        b_i = np.inf
        n_clusters = len(np.unique(labels))
        for k in range(n_clusters):
            if k == labels[i]:
                continue
            other_cluster = x[labels == k]
            if len(other_cluster) == 0:
                continue
            dist = np.mean([euclidean_distance(x[i], sample) for sample in other_cluster])
            if dist < b_i:
                b_i = dist

        silhouette_vals[i] = (b_i - a_i) / max(a_i, b_i)

    return np.mean(silhouette_vals)

def adjusted_rand_index(y_true, y_pred):
    true_labels = np.unique(y_true)
    true_map = {label: i for i, label in enumerate(true_labels)}
    y_true_num = np.array([true_map[label] for label in y_true])

    n = len(y_true_num)
    max_true = int(np.max(y_true_num))
    max_pred = int(np.max(y_pred))
    contingency = np.zeros((max_true + 1, max_pred + 1))
    for i in range(n):
        contingency[int(y_true_num[i]), int(y_pred[i])] += 1

    a = np.sum(contingency, axis=1)
    b = np.sum(contingency, axis=0)

    sum_comb_c = np.sum(contingency * (contingency - 1) / 2)
    sum_comb_a = np.sum(a * (a - 1) / 2)
    sum_comb_b = np.sum(b * (b - 1) / 2)
    expected = (sum_comb_a * sum_comb_b) / (n * (n - 1) / 2)
    max_val = (sum_comb_a + sum_comb_b) / 2
    return (sum_comb_c - expected) / (max_val - expected)

def calinski_harabasz_score(x, labels):
    n_samples = x.shape[0]
    n_clusters = len(np.unique(labels))
    centroids = np.array([np.mean(x[labels == k], axis=0) for k in range(n_clusters)])
    overall_mean = np.mean(x, axis=0)

    between_ss = 0
    for k in range(n_clusters):
        n_k = np.sum(labels == k)
        between_ss += n_k * np.sum((centroids[k] - overall_mean) ** 2)

    within_ss = 0
    for i in range(n_samples):
        within_ss += np.sum((x[i] - centroids[int(labels[i])]) ** 2)

    ch = (between_ss / (n_clusters - 1)) / (within_ss / (n_samples - n_clusters))
    return ch

if __name__ == '__main__':
    iris = pd.read_csv('iris.csv', header=None,
                       names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
    x = iris.iloc[:, :-1].values
    y = iris.iloc[:, -1].values
    x_std = standardize(x)

    kmeans = kmeans()
    kmeans.fit(x_std)
    y_pred = kmeans.labels.astype(int)

    # kmeans模型评估
    sil_score = silhouette_score(x_std, y_pred)
    ari_score = adjusted_rand_index(y, y_pred)
    ch_score = calinski_harabasz_score(x_std, y_pred)
    print('K-Means模型评估结果：')
    print(f"轮廓系数 Silhouette Score: {sil_score:.4f}")
    print(f"调整兰德指数 ARI: {ari_score:.4f}")
    print(f"Calinski-Harabasz指数: {ch_score:.4f}")


    plt.figure(figsize=(5, 10))
    plt.subplot(2, 1, 1)
    for k in range(3):
        plt.scatter(x_std[y_pred == k, 0], x_std[y_pred == k, 1], label=f"簇{k + 1}", alpha=0.7)
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], marker="X", s=200, c="black", label="簇中心")
    plt.xlabel("花萼长度 (标准化)")
    plt.ylabel("花萼宽度 (标准化)")
    plt.title("K-Means聚类结果（原始特征）")
    plt.legend()

    # 2. 真实标签对比
    plt.subplot(2, 1, 2)
    for species in np.unique(y):
        plt.scatter(x_std[y == species, 0], x_std[y == species, 1],
                    label=species, alpha=0.7)
    plt.xlabel("花萼长度 (标准化)")
    plt.ylabel("花萼宽度 (标准化)")
    plt.title("真实标签分布（原始特征）")
    plt.legend()

    plt.tight_layout()
    plt.savefig("task2_kmeans_result.png", dpi=300)
    plt.show()
