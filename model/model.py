import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=nx.DiGraph()
        self._idMapArtisti = {}


    def getAllGeneri(self):
        return DAO.getAllGeneri()  #lista di oggetti di tipo genere

    def buildGrpah(self, genere_id):
        nodes = DAO.getAllNodes(genere_id)  #tutti i nodi
        self._graph.add_nodes_from(nodes) #popolo grafo con i nodi
        self._idMapArtisti = {artista.ArtistId : artista for artista in nodes}
        self.addEdgesPesati(genere_id)

    def addEdgesPesati(self,genere_id):
        pesiArtisti = DAO.getPesoEdges(genere_id)
        for p in pesiArtisti:
           artista= self._idMapArtisti[p(1)]
           artista.popolarita=p(0)

        allEdges = DAO.getAllEdges(genere_id)
        for edge in allEdges:
            self._graph.add_edge(edge,)
