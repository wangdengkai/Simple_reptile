from distutils.core  import setup

setup(
    name="my_reptile",#包名
    version="1.0",#版本
    description="搜索关键词，模拟浏览器",#描述信息
    long_description="输入关键字词，获得百度搜索的前面10条信息",#完整描述信息
    author="玄锷无梦",#作者
    author_email="wangdengkai@163.com",#作者邮箱
    url="www.sousu.com",#主页
    py_modules=["my_soup_parse_html_v1","reptile_destkop_v1","reptile_main_v1","reptile_request_v1"]
)