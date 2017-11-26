
# coding:utf-8

from CCPRestSDK import REST

# 主帐号
accountSid = '8aaf07085fe2d98c015ff7022cce07a9'

# 主帐号Token
accountToken = 'b6597c7cecb842c28e560f2e81e7a516'

# 应用Id
appId = '8aaf07085fe2d98c015ff7022d3707b0'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信的辅助类"""
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj
        # 如果没有，则保存对象直接返回
        return cls.instance

    def send_template_sms(self, to, datas, temp_id):

        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # for k, v in result.iteritems():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.iteritems():
        #             print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)

        # smsMessageSid:cbfb37e86ff444c99ebe22a333127d80
        # dateCreated:20171126160012
        # statusCode:000000
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送成功
            return 0
        else:
            # 发送失败
            return -1

if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_template_sms("13537185979", ["88888", "3"], 1)
    print(ret)

