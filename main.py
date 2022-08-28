# 这是一个示例 Python 脚本。
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import pandas as pd
import pytz
from datetime import datetime, timedelta, timezone
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    import sys
    #sys.setdefaultencoding('utf-8')
    #date = datetime.now()
    #wp = Client('https://hengheng2100.wordpress.com/xmlrpc.php', 'blueflywuheng@163.com', 'Redfire555')
    #post = WordPressPost()
    #post.title = '寻找从前4'
    #post.content = '测试的blog4'
    #post.author = "hengheng2100"
    #post.post_status = "publish"
    #post.date_created = datetime.date(2020, 1, 11)
    #post.date = datetime.datetime(2020, 1, 8)
    #post.id = wp.call(posts.NewPost(post))
    #print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #print_hi('PyCharm')
    print('上传开始')
    file_pathin = input("文件名:")
    sheet_namein = input("sheet名:")
    website_address = input("wordpress网址(不含https://):")
    usr_id = input("用户名(注册邮箱):")
    password_value = input("密码:")
    author_name = input("作者名:")
    #file_path = r'./blog.xls'
    df = pd.read_excel(file_pathin, sheet_name=sheet_namein)
    wp = Client('https://'+website_address+'/xmlrpc.php', usr_id, password_value)
    post = WordPressPost()
    post.author = author_name
    post.post_status = "publish"
    tz = pytz.timezone('Asia/Shanghai')
    tz_utc_0 = timezone(timedelta(hours=0))
    tz_utc_8 = timezone(timedelta(hours=8))
    for indexs in df.index:
        row_data = df.iloc[indexs]
        cell_data0 = str(df.iloc[indexs][0])
        naive_time = datetime.strptime(cell_data0, '%Y-%m-%d %H:%M:%S')
        pktime = naive_time.astimezone(timezone(timedelta(hours=8)))
        utctime = pktime.astimezone(timezone(timedelta(hours=0)))
        #切换时区解决时间差8小时问题建议先少量博客上传测试
        cell_data_date = utctime
        cell_data1 = df.iloc[indexs][1]
        cell_data2 = df.iloc[indexs][2]
        post.title = cell_data1
        post.content = str(cell_data2).replace('&nbsp;', ' ')
        post.date = cell_data_date
        post.id = wp.call(posts.NewPost(post))
        print(cell_data0)
        print(cell_data1)
        print(str(cell_data2).replace('&nbsp;', ' '))

