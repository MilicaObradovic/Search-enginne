import os
import time
import operator
from trie import Trie
from parser import Parser
from directed_graph import Graph

def postojeci_dir(string, dir):
    files = os.listdir(string)
    new = []
    for file in files:
        if "." in file:
            if file[-5:] == ".html":
                new.append(file[:-5])
        else:
            new.append(file)

    if dir in new:
        return True
    else:
        return False

def zeljena_putanja():
    nastavak = ""
    while True:
        nastavak = input("Da li ste izabrali zeljenu putanju? (da ili ne)> ")
        if nastavak in ["da", "ne"]:
            break
        else:
            print("Niste uneli da ili ne... pokusajte ponovo")

    return nastavak

def odabir_direktorijuma():
    string = "./documents"
    while True:
        if os.path.isdir(string) == True:
            z_putanja = zeljena_putanja()
            if z_putanja == "da":
                break
            direktorijum = input("Unesite ime direktorijuma ili fajla: ")
            if postojeci_dir(string, direktorijum):
                string += "/"+direktorijum
            print(string)
        else:
            print("Putanja koju ste uneli je fajl..")
            break
        
    return string
        
def list_files(startpath):
    graf = Graph(True)
    for path, dirs, files in os.walk(startpath):
        for f in files:
            if f[-5:] == ".html":
                parser = Parser()
                links, words = parser.parse(path+"/"+f)
                t = Trie()
                for word in words:
                    try:
                        int(word)
                    except ValueError:
                        word = word.lower()
                    t.insert(word)
                graf.insert_vertex(t, path+"/"+f, links)
    for i in graf._outgoing.keys():
        for j in i._links:
            m = "."+j[61:]
            elem = graf.path_element(m)
            if elem != False:
                graf.insert_edge(i, elem)
    return graf
                
string = odabir_direktorijuma()
start = time.time()
g = list_files(string)
end = time.time()
print('Time: '+str(round(end - start, 6)))
# print(g.edge_count())
# print(g.vertex_count())
# napraviti glavni meni koji ze imati petlju i praviti te uslove iz zahteva

def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        # print(current)
        pos = i
        while pos > 0 and array[pos-1]["rang"] < current["rang"]:
            array[pos] = array[pos-1]
            pos = pos - 1
        array[pos] = current

def get_kontekst(path, word):
    # print(path["path"])
    parser = Parser()
    links, words1 = parser.parse(path["path"])
    words = []
    for t in words1:
        try:
            int(t)
        except ValueError:
            words.append(t.lower())
    # print(len(words))
    kontekst = []
    found = 0
    for w in range(len(words)):
        if words[w] == word:
            found = w
            break
    
    if found > 10 and found < (len(words)//2):
        for k in range(found-10, found+10):
            kontekst.append(words[k])
    elif found < 10:
        for k in range(0, 20):
            kontekst.append(words[k])
    elif found > (len(words)-20):
        for k in range(len(words)-20, len(words)):
            kontekst.append(words[k])
    elif found > (len(words)//2):
        for k in range(found, found+20):
            kontekst.append(words[k])

    string = "Kontekst: "
    for k in kontekst:
        string += " "+k
    print(string)


def print_top(array, num, word):
    if len(array)> 0:
        get_kontekst(array[0],word)
    if len(array) > num:
        for i in range(num):
            print(str(i+1)+". "+ array[i]["path"][12:]+" - "+ str(round(array[i]["rang"],2)))
    else:
        for i in range(len(array)):
            print(str(i+1)+". "+ array[i]["path"][12:]+" - "+ str(round(array[i]["rang"],2)))

def search_jedna_rec(graf, word):
    main = []
    start2 = time.time()
    for i in graf._incoming.keys():
        rang = i.get_rang(word)
        if rang != 0:
            # ako nema reci u dokumentu ne proveravati ni linkove
            for j in graf._incoming[i].keys():
                link_rang = j.get_rang(word)
                if link_rang != 0:
                    rang += 0.05 *link_rang
            main.append({"path": i._path, "rang": rang })
    end2 = time.time()
    print('Search time: '+str(round(end2 - start2, 6)))
    return main

def search_operator(graf, word1, word2, relation):
    fail = 0
    main = []
    start2 = time.time()
    for i in graf._incoming.keys():
        rang = i.get_rang(word1)
        rang2 = i.get_rang(word2)
        if relation(rang != 0, rang2 != 0):
            # ako nema obe reci u dokumentu ne proveravati ni linkove
            for j in graf._incoming[i].keys():
                link_rang = j.get_rang(word1)
                link_rang2 = j.get_rang(word2)
                if relation(link_rang != 0, link_rang2 != 0):
                    rang += (0.05 *link_rang)
                    rang2 += (0.05 *link_rang2)
                else:
                    fail +=1
            rang += rang2
            main.append({"path": i._path, "rang": rang })
    end2 = time.time()
    print('Search time: '+str(round(end2 - start2, 6)))
    print(fail)
    return main

def search_NOT(graf, word1, word2):
    fail = 0
    main = []
    start2 = time.time()
    for i in graf._incoming.keys():
        rang = i.get_rang(word1)
        rang2 = i.get_rang(word2)
        if rang != 0 and rang2 == 0:
            # ako nema obe reci u dokumentu ne proveravati ni linkove
            for j in graf._incoming[i].keys():
                link_rang = j.get_rang(word1)
                link_rang2 = j.get_rang(word2)
                if link_rang != 0 and link_rang2 == 0:
                    rang += (0.05 *link_rang)
            main.append({"path": i._path, "rang": rang })
    end2 = time.time()
    print('Search time: '+str(round(end2 - start2, 6)))
    print(fail)
    return main

def search_more_words(graf, words):
    main = []
    start2 = time.time()
    for i in graf._incoming.keys():
        big_rang = 0
        rangs = []
        for w in words:
            rangs.append({"word":w, "rang": i.get_rang(w)})
        for r in rangs:
            big_rang += r["rang"]
        if big_rang != 0:
            # ako je pronadjena bar jedna rec
            for j in graf._incoming[i].keys():
                big_link_rangs = 0
                link_rangs = []
                for l in rangs:
                    link_rangs.append(j.get_rang(l["word"]))
                for ll in link_rangs:
                    big_link_rangs += ll
                if big_link_rangs != 0:
                    for lll in link_rangs:
                        big_rang += (0.05 * lll)
            main.append({"path": i._path, "rang": big_rang })
    end2 = time.time()
    print('Search time: '+str(round(end2 - start2, 6)))
    return main

def search(graf):
    while True:
        word = input("Unesite upit za pretragu: ")
        main = []
        jedna = False
        if " " not in word:
            main = search_jedna_rec(graf, word)
            jedna = True
        else:
            word = word.split()
            print(word)
            
            if word[1] == "AND":
                main = search_operator(graf, word[0], word[2], operator.and_)
            elif word[1] == "OR":
                main = search_operator(graf, word[0], word[2], operator.or_)
            elif word[1] == "NOT":
                main = search_NOT(graf, word[0], word[2])
            else:
                main = search_more_words(graf, word)
        insertion_sort(main)
        if jedna:
            print_top(main, 5, word)
        else:
            print_top(main, 5, word[0])
        word2 = input("Nastavak: ")
        if word2 == "ne":
            break
search(g)

