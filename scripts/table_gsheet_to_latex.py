import pandas as pd
url = 'https://docs.google.com/spreadsheets/d/' + '1wY63uV0DIN92cAebhKiV4o5RYW0qMvJAkIDgziu42I8' + '/export?gid=0&format=csv'
table = pd.read_csv(url)
latex_table = table.to_latex(index=False, bold_rows=True, caption="Caption here", na_rep='', escape=True)
print(latex_table)
