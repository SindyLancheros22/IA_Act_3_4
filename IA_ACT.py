class SistemaTransporte:
    def __init__(self, grafo):
        self.grafo = grafo

    def encontrar_ruta(self, origen, destino):
        visitado = set()
        return self.dfs(origen, destino, visitado)

    def dfs(self, actual, destino, visitado):
        if actual == destino:
            return [actual]
        
        visitado.add(actual)
        
        for vecino in self.grafo[actual]:
            if vecino not in visitado:
                ruta = self.dfs(vecino, destino, visitado)
                if ruta:
                    return [actual] + ruta

        return None


# Ejemplo de uso
if __name__ == "__main__":
    # Base de conocimiento: grafo representando las conexiones entre estaciones
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B', 'F'],
        'E': ['C', 'F'],
        'F': ['D', 'E']
    }

    sistema = SistemaTransporte(grafo)
    origen = 'A'
    destino = 'F'
    mejor_ruta = sistema.encontrar_ruta(origen, destino)

    if mejor_ruta:
        print("La mejor ruta desde {} hasta {} es:".format(origen, destino))
        print(" -> ".join(mejor_ruta))
    else:
        print("No se encontró una ruta desde {} hasta {}".format(origen, destino))
