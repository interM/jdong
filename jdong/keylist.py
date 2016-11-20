import re
import pprint
from .utils import get_soup


class KeyList(object):
    '''关键词查询列表
    '''

    def __init__(self, keyword, *args, **kwages):
        """初始化
        """
        self.keyword = keyword
        self.url = 'https://search.jd.com/Search?keyword={}&enc=utf-8'.format(
            self.keyword)

    def get_relist(self, page=1):
        """返回商品信息。
        :param int page:页数
        """
        start_url = self.url + '&page={}'.format(page * 2)

        soup = get_soup(start_url)

        goodslist = soup.find("div", {"id": "J_goodsList"}).find("ul")
        relist = []
        for good in goodslist.find_all("li"):
            good_info = good.find("div", {"class": "gl-i-wrap"})
            try:
                name = good_info.find(
                    "div", {"class": "p-name p-name-type-2"}).get_text()
                name = name.replace("\n", "")
            except AttributeError:
                continue
            price = good_info.find("div", {"class": "p-price"}).get_text()
            price = price.replace("\n", "").replace(" ", "")
            try:
                tips = good_info.find(
                    "div", {"class": "p-icons"}).find("img").attrs['data-tips']
            except:
                tips = ''

            cash = good_info.find("div", {"class": "p-icons"}).find("i")
            if cash:

                if cash.get_text() == '货到付款':
                    cash_on_delivery = True
                else:
                    cash_on_delivery = False
            else:
                cash_on_delivery = False

            try:
                img = good_info.find(
                    "div", {"class": "p-img"}).find("img").attrs['src']
                img = "https://" + img
            except:
                img = ''

            link = good_info.find(
                "div", {"class": "p-img"}).find("a").attrs['href']
            if len(link) > 70:
                continue
            link = "https:" + link

            comment = good_info.find(
                "div", {"class": "p-commit"}).find("a").get_text()

            info = {"name": name,
                    "price": price,
                    "link": link,
                    "img": img,
                    "comment": comment,
                    "tips": tips,
                    "cash_on_delivery": cash_on_delivery
                    }
            relist.append(info)

        return relist

if __name__ == '__main__':
    k = KeyList("茶叶")
    pprint.pprint(k.get_relist())
