import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import webbrowser


class HAITWIFI:

    def __init__(self):
        self.username = '2007441403'
        self.password = '1998925sk'
        # 移动@gxyyd  联通@gxylt  电信@gxydx
        self.operator = {'1': '@gxyyd', '2': '@gxylt', '3': '@gxydx'}.get('1', '@gxyyd')

    def getIP(self):
        url = 'http://211.69.15.33:9999/portalReceiveAction.do?wlanuserip=10.50.57.125&wlanacname=HAIT-SR8808'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        wlanuserip = soup.find('input', attrs={'name': 'wlanuserip'}).attrs['value']
        wlanacip = soup.find('input', attrs={'name': 'wlanacIp'}).attrs['value']
        return wlanuserip, wlanacip

    def login(self):
        ip = self.getIP()
        login_url = "http://211.69.15.33:9999/portalAuthAction.do"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.121 Safari/537.36',
            'Referer': 'http://211.69.15.33:9999/portalReceiveAction.do?wlanuserip=10.50.57.125&wlanacname=HAIT-SR8808',
        }
        post_data = {'wlanuserip': ip[0],
                     'wlanacname': 'HAIT-SR8808',
                     'chal_id': '',
                     'chal_vector': '',
                     'auth_type': 'PAP',
                     'seq_id': '',
                     'req_id': '',
                     'wlanacIp': ip[1],
                     'ssid': '',
                     'vlan': '',
                     'mac': '',
                     'message': '',
                     'bank_acct': '',
                     'isCookies': '',
                     'version': '0',
                     'authkey': '88----89',
                     'url': '',
                     'usertime': '0',
                     'listpasscode': '0',
                     'listgetpass': '0',
                     'getpasstype': '0',
                     'randstr': '7150',
                     'domain': '',
                     'isRadiusProxy': 'true',
                     'usertype': '0',
                     'isHaveNotice': '0',
                     'times': 12,
                     'weizhi': 0,
                     'smsid': '',
                     'freeuser': '',
                     'freepasswd': '',
                     'listwxauth': '0',
                     'templatetype': '1',
                     'tname': 'gxy_pc_portal',
                     'logintype': '0',
                     'act': '',
                     'is189': 'false',
                     'terminalType': '',
                     'checkterminal': 'true',
                     'portalpageid': '23',
                     'listfreeauth': '0',
                     'viewlogin': '1',
                     'userid': self.username + self.operator,
                     'authGroupId': '',
                     'smsoperatorsflat': '',
                     'useridtemp': self.username + self.operator,
                     'passwd': self.password,
                     'operator': self.operator}
        r = requests.post(url=login_url, data=post_data, headers=headers)
        bs = BeautifulSoup(r.content, 'html5lib')
        toaster = ToastNotifier()
        if bs.find_all('input', id='loginOut') != []:
            toaster.show_toast('WIFI登录', '登录成功', threaded=True)
        else:
            toaster.show_toast('WIFI登录', '登录失败', threaded=True)
            webbrowser.open(
                'http://211.69.15.33:9999/portalReceiveAction.do?wlanuserip=10.50.57.125&wlanacname=HAIT-SR8808')


HAITlogin = HAITWIFI()
HAITlogin.login()
