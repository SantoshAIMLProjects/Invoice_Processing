from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import pandas as pd

templates = read_templates('Template/')
print(templates)
result = extract_data('Invoice/F2_invoice_1_EN.pdf', templates=templates)
print('\n')
print(result)
print(type(result))
#df = pd.DataFrame(result,index=[0])

#print(df)
#df.to_csv('output1.csv')
#print(output1.csv)
#/Users/apple/AI ML Projects/invoice2data/Invoice/F1_invoice_1.pdf
# invoice processing