import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" +
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71"}


def get_soup(url):
    """接受一个URL，返回其BeautifulSoup对象
    """
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content.decode("utf-8"), "lxml")
    return soup
