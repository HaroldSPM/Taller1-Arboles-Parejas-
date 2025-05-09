from bigtree import Node, print_tree

# Crear nodo raíz (Director General)
director_general = Node("Director General")

# Añadir hijos al nodo raíz
director_tecnologia = Node("Director de Tecnología", parent=director_general)
director_finanzas = Node("Director de Finanzas", parent=director_general)
director_operaciones = Node("Director de Operaciones", parent=director_general)

# Añadir hijos al Director de Tecnología
gerente_desarollo = Node("Gerente de Desarrollo", parent=director_tecnologia)
gerente_calidad = Node("Gerente de Calidad", parent=director_tecnologia)

# Añadir hijos al Director de Finanzas
contador = Node("Contador", parent=director_finanzas)
analista_financiero = Node("Analista Financiero", parent=director_finanzas)

# Añadir hijos al Gerente de Desarrollo
Node("Desarrollador Backend", parent=gerente_desarollo)
Node("Desarrollador Frontend", parent=gerente_desarollo)

# Añadir hijo al Gerente de Calidad
Node("Ingeniero QA", parent=gerente_calidad)

# Mostrar árbol
print_tree(director_general)