# jdong
京东非官方API，可根据关键词获取相应商品列表，根据商品ID获取商品评价。   
​    
​    
目前正在开发中....

##API
###*class jdong.Good* —— 单个商品类
每一个商品的页面代表一个Good对象

>\_\_init\_\_(self, id=None, *args, **kwages)
>
>> 初始化，接受一个商品的ID，或者URL
>>
>> :param int id:ID
>>
>> Example:
>>
>> ​	g = Good('11867803')
>>
>> ​	g = Good(url='https://item.jd.com/11867803.html')
>
>get_comments(self, page=1)
>
>>:param int page:页数
>>
>>获取评论相关的JSON表单，返回一个Dict对象。

### *class jdong.KeyList* —— 关键词搜索类

根据关键词，搜索所有商家的商品。

>\_\_init\_\_(self, keyword, *args, **kwages)
>
>> :param str keyword:关键词
>>
>> 初始化，接受一个待搜索的关键词
>
>get_relist(self, page=1)
>
>> :param int page:页数
>>
>> 返回相关商品信息





## TODO
* 处理AJAX

