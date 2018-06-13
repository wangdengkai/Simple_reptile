from bs4 import BeautifulSoup
from bs4 import SoupStrainer


class Bsoup_html():
    def __init__(self):
        '''初始化分析对象'''
        self.content_left = SoupStrainer("div", attrs={"id": "content_left"})
        self.soup = BeautifulSoup(open("response_baidu.html", encoding="utf-8"), "html.parser",
                                  parse_only=self.content_left)
        self.h3_list = []
        self.descript_list = []

    def get_title_href(self):
        '''获取每一条数据的标题'''
        my_h3 = self.soup.find_all("h3")
        for my in my_h3:
            temp_str = ""
            for my_str in my.stripped_strings:
                temp_str += repr(my_str)
            temp_str += "()" + my.a["href"]
            self.h3_list.append(temp_str)

    def get_descript_info(self):
        '''获取每一条数据的描述信息'''
        count = 0
        my_h3 = self.soup.find_all("h3")

        for my in my_h3:
            my_tag = my.find_next("div", class_=["c-abstract", "c-span18 c-span-last", ])
            temp_str = ""
            for my_str in my_tag.stripped_strings:
                temp_str += my_str
            temp_str = temp_str.split()
            self.descript_list.append("".join(temp_str))

    def write_to_data(self):
        '''将分析后的数据，格式化写到另外的文件。'''
        html_list = []
        my_tuple_info = zip(self.h3_list, self.descript_list)
        for k, v in my_tuple_info:
            title_k = k.split("()")
            temp_str = title_k[0] + "\n\t\t\t\t" + v + "\n\t\n"
            html_list.append(temp_str)
            my_html_format = '<h3><a href="{}">{}</a></h3><br/><p>{}</p>'.format(title_k[1], title_k[0], v)

        with open("show_data.txt", "w") as f:
            f.write("")
        with open("show_data.txt", "a+", encoding="utf-8") as f:
            for ht in html_list:
                f.writelines(ht)
                f.write("\n")

    def run_to_txt(self):
        '''系统运行以上方法，进行一次调用，就完成'''
        self.get_descript_info()
        self.get_title_href()
        self.write_to_data()


if __name__ == "__main__":
    bshtml = Bsoup_html()
    bshtml.get_descript_info()
    bshtml.get_title_href()
    bshtml.write_to_data()
