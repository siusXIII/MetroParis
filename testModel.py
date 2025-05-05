from model.fermata import Fermata
from model.model import Model

model = Model()
model.buildGraphPesato()
print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())


f = Fermata(2, "Abbesses", 2.33855,	48.8843)
nodesBFS = model.getBFSNodesFromTree(f)
# for nodi in nodesBFS:
#     print(nodi)

nodesDFS = model.getDFSNodesFromTree(f)
# for nodi in nodesDFS:
#     print(nodi)

nodesFromEdgesB = model.getBFSNodesFromEdges(f)
# for node in nodesFromEdgesB:
#     print(node)

nodesFromEdgesD = model.getDFSNodesFromEdges(f)
# for node in nodesFromEdgesD:
#     print(node)

archiMaggiori = model.getArchiPesoMaggiore()
for a in archiMaggiori:
    print(a)