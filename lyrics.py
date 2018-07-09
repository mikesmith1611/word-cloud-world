import re
import urllib.request
from bs4 import BeautifulSoup
import time

def get_lyrics(artist,song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"
    
    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        return lyrics
    except Exception as e:
        return "Exception occurred \n" +str(e)

def get_all_lyrics_for_album(artist,album):
    url = "https://search.azlyrics.com/search.php?q={0}".format(artist.replace(' ', '+'))
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table')
    data = []
    rows = table.find_all('tr')
    time.sleep(1)

    artisturl = rows[0].find_all('a', href=True)[0]['href']
    content = urllib.request.urlopen(artisturl).read()
    soup = BeautifulSoup(content, 'html.parser')
    albums = soup.find_all('div', attrs={'class': "album"})
    
    for a in albums:
        b = a.findNext()
        print(b.contents[0])
        if b.contents[0] == '"{0}"'.format(album):
            break
    urls = []
    while True:
        if a.findNext().findNext().findNext() in albums:
            break
        a = a.findNext().findNext(href=True) #a.findNext('a', href=True)
        urls.append(a['href'])

    lyrics = ''

    for url in urls:
        artist = url.split('/')[2]
        song = url.split('/')[-1].split('.html')[0]
        time.sleep(0.5)
        lyrics += ' ' + get_lyrics(artist, song)
    
    return lyrics