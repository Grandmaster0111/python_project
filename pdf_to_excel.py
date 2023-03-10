import tabula
import pandas as pd

tab = tabula.read_pdf('new.pdf',pages=all)

tabula.convert_into("new.pdf","new.csv",pages="all",output_format="csv")
df = pd.concat(tab)
excel_file = df.to_excel("new1.xlsx")