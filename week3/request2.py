import urllib.request as req
import bs4

# find time function: get into article and find time 
# open url which link is from title
def get_time(t):
    url = "https://www.ptt.cc" + t.a["href"]
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    # find html tag of time
    time_span_ch = root.find(
        "span",
        string = lambda s: s != None and s.strip() == "時間")
    # if there's no time return empty string
    if time_span_ch == None:
        return ""
    else:
        time = time_span_ch.find_next_sibling("span")
        return time.string
# find like function
def get_like(t):
    like_div = t.find_previous_sibling("div")
    like_span = like_div.span
    if like_span != None:
        return like_span.string
    # if there's no like return 0
    else:
        return "0"

# main function
def getData(u):
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    titles = root.find_all("div", class_ = "title")
    
    for title in titles:
        if title.a != None:
            result_titles.append(title.a.string)
            result_likes.append(get_like(title))
            result_times.append(get_time(title))
    route = root.find("a", string = "‹ 上頁")
    return route["href"]
    
result_titles = []
result_likes = []
result_times = []
    
url = "https://www.ptt.cc/bbs/Steam/index.html"
n = 0
while n < 3:
    nextlink = "https://www.ptt.cc" + getData(url)
    url = nextlink
    n += 1
    
print(result_titles, result_likes, result_times)

with open ("article.csv", "w", encode = "utf-8") as file:
    for a, b ,c in zip(result_times, result_likes, result_titles):
        file.write(f'{a},{b},{c}\n')