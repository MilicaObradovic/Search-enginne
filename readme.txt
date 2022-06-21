Opis projekta (search engine)

Glavne strukture podataka korišćene u projektu jesu usmereni graf i trie stablo. Takodje implementiran je Insertion sort za sortiranje fajlova po rangovima unesenog upita za pretragu.

Trie stablo

Korišćeno radi brže pretrage reči u jednom fajlu. Čvor ovog stabla je implementiran preko klase Node i sadrži 4 atributa, slovo, podatak o kraju reči, brojač pronadjenih reči ukoliko je kraj reči, kao i rečnik u koji se smeštaju deca. Klasa Trie sadrži koren kao početak stabla u kome se nalazi prazan string, kao i metode search i insert preko kojih se pretrazuju i dodaju reči u stablo.
Instanca Trie stabla se kreira za svaki fajl pre dodavanja Vertexa grafa i u nju se dodaju reci iz fajla.

Usmereni graf

Korišćen za organizaciju fajlova iz unetog direktorijuma. Čvor klase Graph je implementiran preko Vertex ugnježdene klase i sadrži 3 atributa u koja se upisuju linkovi na koje pokazuje fajl, putanja fajla kao i instanca klase Trie. Ivica klase Graph je implementirana preko Edge ugnježdene klase i sadrži takodje 3 atributa, koji predstavljaju dva čvora koja spaja ivica grafa, kao i element ivice koji u ovom projektu nije korišćen, ali je ostavljen u slučaj da zatreba za neku narednu verziju. Neke od bitnijih metoda iz klase Graph su insert_vertex i insert_edge koje su korišćene pri kreiranju grafa, kao i path_element koja je korišćena za dobavljanje čvora preko putanje fajla.
Graf se kreira nakon što korisnik unese željenu putanju i u tom koraku se kreiraju instance klase Vertex u koju se dodaju podaci o fajlu i trie stablo tog fajla. Nakon toga se dodaju ivice preko linkova na koje pokazuju fajlovi.

Insertion sort

Algoritam Insertion sorta je predstavljen preko sledeceg pseudokoda.
n - duzina niza A

for j <— 1 to n-1 do
	v <— A[ j ]
	i <— j - 1
	while j >= 0 and A[ j ] > v do
		A[ j + 1 ] <— A[ j ]
		j <— j - 1
	A[ j + 1 ]

Algorithm funkcioniše tako što prvo sortira prva dva elementa i onda zatim u svakoj iteraciji prolazi redom kroz ostale elemente i stavlja jedan po jedan element na svoju sortiranu poziciju u prvih j elemenata.
Insertion sort je implementiran u ovom projektu iz razloga sto nemamo previše dokumenata koje mozemo da pretražujemo, stoga maksimalan broj liste za sortiranje može da bude 508 što predstavlja broj .html fajlova u datom direktorijumu.