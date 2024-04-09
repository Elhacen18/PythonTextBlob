from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path


#  Part 2
nltk.download('stopwords')
stop_words = list(stopwords.words('english'))
# print(stop_words)
def ReadAllFiles():
    MyList = []
    blob1 = TextBlob(Path('Taken_Or_Left_novel.txt').read_text())
    # items = blob1.word_counts.items()
    # print(len(items))
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
        WordList = [word for word in blob.words if word not in stop_words]
        MyBlobList.append(WordList)
        # print(blob)
    
    return MyBlobList
def GetWordCount(BlobList):
    # convert each sublit list of words to a string
    SubList = [' '.join(sublist) for sublist in BlobList]

    Dic_List = []
    for List in SubList: 
        blob = TextBlob(List)
        Wordcount = list(blob.word_counts.items())
        # print(Wordcount)
        Dic_List.append(Wordcount)
    return Dic_List

BlobList = ReadAllFiles()
MyList= RemoveStopWords(BlobList)
WordCount = GetWordCount(MyList)
print(len(WordCount[0]))
