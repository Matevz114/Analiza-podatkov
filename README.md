# Analiza-podatkov
LoL lestvica
=========================================

Analiziral bom najboljših 4000 igralcev videogrice League of Legends na vzhodnoevropskem serverju glede na Soloqueue.
Podatke bom poiskal na strani https://www.leagueofgraphs.com/rankings/summoners/eune

Za vsakega igralca bom pogledal:
 - ime igralca
 - uvrstitev na lestvici, in njegove točke (po teh smo tudi igralci razvrščeni) ter točkam pripadajoč rang
 - število zmag in splošen winrate
 - rang, število zmag in wirate v Flexqueue.

S podatki se bom spraševal:
 - ali je (bolj) pomembna povezava med številom iger in doseženimi točkami
   oziroma ali je bolj pomembna povezava med wirate-om in točkami
 - ali obstaja povezava med uspešnostjo v Soloqueue-ju in Flexqueue-ju
   oziroma ali je igralcem sploh do tega da igrajo oba queue-ja
   
   
 
 
 
 
Kaj sploh je League of Legends (LoL) in kako sistem razvrsti igralce?

LoL je videoigra, igrana 5 na 5. Za potrebe te naloge so pomembni naslednji podatki:
1. Igralci se merijo v dveh različnih kategorijah - v Soloqueueju in FlexQueueju. Kot že imeni predlagata
prvega igraš sam (torej dobiš še štiri druge igralce, ki igrajo sami v ekipo in igraš proti petim drugim, ki so ravno tako vsak sam),
v drugem pa lahko igraš sam, v dvoje, troje, ali kot 5 na 5, po celih ekipah skupaj.

 1.1. Neuradno je Soloqueue veliko bolj reprezentativna kategorija sposobnosti nekega igralca, zato bom tudi po tej kategoriji
 razvrščal igralce.

2. Sistem rangiranja igralce razvrsti v kategorije Iron, Bronze, Silver, Gold, Platinum, Diamond, Master, Grandmaster, Challenger.
Vsak od teh rankov je potem razdeljen še na divizije od 1-4, kjer je 1 boljše od 4 (torej Gold 1 je boljše od Gold 3).
V nalogi bom gledal le igralce v najvišjih rankih, torej od Diamond 1 do Challenger.

3. Na odigrano igro vsak igralec v zmagovalni ekipi dobi približno 20 točk, vsak izmed poražencev pa jih toliko zgubi. 
 3.1 Master, Grandmaster in Challenger so v bistvu ena sama velika kategorija, kjer igralci tekmujejo neposredno en z drugim;
 od tega je prvih 200 po točkah v Challengerju, naslednjih 500 v Grandmasterju, ostali pa so v Masterju.
 3.2 V nižjih rankih (od Irona do Diamonda) pa za vsako naslednjo divizjo potrebuješ 100 točk in si avtomatsko naprej (torej da 
 prideš iz Gold 2 v Gold 1 potrebuješ 100 točk in potem si v Gold 1 na 0 točk, iz Platinum 1 ravno tako potrebuješ 100 točk in 
 potem si Diamond 4 na 0 točk...).
