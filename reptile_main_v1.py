#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    0 主模块：
    定义一个主函数，直接调用界面模块
    初始化，启动程序
'''
import reptile_destkop_v1
def main():
    d=reptile_destkop_v1.Destkop()
    d.top.mainloop()



if __name__ == "__main__":
    main()


