graph = {'Lampung': ['Cikarang', 'Bekasi','Kalimantan'],
             'Cikarang': ['Lampung', 'Jakarta'],
             'Jakarta': ['Cikarang','Cibeureum'],
             'Cibeureum': ['Jakarta','Legok'],
             'Legok': ['Cibeureum','Sulawesi'],
             'Sulawesi': ['Legok','Bekasi'],
             'Bekasi': ['Lampung', 'Kalimantan', 'Sulawesi'],
             'Kalimantan': ['Buahdua', 'Lampung'],
         }
 
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Kota di Indonesia")
print ("(Lampung,Cikarang,Jakarta,Cibeureum)")
print ("(Legok,Sulawesi,Bekasi,Kalimantan)")
print ("\n")
awal = raw_input("Titik Awal : ")
tujuan = raw_input("Titik Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
