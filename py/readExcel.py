#!/usr/bin/env python
#coding:utf8
import os
from openpyxl import load_workbook

xlsxPath = os.path.expanduser("~/examples/xlsx/cglist.xlsx")
wb = load_workbook(filename=xlsxPath, read_only=True)
ws = wb["Sheet1"]
for row in ws.rows:
	for cell in row:
		print(cell.value)
