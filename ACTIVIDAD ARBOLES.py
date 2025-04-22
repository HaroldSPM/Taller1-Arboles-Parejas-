class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if not self.raiz:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        direccion = input(f"¿Insertar {dato} a la izquierda (i) o derecha (d) de {nodo.dato}? ").lower()
        if direccion == 'i':
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._insertar_recursivo(nodo.izquierdo, dato)
        elif direccion == 'd':
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self._insertar_recursivo(nodo.derecho, dato)
        else:
            print("Opción inválida. Usa 'i' o 'd'.")
            self._insertar_recursivo(nodo, dato)

    def peso(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierdo), self._altura_recursiva(nodo.derecho))

    def orden(self):
        if not self.raiz:
            return 0
        from collections import deque
        cola = deque([self.raiz])
        max_nodos_en_nivel = 0
        while cola:
            nivel = len(cola)
            max_nodos_en_nivel = max(max_nodos_en_nivel, nivel)
            for _ in range(nivel):
                nodo = cola.popleft()
                if nodo.izquierdo:
                    cola.append(nodo.izquierdo)
                if nodo.derecho:
                    cola.append(nodo.derecho)
        return max_nodos_en_nivel

# --- Programa principal ---
arbol = ArbolBinario()

n = int(input("¿Cuántos nodos deseas ingresar? "))
for i in range(n):
    dato = input(f"Ingrese el valor para el nodo #{i + 1}: ")
    arbol.insertar(dato)

print(f"\nPeso del árbol: {arbol.peso()}")
print(f"Altura del árbol: {arbol.altura()}")
print(f"Orden del árbol: {arbol.orden()}")
