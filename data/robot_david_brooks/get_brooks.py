from nytimesarticle import articleAPI

api = articleAPI("1d21881c9f374736821cd81efbffa68b")

if __name__=='__main__':
    data = api.search(q="David Brooks", fq={"byline":"David Brooks"})
