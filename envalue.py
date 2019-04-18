import requests
import urllib
import _md5

headers = {
    'Host': "bkjws.sdu.edu.cn",
    'Connection': "keep-alive",
    'Accept': '*/*',
    # Origin: http://bkjws.sdu.edu.cn
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36""",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    # Referer: http://bkjws.sdu.edu.cn/f/common/main
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9"
}
list_data = "aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A5%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A-1%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22kch%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22kcm%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22jsm%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22function%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22function%22%7D%2C%7B%22name%22%3A%22iSortCol_0%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22sSortDir_0%22%2C%22value%22%3A%22asc%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3Atrue%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_3%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_4%22%2C%22value%22%3Afalse%7D%5D"
target_url = 'http://bkjws.sdu.edu.cn/b/pg/xs/add'
login_url = 'http://bkjws.sdu.edu.cn/b/ajaxLogin'
list_url = "http://bkjws.sdu.edu.cn/b/pg/xs/list"
standard = "&wjid=1&wjmc=%E5%B1%B1%E4%B8%9C%E5%A4%A7%E5%AD%A6%E8%AF%BE%E5%A0%82%E6%95%99%E5%AD%A6%E8%AF%84%E4%BB%B7(2017)&zbid=36&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_0=5.0&zbid=37&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_1=5.0&zbid=38&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_2=5.0&zbid=39&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_3=5.0&zbid=40&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_4=5.0&zbid=41&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_5=5.0&zbid=42&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_6=5.0&zbid=43&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_7=5.0&zbid=44&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_8=5.0&zbid=45&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_9=5.0&zbid=46&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_10=5.0&zbid=47&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_11=5.0&zbid=48&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_12=5.0&zbid=49&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_13=5.0&zbid=50&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_14=5.0&zbid=52&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_15=5.0&zbid=53&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_16=5.0&zbid=54&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_17=5.0&zbid=55&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_18=10.0&zbid=51&zblx=%E4%B8%BB%E8%A7%82%E9%80%89%E6%8B%A9&sfbt=&zbda_19=%E8%AF%BE%E7%A8%8B%E6%9C%89%E6%8C%91%E6%88%98%E6%80%A7&zbid=56&zblx=%E4%B8%BB%E8%A7%82%E9%80%89%E6%8B%A9&sfbt=&zbda_20=%E6%8E%A8%E8%8D%90&zbid=57&zblx=%E4%B8%BB%E8%A7%82&sfbt=%E6%98%AF&zbda_21="


def write(session, xnxq, kch, jsh, kcm, jsm):
    print("课程名：" + kcm + " " + jsm + "\n如果要跳过请输入\'q\' 否则请对老师进行评价：")
    envalue = input()
    if (envalue == "q" or envalue == "\'q\'"):
        print("你已跳过此项\n")
    else:
        data = "xnxq=" + xnxq + "&kch=" + kch + "&jsh=" + jsh + standard + urllib.parse.quote(envalue)
        headers['content-length'] = str(len(str(data)))
        p = session.post(target_url, headers=headers, data=data)
        print(p.json()["msg"])
    print("<--------------Cutline-------------------->\n")


def login():
    session = requests.Session()
    ID = input("please input your ID:")
    password = input("please input your password:")
    account = "j_username=" + str(ID) + "&j_password=" + str(_md5.md5(password.encode()).hexdigest())
    headers['content-length'] = str(len(str(account)))
    s = session.post(login_url, headers=headers, data=account)
    print("登录状态:" + s.json())
    headers['content-length'] = str(len(str(list_data)))
    List = session.post(list_url, headers=headers, data=list_data)
    list_number = List.json()['object']['aaData']
    for oneclass in list_number:
        write(session, oneclass["xnxq"], oneclass["kch"], oneclass["jsh"], oneclass["kcm"], oneclass["jsm"])


if (__name__ == "__main__"):
    print("本脚本的目的是避免点点点的反人类操作，以及对老师工作的肯定，因此默认全部好评，\n但是对老师的文字评价需要自己书写。如果某门课不想全部好评,请按\"q\"跳过，然后自行进入系统进行评价！\n注意：有些课可能还没有开始上，因此暂时先不用评价！跳过就好！切记！")
    a = input("请按任意键继续_")
    login()
