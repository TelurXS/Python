import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from textblob import TextBlob
import re
from collections import Counter

def task1() -> None:

    # 1
    data = pd.read_csv("top250.csv")

    # 2
    print(data.head(5))

    # 3
    print(data.shape)

    # 4
    data.select_dtypes(include=["int16", "int32", "int64", "float16", "float32", "float64"]).info()
    
    # 5
    print(data.isnull().value_counts())

    # 6
    data.drop("Market_value", axis=1, inplace=True)

    # 7
    #plt.style.use("ggplot")
    #data.hist()
    #plt.tight_layout()
    #plt.savefig("Distribution.png")
    
    # 8
    #sns.countplot(x='Position',data=data)
    #plt.xticks(rotation=90)
    #plt.show()

    # 9
    #sns.pointplot(x=data.index, y=data["Season"])
    #plt.xticks(rotation=90)
    #plt.xlabel('Season')
    #plt.ylabel('Number of Trade')
    #plt.show()

    # 10
    data = data.head(20)

    # 11
    data["Transfer_fee"] = [float(i) / sum(data.Transfer_fee) for i in data["Transfer_fee"]] 
    data.Age = [float(i)/sum(data["Age"]) for i in data["Age"]]

    # 12
    #f,ax = plt.subplots(figsize=(16,8))
    #plt.xticks(rotation = 60)
    #sns.pointplot(x = "Name",y="Age",data=data,color="black")
    #sns.pointplot(x = "Name",y="Transfer_fee",data=data,color="red")
    #plt.text(15,0.1,'Age',color='black',fontsize = 10,style = 'italic')
    #plt.text(15,0.103,'Transfer Fee',color='red',fontsize = 10,style = 'italic')
    #plt.xlabel("Football Player Names")
    #plt.ylabel("Transfer Fee vs. Age")
    #plt.savefig('graph.png')

    # 13
    #sns.countplot(x='Team_from',data=data)
    #plt.xticks(rotation=90)
    #plt.xlabel("Team From")
    #plt.ylabel("Count")
    #plt.show()

    # 14
    #labels = data[:15]["League_to"].value_counts().index
    #colors = ["blue","red","green","yellow"]
    #explode = [0,0,0,0]
    #sizes = data[:15]["League_to"].value_counts().values
    #plt.figure(figsize = (7,7))
    #plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
    #plt.title('Transfers League_to',color = 'blue',fontsize = 15)
    #plt.show()

    # 15
    sns.swarmplot(x="Position",y="Transfer_fee",hue="League_from",data=data)
    plt.xticks(rotation=15)
    plt.title("Swarm Plot for Transfer Fee and Position",fontsize=12)
    plt.xlabel("Position",fontsize=10)
    plt.ylabel("Transfer Fee",fontsize=10)
    plt.show()

    return


def task2() -> None:

    # 1
    data = pd.read_csv("tweets.csv")
    print(data.head())
    
    # 2
    print(data.shape)

    # 3
    print(data["lang"].value_counts())

    # 4
    def language(df) :
        if df["lang"] == "en" :
            return "English"
        elif df["lang"] == "es" :
            return "Spanish"
        else :
            return "Other"
        
    data["lang"] = data.apply(lambda tweets:language(tweets), axis = 1)

    # 4
    print(data["lang"].value_counts())

    # 5
    print(data["time"].head())

    # 6
    date_format = "%Y-%m-%dT%H:%M:%S" 
    data["time"]   = pd.to_datetime(data["time"],format = date_format)
    data["hour"]   = pd.DatetimeIndex(data["time"]).hour
    data["month"]  = pd.DatetimeIndex(data["time"]).month
    data["day"]    = pd.DatetimeIndex(data["time"]).day
    data["month_f"]  = data["month"].map({1:"JAN",2:"FEB",3:"MAR",
                                            4:"APR",5:"MAY",6:"JUN",
                                            7:"JUL",8:"AUG",9:"SEP"})
    
    print(data.head())

    # 7
    data=pd.concat([data.handle, data.text], axis=1)

    # 8
    data.dropna(axis=0, inplace=True)  

    # 9
    print(data.handle.value_counts())

    # 10
    #sns.countplot(x='handle', data = data)
    #plt.savefig("tweet.png")

    # 11
    data = pd.read_csv("tweets.csv")

    #plt.style.use('ggplot')

    #plt.figure(figsize = (13,6))
    #plt.subplot(121)
    #data[data["handle"] =="realDonaldTrump"]["is_retweet"].value_counts().plot.pie(autopct = "%1.0f%%", wedgeprops = {"linewidth" : 1,"edgecolor" : "k"},shadow = True, fontsize = 13,
    #explode = [.1,0.09], startangle = 20, colors = ["#ff0026","#fbff00"])
    #plt.ylabel("")
    #plt.title("Percentage of Trump retweets")

    #plt.subplot(122)
    #data[data["handle"] =="HillaryClinton"]["is_retweet"].value_counts().plot.pie(autopct = "%1.0f%%",
    #wedgeprops = {"linewidth" : 1, "edgecolor" : "k"},
    #shadow = True,fontsize = 13, explode = [.09,0],
    #startangle = 60, colors = ["#0095ff","#fbff00"])
    #plt.ylabel("")
    #plt.title("Percentage of Hillary retweets")
    #plt.savefig("pieplot.png")

    # 13
    #bloblist_desc = list()                                  
    #df_tweet_descr_str=data['text'].astype(str)           

    #for row in df_tweet_descr_str:
    #    blob = TextBlob(row)
    #    bloblist_desc.append((row,blob.sentiment.polarity, blob.sentiment.subjectivity))
    #    df_tweet_polarity_desc = pd.DataFrame(bloblist_desc, columns = ['sentence','sentiment','polarity'])
    #
    #def f(df_tweet_polarity_desc):
    #    if df_tweet_polarity_desc['sentiment'] > 0:
    #        val = "Positive"
    #    elif df_tweet_polarity_desc['sentiment'] == 0:
    #        val = "Neutral"
    #    else:
    #        val = "Negative"
    #    return val

    #df_tweet_polarity_desc['Sentiment_Type'] = df_tweet_polarity_desc.apply(f, axis=1)

    #plt.figure(figsize=(10,10))
    #sns.set_style("whitegrid")
    #ax = sns.countplot(x="Sentiment_Type", data=df_tweet_polarity_desc)
    #plt.savefig("text.png")

    # 14
    pattern = r'[^\w\s]'
    expression = re.compile(pattern)

    def remove_symbols(text):
        cleaned_text = expression.sub('', text)
        return cleaned_text

    data['text'] = data['text'].apply(remove_symbols)

    print(data["text"].head(20))

    # 15
    def count_words(text: str):
        words = text.split()
        word_counts = Counter(words)
        return word_counts
    
    word_counts = data['text'].apply(count_words).sum()
    most_common_word = word_counts.most_common(1)

    print("The most common word is:", most_common_word)

    return



def main() -> None:
    #task1()
    task2()
    return


if __name__ == "__main__":
    main()
    