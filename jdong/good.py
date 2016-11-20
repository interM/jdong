import requests
import re


class Good(object):
    '''单个商品类，每一个商品的页面代表一个Good对象，
    例如可以将 https://item.jd.com/11867803.html 封装为一个Good对象。
    '''

    def __init__(self, id=None, *args, **kwages):
        """初始化，传入商品ID，或者URL。
        Example:
            g = Good('11867803')
            g = Good(url='https://item.jd.com/11867803.html')
        """
        if id != None:
            self.id = id
        else:
            self.id = kwages.get('url').split('/')[3][:-5]

    def get_comments(self, page=1):
        """获取评论相关的JSON表单。
        返回一个dict对象。
        """
        comment_url = 'https://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=3&' \
            'page={}&pageSize=10&callback=fetchJSON_comment98vv157'.format(
                self.id, page)

        raw_datas = requests.get(comment_url).text

        # 加工原始数据，提取出能构成JSON的字符串
        str_comments = re.findall(
            'fetchJSON_comment98vv157\((.*?)\);', raw_datas)[0]

        str_comments = str_comments.replace('null', '\'null\'')
        str_comments = str_comments.replace('false', '\'false\'')
        str_comments = str_comments.replace('true', '\'true\'')

        comments = eval(str_comments)
        return comments
