import os
import time
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

def print_top(array, num):
    for i in range(num):
        print(str(i+1)+". "+ array[i]["path"][12:]+" - "+ str(round(array[i]["rang"],2)))

def search(graf):
    word = input("Unesite rec za pretragu: ")
    main = []
    start2 = time.time()
    for i in graf._incoming.keys():
        rang = i.get_rang(word)
        if rang != False:
            # ako nema reci u dokumentu ne proveravati ni linkove
            for j in graf._incoming[i].keys():
                link_rang = j.get_rang(word)
                if link_rang != False:
                    rang += 0.05 *link_rang
            main.append({"path": i._path, "rang": rang })
    end2 = time.time()
    print('Time2: '+str(round(end2 - start2, 6)))
    # print(main)
    insertion_sort(main)
    print_top(main, 5)
    
search(g)

