import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site "http://www.pudim.com.br/" não está acessivel no momento.')
else:
    print('Consegui acessar o site "http://www.pudim.com.br/" com sucesso!')
    print(site.read())
    