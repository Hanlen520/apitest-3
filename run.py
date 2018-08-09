# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 执行包：runscript

import function.func as func

ApiTest = func.ApiTest()

FILENAME = 'user.ini'
FILENAME1 = 'task_lists.ini'


"""1.新建测试报告目录"""
ApiTest.reset_report(filename=func.cs.CASE_PATH+FILENAME)
ApiTest.reset_report(filename=func.cs.CASE_PATH+FILENAME1)

"""2.执行测试用例"""
ApiTest.run_test(filename=func.cs.CASE_PATH+FILENAME)
ApiTest.run_test(filename=func.cs.CASE_PATH+FILENAME1)


"""3.统计测试报告结果"""
ApiTest.write_report_result()
