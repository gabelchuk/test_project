import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101',
 'Firefox/47.0' 'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9,*/*,q=0.8'}

domain = 'https://www.work.ua/'
url = 'https://www.work.ua/jobs-kyiv-python/'
resp = requests.get(url, headers=headers)
vacancies = []
errors = []

if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', id='pjax-job-list')
    div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
    for div in div_lst:
        title = div.find('h2')
        href = title.a['href']
        description = div.p.text
        div_company = div.find('div', attrs={'class': 'add-top-xs'})
        company = div_company.span.text
        vacancies.append({'title': title.text, 'url': domain+href, 'description':
            description, 'company': company})
else:
    errors.append({'url': url, 'title': 'Page do not respond'})
    
# with codecs.open('work.txt', 'w', 'utf-8') as file:
#     file.write(str(vacancies))

# file = open('work.html', 'w')
# file.write(str(resp.content))
# file.close()