import requests
res = requests.get('http://forecast.weather.gov/MapClick.php?lat=42.88644715000049&lon=-78.87836706299964#.WJXaS9J94s4')
res.raise_for_status()
playFile = open('weat.htm', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
import bs4
exampleFile = open('weat.htm')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
soup = bs4.BeautifulSoup(open('weat.htm'))
pElem = soup.select('p')
print('BUFFALO TODAY\n')
print('BUFFALO TODAY\n')
print('BUFFALO TODAY\n')
print('BUFFALO TODAY\n')
print('BUFFALO TODAY\n')
print('BUFFALO TODAY\n')
print('Collecting..\n')
print('BUFFALO TODAY\n')
#print('BUFFALO TODAY\n')print('BUFFALO TODAY\n')print('BUFFALO TODAY\n')print('BUFFALO TODAY\n')
print('Collecting...\n')
print('BUFFALO TODAY\n')
#print('BUFFALO TODAY\n')print('BUFFALO TODAY\n')print('BUFFALO TODAY\n')print('BUFFALO TODAY\n')
print('Collecting......\n')

pElem[4].getText()
print(pElem[4].getText(),end='\n')
pElem[5].getText()
print(pElem[5].getText(),end='\n')
pElem[3].getText()
#elem number by searching <\p>!!
print(pElem[3].getText(),end='\n')
#print('end')
