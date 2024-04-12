from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path
from operator import itemgetter
import matplotlib.pyplot as plt 
from wordcloud import WordCloud   
import imageio



# Stops =['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

#  Part 2a
nltk.download('stopwords')
stop_words = list(stopwords.words('english'))
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
    WordList = []
    MyBlobList = []
    for blob in BlobList:
        # "if not word.isdigit()"" will exclude any number in the text. 
        WordList = [word.lower() for word in blob.words if word.lower() not in stop_words if not word.isdigit()]
        MyBlobList.append(WordList)   
    return MyBlobList
def GetWordCount(BlobList):
    # convert each sublit list of words to a string so TextBlob can be used to get words count
    SubList = [' '.join(sublist) for sublist in BlobList]

    Dic_List = []
    for List in SubList: 
        blob = TextBlob(List)
        Wordcount = list(blob.word_counts.items())
        Dic_List.append(Wordcount)
    return Dic_List
def GetTop100Words(list):
    Top100words=[]
    for item in list:
        sorted_items = sorted(item, key=itemgetter(1), reverse=True)
    # add only top 100 words 
        Top100words.append(sorted_items[:100]) 
    
    return Top100words
def Top25WordsPlot(list):

    top25Words = []
    for item in list:
        sorted_items = sorted(item, key=itemgetter(1), reverse=True)
        # add only top 25 words 
        top25Words.append(sorted_items[:25]) 

    fig, axis = plt.subplots(3,1,figsize=(20, 8))
    for i, ax in enumerate( axis.flat):
    
        keys_list = [key for key in dict(top25Words[i])]
        values_list = [dict(top25Words[i])[key] for key in dict(top25Words[i])]

        ax.bar(keys_list, values_list, color='green')
        ax.set_title(f'{fileName[i]} top {len(top25Words[i])} words')
        ax.set_xlabel('word')
        ax.set_ylabel('Count')
        ax.tick_params(labelrotation=50)  # Rotate labels for better readability
        ax.tick_params(labelbottom=True)
        plt.tight_layout(pad=2.0)
    plt.show()
    return top25Words

def DisplayWordCloud(list):
    mask_image = imageio.v2.imread('AppleLogo.png') 
    wc = WordCloud(width=1000, height=1000,
    colormap='prism', mask=mask_image,background_color='white')

    fig = plt.figure(figsize=(15, 5))
    Top_100_words = int((len(list[0])+(len(list[1]))+(len(list[2])))/(len(list)))
    fig.suptitle(f"Apple logo word cloud for each document's top {Top_100_words} words")

    for i in range(len(list)):
        wc.fit_words(dict(list[i]))
        # i+1 will place each subplot in the correct position inside of the figure.
        ax =fig.add_subplot(1, 3, i+1) # print(i)
        ax.set_title(f'{fileName[i]} top {len(list[i])} words')
        ax.imshow(wc, interpolation="bilinear")
        ax.axis('off')
    plt.tight_layout()   
    plt.show()
def Top25cumulativeWord(lists):
    Top25words =[]
    # for list in list Merge sublists in one list
    MyList = [list for list in lists for list in list] 
    for item in MyList:
            word,count = item
            Top25words.append({word:count})
          
    Top25cumulativeWord = {}
    for item in MyList:
        word,count = item
        # print(word,count)
        Top25cumulativeWord[word] = Top25cumulativeWord.get(word, 0) + count

    print(len(Top25cumulativeWord))
    return Top25cumulativeWord


    
BlobList = ReadAllFiles()
MyList= RemoveStopWords(BlobList)
FileWordCount = GetWordCount(MyList)
# Part 2b
list_100=GetTop100Words(FileWordCount)
Top25words = Top25WordsPlot(FileWordCount)
# Part 2c
DisplayWordCloud(list_100)
print(Top25words)
# part 3a
Top25cumulativeWord(Top25words)

