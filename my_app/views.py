from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key = "a0595ccff26a4790a9dd4b8c1e7e7c01")
    top = newsapi.get_top_headlines(sources ='bbc-news') 
    l = top["articles"]
    desc =[] 
    news =[] 
    img =[] 
    pub = []
    url = []

    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        pub.append(f['publishedAt'])
        url.append(f['url'])
    mylist = zip(news, desc, img , pub , url) 
    return render(request, 'index.html', context ={"mylist":mylist})

def technews(request):
    newsapi = NewsApiClient(api_key = "a0595ccff26a4790a9dd4b8c1e7e7c01")
    top_headlines = newsapi.get_top_headlines(sources = "the-next-web")
    l = top_headlines["articles"]
    desc = []
    news = []
    img = []
    pub = []
    url = []
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pub.append(f["publishedAt"])
        url.append(f['url'])
    mytech = zip(news , desc , img , pub , url)
    return render(request , 'tech.html' , context={"mytech" : mytech})