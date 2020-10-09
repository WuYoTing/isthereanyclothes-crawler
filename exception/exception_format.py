import sys
import traceback
from mail.mail_log import mail_log


def exception_format(mail_user, mail_password, recipient, exception, prod_url):
    print("Exception has been thrown. " + str(exception) + "when deal with " + prod_url)
    error_class = exception.__class__.__name__  # 取得錯誤類型
    detail = exception.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    last_call_stack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    file_name = last_call_stack[0]  # 取得發生的檔案名稱
    line_num = last_call_stack[1]  # 取得發生的行號
    fun_name = last_call_stack[2]  # 取得發生的函數名稱
    error_msg = "File \"{}\", line {}, in {}: [{}] {}".format(file_name, line_num, fun_name, error_class, detail)
    mail_log(mail_user, mail_password, recipient, 'Crawler Exception', error_msg + ' Exception Url: ' + prod_url)
