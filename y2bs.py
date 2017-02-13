import requests , bs4
url = 'https://www.youtube.com/'
url2 = 'https://www.youtube.com/?gl=US'
res = requests.get(url2)
res.raise_for_status()
bres = bs4.BeautifulSoup(res.text,"lxml")

vid_title = bres.select('.yt-lockup-title ')
vid_views = bres.select('.yt-lockup-meta-info')
print(type(vid_title) )
print((len(vid_title)))
for i in range(0,len(vid_title)):
	print(vid_title[i].getText())
	print(vid_views[i].getText())

