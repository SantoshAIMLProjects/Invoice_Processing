from invoice2data import extract_data
from invoice2data.extract.loader import read_templates

templates = read_templates('Template/')
print(templates)
result = extract_data('Invoice/QualityHosting.pdf', templates=templates)
print(result)