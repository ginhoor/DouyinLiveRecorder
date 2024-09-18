#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import base64
import hmac
import time
import requests, logging
# 个人任务
# MQ_NOTIFICATION_SECRECT = "3b9q2xzlcGMG7BpoNTsAX"
# MQ_NOTIFICATION_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/ccf3ed4c-c39e-457d-ba0d-b278633e7f85"

class FeiShuWebhookMsgeAPI(object):
    def __init__(self, webhook: str, secrect: str):
        self.webhook = webhook
        self.secrect = secrect

    def gen_sign(self, timestamp):
        # 拼接timestamp和secret
        string_to_sign = '{}\n{}'.format(timestamp, self.secrect)
        hmac_code = hmac.new(
            string_to_sign.encode("utf-8"),
            digestmod=hashlib.sha256).digest()
        # 对结果进行base64处理
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign

    def send_text_msg(self, text):
        timestamp = int(round(time.time()))
        sign = self.gen_sign(timestamp)
        data = {
            "timestamp": timestamp,
            "sign": sign,
            "msg_type": "text",
            "content": { "text": text }
        }
        response = requests.post(self.webhook, json=data)
        if response.status_code == 200:
            logging.info(f"飞书消息发送成功")
        else:
            logging.error(f"飞书消息发送失败，状态码：{response.status_code}")

def main_test():
    # 小扁家 测试
    sec = "cx534pMTmYGswfzf84mMhd"
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/8f543907-d620-4162-9522-b5fc3e91ec1a"

    api = FeiShuWebhookMsgeAPI(webhook, sec)
    api.send_text_msg("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")

if __name__ == '__main__':
    main_test()