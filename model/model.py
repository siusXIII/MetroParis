from datetime import datetime

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGraph(self):
        # aggiungiamo i nodi
        # self._grafo.add_nodes_from(self._fermate)
        # tic = datetime.now()
        # self.addEdges1()
        # toc = datetime.now()
        # print("Tempo modo 1:", (toc-tic))
        #
        # self._grafo.clear_edges()
        # tic = datetime.now()
        # self.addEdges2()
        # toc = datetime.now()
        # print("Tempo modo 2:", (toc - tic))

        self._grafo.clear_edges()
        tic = datetime.now()
        self.addEdges3()
        toc = datetime.now()
        print("Tempo modo 3:", (toc - tic))

    def addEdges1(self):
        """
        Aggiungo gli archi con doppio ciclo sui nodi, testando se per ogni coppia esista una connessione
        """
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasConnessione(u, v):
                    self._grafo.add_edge(u, v)

    def addEdges2(self):
        """
        Ciclo solo una volta e faccio una query per trovare tutti i vicini.
        """
        for u in self._fermate:
            for con in DAO.getVicini(u):
                v = self._idMapFermate[con.id_stazA]
                self._grafo.add_edge(u,v)

    def addEdges3(self):
        """
        Faccio una query unica che prende tutti gli archi e li ciclo qui.
        """
        allEdges = DAO.getAllEdges()
        for edge in allEdges:
            u = self._idMapFermate[edge.id_stazP]
            v = self._idMapFermate[edge.id_stazA]
            self._grafo.add_edge(u, v)

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    @property
    def fermate(self):
        return self._fermate