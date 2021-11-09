from orodja import *
import re
from requests import *

def hekersko_shrani(url, datoteka, sesh):
    #potrebno je bilo shrani_spletno_stran malo spremeniti
    #credit g. Pretnar
    try:
        print(f'Shranjujem {url} ...', end='')
        sys.stdout.flush()
        if os.path.isfile(datoteka):
            print('shranjeno že od prej!')
            return
        req = Request('GET', url)
    except exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        prep = req.prepare()
        #za sledec line je potrebna obrazlozitev:)
        #########################################################
        prep.headers['User-Agent'] = 'burek'
        #########################################################
        response = sesh.send(prep)
        page_html = response.text

        pripravi_imenik(datoteka)        
        with open(datoteka, 'w', encoding='utf-8') as fajl:
            fajl.write(page_html)
            print('shranjeno!')
    return


STEVILO_STRANI = 30 #error pri master in diamond I.. nimamo tolerance za "I" pri diamondo
STEVILO_SUMMONERJEV_NA_STRAN = 100

vzorec = (
    r'<span class="name">'  # tako se zacne tabelni vnos za posameznega summonerja
    r'(?P<summoner>.*?)'    # zajamemo ime summonerja
    r'</span>'   
    r'.*?'  #soloqueue
    r'<div class="summonerTier">'    #tu so naslednji podatki.. etc 
    r'\s*(?P<rank>.*?)\s\s*(?P<lp>.*?)?\sLP\s*'    
    r'</div>'
    r'\s*<div class="wins">\s*Wins:\s'
    r'(?P<wins>.*?)\s<i>\((?P<winrate>.*?)%\)'
    r'</i>'
    r'.*?'  #flex ki mogoce obstaja mogoce pa ne... lahko bi lepse spisal ampak jbg
    r'<td class="text-center hide-for-small-down">' #tega morda ni za tiste ki ne igrajo flexa
    r'(\s*<div class="summonerTier">\s*(?P<rankFlex>.*?)\s.*?</div>\s*<div class="wins">\s*Wins:\s(?P<winsFlex>.*?)\s<i>\((?P<winrateFlex>.*?)\)</i>)?'
    r'.*?</td>'
)

sesh = Session()
najdeni_summonerji = 0
seznam_slovarjev = []

for index in range(STEVILO_STRANI):
    #save vsako stran
    url = f'https://www.leagueofgraphs.com/rankings/summoners/eune/page-{index+1}'
    datoteka = f'najboljsi-summonerji/page{index+1}.html'
    #shrani_spletno_stran(url, datoteka)
    hekersko_shrani(url, datoteka, sesh)
    vsebina = vsebina_datoteke(datoteka)
    
    #obdelaj z regexom
    #    flags = re.DOTALL  vštulit
    for zadetek in re.finditer(vzorec, vsebina, flags = re.DOTALL):
        #print(zadetek.groupdict())
        najdeni_summonerji += 1
        #skupine named summoner, rank, lp, wins, winrate, rankflex, winsflex, winrateflex
        #[pojavitev.groupdict() for pojavitev in re.finditer(vzorec, recept)]
        #print(zadetek.groupdict())
        slovar = zadetek.groupdict()
        #popravi input ce ne igra flex
        #ne rabi
        seznam_slovarjev.append(slovar)

#print(seznam_slovarjev)
atribs = ['summoner', 'rank', 'lp', 'wins', 'winrate', 'rankFlex', 'winsFlex', 'winrateFlex']
zapisi_csv(seznam_slovarjev, atribs, "tabelica.csv")
