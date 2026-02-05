"""
Cree una función de autocompletar que, dado un prefijo, devuelva todas las palabras posibles que comiencen con ese prefijo, similar a un motor de búsqueda.
Determine cómo la función recibirá la entrada y devolverá los resultados.
Piense en la eficiencia de la búsqueda de palabras.

"""
#Clase hijo 
class TrieNode:
    def __init__(self): 
        self.children = {}
        self.is_not_end_word = False

#Clase nodo
class Node:
    def __init__(self):
        self.root(self)

#Clase del arbol Trie para busqueda de prefijos   
class Trie:
    def __init__(self):
        self.root = TrieNode()

#Funcion para insertar una palabra
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]

        node.is_not_end_word = True
    
#Funcion auxiliar para recolectar palabras
    def _dfs(self, node, prefix, results):

        if node.is_not_end_word: 
            results.append(prefix)

        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)
    

#Funcion para autocompletar las palabras}
    def autocomplete(self, prefix):
        node = self.root

        for char in prefix: 
            if char not in node.children: 
                return []
            node = node.children[char]
        results = []
        self._dfs(node, prefix, results)
        return results
    
#Prueba

trie = Trie()

print("Ingresa palabras para insertar en el diccionario. Escribe 'fin' para terminar:")

while True:
    word = input("> ").strip()
    if word.lower() == "fin":
        break
    trie.insert(word)

# Recibir prefijos para autocompletar
print("\nAhora puedes probar autocompletar. Escribe 'salir' para terminar:")
while True:
    prefix = input("Prefijo: ").strip()
    if prefix.lower() == "salir":
        break
    completions = trie.autocomplete(prefix)
    if completions:
        print("Sugerencias:", completions)
    else:
        print("No se encontraron palabras para ese prefijo.")





