from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import requests
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

warnings.filterwarnings(action='ignore')

# import gensim
from gensim.models import Word2Vec

#爬取alice.txt文档
sample = requests.get("http://www.gutenberg.org/files/11/11-0.txt")
s = sample.text

#将换行符变为空格
f = s.replace("\n", " ")

data = []   #存储的是单词表

#迭代文本中的每一句话
for i in sent_tokenize(f):
    temp = []

    #将句子进行分词
    for j in word_tokenize(i):
        temp.append(j.lower())  #存储的的时候全变为小写

    data.append(temp)




def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        # tokens.append(word)
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)
    # tsne_model.fit

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()


#创建CBOW模型
model1 = Word2Vec(data, min_count=1,size=200, window=7)   #忽略出现次数小于1的词，size是每个单词的词向量的维度

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@RESULT@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2')
# print("Cosine similarity between 'alice' " + "and 'wonderland' - CBOW : ", model1.similarity('alice', 'wonderland'))
tsne_plot(model1)