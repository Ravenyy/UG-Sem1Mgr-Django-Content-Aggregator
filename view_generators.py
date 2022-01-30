from content_aggregator.models import *
import cld3
import re
from urllib.parse import urlparse


def reddit_view_generator(info, content, content_list):
    content.headline = info.title
    desc = info.description

    if "<p>" in desc:
        start = desc.find('<p>')
        end = desc[start + 3:].find("</p>")
        content.text = desc[start + 3: start + 3 + end]
        content.text = re.sub(r'our <a href="', '"', content.text)
        content.text = re.sub(r'">Wiki</a>', '"', content.text)
        content.text = re.sub(r'>FAQ</a>', '', content.text)
        content.text = re.sub(r'<em>', '', content.text)
        content.text = re.sub(r'</em>', '', content.text)
        content.text = re.sub(r'<strong>', '', content.text)
        content.text = re.sub(r'</strong>', '', content.text)
        content.text = re.sub(r'<br>', '', content.text)
        content.text = re.sub(r'</br>', '', content.text)

        if "href" in content.text:
            pass
        elif len(content.text) > 3 and cld3.get_language(content.text).language == 'en':
            content.url = info.link
            content_list.append(content)

    elif "<span><a href=" in desc:
        start = desc.find('<span><a href="')
        end = desc[start + 15:].find('">[link]')
        content.text = desc[start + 15: start + 15 + end]
        domain = urlparse(content.text).netloc
        excluded_urls = ["/i.redd.it/", "/www.reddit.com/", "/gfycat.com/", "/imgur.com/", "/i.imgur.com/",
                         "/v.redd.it/"]

        if any(url in content.text for url in excluded_urls):
            pass
        else:
            content.url = info.link
            content.text = domain
            content_list.append(content)


def medium_view_generator(info, content, content_list):
    content.headline = info.title

    desc = info.description
    start = desc.find('<p class="medium-feed-snippet">')
    end = desc[start + 31:].find("<")

    content.text = desc[start + 31: start + 31 + end]
    content.text = re.sub(r'&#x2018;', "'", content.text)
    content.text = re.sub(r'&#x2019;', "'", content.text)
    content.text = re.sub(r'&#x2026;', "...", content.text)
    content.text = re.sub(r'&#xa0;', "", content.text)
    content.text = re.sub(r'&apos;', "'", content.text)
    content.text = re.sub(r'&#x200a;', "", content.text)
    content.text = re.sub(r'&#x2014;', "—", content.text)
    content.text = re.sub(r'&#x201c', '"', content.text)

    if len(content.text) > 3 and cld3.get_language(content.text).language == 'en':
        content.url = info.link
        content_list.append(content)


def bbc_cbn_view_generator(info, content, content_list):
    content.headline = info.title

    content.text = info.description

    if len(content.text) > 3 and cld3.get_language(content.text).language == 'en':
        content.url = info.link
        content_list.append(content)


def default_view_generator(info, content, content_list):
    content.headline = info.title

    content.text = info.description

    if len(content.text) > 3 and cld3.get_language(content.text).language == 'en':
        content.url = info.link
        content_list.append(content)


def pl_view_generator(info, content, content_list):
    content.headline = info.title

    content.text = info.description

    if len(content.text) > 3:
        content.url = info.link
        content_list.append(content)
