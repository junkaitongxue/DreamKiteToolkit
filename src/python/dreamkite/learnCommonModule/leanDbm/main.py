'''
在一些python小型应用程序中，不需要关系型数据库时，可以方便的用持久字典来存储名称/值对，它与python的字典非常类似，
主要区别在于数据是在磁盘读取和写入的。另一个区别在于dbm的键和值必须是字符串类型。
'''
import dbm

'''
标志	用法
C	打开文件对其读写，必要时创建该文件
W	打开文件对其读写,如果文件不存在，不会创建它
N	打开文件进行读写，但总是创建一个新的空白文件
'''

# 新建
def main01():
    db = dbm.open('Bookmark', 'c')
    # 添加选项
    db['MyBlog'] = 'https://blog.csdn.net/weixin_41501825'
    print(db['MyBlog'])
    # 保存，关闭
    db.close()

# 删除
def main02():
    db = dbm.open('Bookmark', 'w')
    db['MyGit'] = 'https://github.com/junkaitongxue'
    if 'MyBlog' in db:
        del db['MyBlog']
    db.close()


if __name__ == '__main__':
    main01()
    main02()
