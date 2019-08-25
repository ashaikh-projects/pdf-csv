import tabula
import re
import pandas as pd
import json2xls
import json
import csv
import xlsxwriter
from xlrd import open_workbook

df = tabula.read_pdf("catbcp.pdf", pages="all", pandas_options={'header':None})
#df.replace()
df_head = df.head()
print(df_head)

df_replace = df_head.replace(to_replace=r"\r", value = " ", regex=True)
df_replace2 = df_replace. replace(to_replace=r" /", value= "", regex=True)
print("Replace")
print(df_replace)

print("Replace /")
print(df_replace2)
