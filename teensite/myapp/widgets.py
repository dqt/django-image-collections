import praw
import requests
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
from os.path import splitext, basename
import os
from django.template.defaultfilters import slugify
import HTMLParser


def memeScrape(where, maxcount=5):
    r = praw.Reddit(user_agent="/r/"+where+" grabber v1.0")
    already_done = []
    count = 0
    scraped = []
    subreddit = r.get_subreddit(where)
    for submission in subreddit.get_hot(limit=20):
        if submission.id not in already_done and count < maxcount:
            url = submission.url
            picture_page = url
            disassembled = urlparse(picture_page)
            filename, file_ext = splitext(basename(disassembled.path))
            r = requests.get(url, stream=True)
            if file_ext == '.jpg' or file_ext == '.jpeg':
                location = submission.id + file_ext
                imgloc = '/media/' + submission.id + file_ext
                html_parser = HTMLParser.HTMLParser()
                title = html_parser.unescape(submission.title)
                slug = slugify(submission.title)
                with open(os.path.join('/home/DuyLLC/teensite2/teensite/media/', location),  'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                already_done.append(submission.id)
                count += 1
                details = {'imgloc': imgloc, 'title': title, 'slug': slug}
                scraped.append(details)
    return scraped

def funScrape(page=1):
    if page == 1:
        r = requests.get("http://www.allforfun.org/")
    else:
        r = requests.get("http://www.allforfun.org/page/"+str(page))
    soup = BeautifulSoup(r.text)
    block = soup.find("div", {"class": "block archive"})
    posts = []
    for a in block.findAll('a',href=True):
        posts.append(a['href'])
    posts = posts[::4]
    if page == 1:
        posts.pop()
    else:
        posts.pop()
        posts.pop()
    scraped = []
    for post in posts:
        r = requests.get(post)
        soup = BeautifulSoup(r.text)
        h1 = soup.find("h1").contents
        block = soup.find("div", {"class": "post-entry"})
        img = block.find("img",src=True)
        name = img['src'].split("/")[-1]
        imgloc = '/media/' + name
        title = h1[0]
        slug = slugify(title)
        r = requests.get(img['src'])
        with open(os.path.join('/home/DuyLLC/teensite2/teensite/media/', name),  'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        details = {'imgloc': imgloc, 'title': title, 'slug': slug}
        scraped.append(details)
    return scraped
