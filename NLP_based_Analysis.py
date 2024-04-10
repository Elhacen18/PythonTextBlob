from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path
from operator import itemgetter
import matplotlib.pyplot as plt 

Stops =['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

#  Part 2a
nltk.download('stopwords')
stop_words = list(stopwords.words('english'))
# print(stop_words)
fileName = ['Taken_Or_Left_novel.txt','Catching_of_the_whale_and_seal.txt','Extramammary_Articale.txt']
def ReadAllFiles():
    MyList = []
    blob1 = TextBlob(Path('Taken_Or_Left_novel.txt').read_text())
    MyList.append(blob1)
    blob2 = TextBlob(Path('Catching_of_the_whale_and_seal.txt').read_text())
    MyList.append(blob2)
    blob3 = TextBlob(Path('Extramammary_Articale.txt').read_text())
    MyList.append(blob3)
    return MyList
def RemoveStopWords(BlobList):
    # print(BlobList)
    WordList = []
    MyBlobList = []
    # print(len(BlobList[0]))
    for blob in BlobList:
        WordList = [word.lower() for word in blob.words if word.lower() not in stop_words]
        # WordList = [word for word in blob.words if word not in stop_words]
        MyBlobList.append(WordList)   
    # print(MyBlobList[2]) 
    return MyBlobList
def GetWordCount(BlobList):
    # convert each sublit list of words to a string
    SubList = [' '.join(sublist) for sublist in BlobList]

    Dic_List = []
    for List in SubList: 
        blob = TextBlob(List)
        Wordcount = list(blob.word_counts.items())
        Dic_List.append(Wordcount)
    return Dic_List
def Top25WordsPlot(list):
    top25Words = []
    for item in list:
        sorted_items = sorted(item, key=itemgetter(1), reverse=True)
        top25Words.append(sorted_items[:25])
    print("=========================================")

    fig, axis = plt.subplots(3,1,figsize=(16, 8))
    for i, ax in enumerate( axis.flat):
    
        keys_list = [key for key in dict(top25Words[i])]
        values_list = [dict(top25Words[i])[key] for key in dict(top25Words[i])]

        ax.bar(keys_list, values_list, color='green')
        ax.set_title(f'{fileName[i]} top 25 words')
        ax.set_xlabel('word')
        ax.set_ylabel('Count')
        ax.tick_params(labelrotation=90)  # Rotate labels for better readability
        ax.tick_params(labelbottom=True)
        fig.tight_layout(pad=10.0)
        plt.tight_layout()
    plt.show()
    return top25Words

BlobList = ReadAllFiles()
MyList= RemoveStopWords(BlobList)
FileWordCount = GetWordCount(MyList)
# Part 2b
Top25WordsPlot(FileWordCount)
# print(FileWordCount)
# Part 2c
print(len(FileWordCount))
# print(list(WordCount[1]))
