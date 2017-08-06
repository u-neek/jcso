#imoport libraries
import urllib.request
from bs4 import BeautifulSoup


#specify the url
url = "http://jonesso.com/inmate-roster"

#query the site ans return html
page = urllib.request.urlopen(url)

#parse html 
soup = BeautifulSoup(page, 'html.parser')

# find div and return value
inmate_roster = soup.find('div', attrs={'id': 'inmate_roster'})

inmates = inmate_roster.find_all( 'div', attrs={'class': 'inmate'})

inmate = inmates[0]

print (inmate.prettify)