#!/usr/bin/env python
#coding:utf8
from openpyxl import Workbook
wb = Workbook()
dest = "output.xlsx"
ws1 = wb.active
ws1.title = "Sheet1"
ws1.append(["eq","seq","scene","shot","note"])
wb.save(filename = dest)
