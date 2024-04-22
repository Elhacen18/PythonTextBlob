from typing import Counter
from textblob import TextBlob
from textatistic import Textatistic
import nltk
from nltk.corpus import stopwords
from pathlib import Path
from operator import itemgetter
import matplotlib.pyplot as plt 
from wordcloud import WordCloud   
import imageio
import spacy
nlp_sm = spacy.load('en_core_web_sm')

#  Part 2a
nltk.download('stopwords')
stop_words = list(stopwords.words('english'))
fileNames = ['Taken_Or_Left_novel.txt','Catching_of_the_whale_and_seal.txt','Extramammary_Articale.txt']
# From assignment2 
def Get_Words_Freq(list): # using this fucntion to get word frequancy for all three files as one list. 
    return Counter(list)
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
def Top25WordsPlot(list):

    top25Words = []
    # Get top 20 word for each file
    for item in list:
        file = sorted(item, key=itemgetter(1), reverse=True)
        # add only top 25 words 
        top25Words.append(file[:25])


    fig, axis = plt.subplots(3,1,figsize=(20, 8))


    for i, ax in enumerate( axis.flat):
        keys_list = [key for key in dict(top25Words[i])]
        values_list = [dict(top25Words[i])[key] for key in dict(top25Words[i])]

        Words = [key for key in dict(top25Words[i])]
        ax.bar(keys_list, values_list, color='green')
        ax.set_title(f'{fileNames[i]} top {len(top25Words[i])} words')
        ax.set_xlabel('words')
        ax.set_ylabel('Count')
        ax.tick_params(labelrotation=50)  # Rotate labels for better readability
        ax.tick_params(labelbottom=True)
        plt.tight_layout(pad=2.0)
    plt.show()
def Displa100yWordCloud(List):


    Top100words=[]
    for item in List:
        file = sorted(item, key=itemgetter(1), reverse=True)
    # add only top 100 words 
        Top100words.append(file[:100]) 


    mask_image = imageio.v2.imread('AppleLogo.png') 
    wc = WordCloud(width=1000, height=1000,
    colormap='prism', mask=mask_image,background_color='white')

   
    Top_100_words= int((len(Top100words[0])+(len(Top100words[1]))+(len(Top100words[2])))/(len(Top100words)))
    fig = plt.figure(figsize=(15, 5))
    fig.suptitle(f"Apple logo word cloud for each document's top {Top_100_words} words")
    for i in range(len(List)):
        wc.fit_words(dict(Top100words[i]))
        # i+1 will place each subplot in the correct position inside of the figure.
        ax =fig.add_subplot(1, 3, i+1) # print(i)
        ax.set_title(f'{fileNames[i]} top {len(Top100words[i])} words')
        ax.imshow(wc, interpolation="bilinear")
        ax.axis('off')
    plt.tight_layout()   
    plt.show()
def Top25cumulativeWord(lists):
    AllWordlist =[]
    SortList = []

    # "for list in list" Merge sublists into one list
    AllfilesMerged = [list for list in lists for list in list] 
    wordCumlative = Get_Words_Freq(AllfilesMerged)
    AllWordlist = list(wordCumlative.items())
 
    
    SortList =  sorted(AllWordlist, key=itemgetter(1), reverse=True)
    Top25CumalativeWords=  SortList[:25]

    return Top25CumalativeWords

def OutPutToCSVFile(words):
    with open("MCW.csv", 'w') as file:
        sum = 0
        file.write(f"word,Count\n")
        for word in words:
            sum = sum + word[1]
            file.write(f"{word[0]},{word[1]}\n")
        file.write(f"Sum,{sum}")
def FilesTextatistic(Files):
    AllFileTextStats = []
    TextStatsByFile = []
    avgScores = []
    for file in Files:
        Text = Textatistic(file)
        avgScores.append(Text.fleschkincaid_score)
        avgScores.append(Text.gunningfog_score)
        avgScores.append(Text.smog_score)
        avgScores.append(Text.dalechall_score)
        TextStatsByFile = (sum(avgScores))/(len(avgScores))
        AllFileTextStats.append({file:TextStatsByFile})
  
    # print(AllFileTextStats)    
    for file in AllFileTextStats:
        for Filename, avgScore in file.items():
            print(f"File name: {Filename}\nFlesch- Kincaid, Gunning Fog, SMOG, and Dale-Chall avg score:\n{avgScore}\n\n")


def pairwise_similarity(FileList):

    files = [nlp_sm(file) for file in FileList]
    print(files)
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            similarity_scores = files[i].similarity(files[j])
            print(f"{files[i]} and  {files[j]} Similarity: {f"{similarity_scores:.5f}"}")

# Part 1
ThreeFilesBlob = ReadAllFiles()
FilesWoStopWord= RemoveStopWords(ThreeFilesBlob)
# Par 2a
WordCountByFiles = GetWordCount(FilesWoStopWord) 
print(WordCountByFiles)
# Part 2b
Top25WordsPlot(WordCountByFiles)

# Part 2c
Displa100yWordCloud(WordCountByFiles)
# part 3a
top25cumlativeword =Top25cumulativeWord(FilesWoStopWord)
# part 3b
OutPutToCSVFile(top25cumlativeword)
# part 4a
FilesTextatistic(fileNames)

# Part 5a
pairwise_similarity(fileNames)



