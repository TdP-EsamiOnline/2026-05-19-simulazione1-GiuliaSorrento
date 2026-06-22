from model.model import Model

mymodel = Model()
mymodel.buildGrpah(7)

nodi, archi = mymodel.get_graph_details()
print(nodi, archi)

artista,influenza = mymodel.getBestArtist()
print(artista, influenza)

#archimaggiori = mymodel.archi_maggiori()
#for u,v,data in archimaggiori:
    #print(f"arco {u.Name}-{v.Name}-{data["weight"]}")