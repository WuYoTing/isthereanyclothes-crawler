import sys
import traceback
from mail.mailLog import maillog


def exceptionFormat(e, url):
    print("Exception has been thrown. " + str(e) + "when deal with " + url)
    error_class = e.__class__.__name__  # 取得錯誤類型
    detail = e.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    fileName = lastCallStack[0]  # 取得發生的檔案名稱
    lineNum = lastCallStack[1]  # 取得發生的行號
    funcName = lastCallStack[2]  # 取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    maillog('Crawler Exception', errMsg + ' Exception Url: ' + url, 'hakosaki314@gmail.com')
