"""
#Diseñe un sistema que permita a los usuarios navegar por las páginas web, 
incluida la capacidad de volver a la página anterior y avanzar a la página 
siguiente, de forma similar a como funcionan los navegadores web modernos.
"""
#Clase para Navegar entre paginas (se definen los estados de cada metodo)
class BrowserNavigation:
    def __init__(self):
        self.backStack= [ ]
        self.forwardStack= [ ]
        self.currentPage= None  

    #Carga una nueva pagina
    def loadPage(self, url):
        if self.currentPage == url:
            return

        elif self.currentPage is not None:
            self.backStack.append(self.currentPage)

        self.currentPage = url
        self.forwardStack.clear()
        print(f"Pagina cargada: {self.currentPage}")

    #Vuelve a la pagina anterior si es posible
    def goBack(self):
        if not self.backStack:
            print("No hay pagina anterior para volver")
            return
        
        self.forwardStack.append(self.currentPage) 
        self.currentPage = self.backStack.pop()
        print(f"Volivste a la página: {self.currentPage}")

    #Avanza a la pagina siguiente si es posible
    def goForward(self):
        if not self.forwardStack:
            print ("No hay más páginas para avanzar")
            return 
        
        self.backStack.append(self.currentPage)
        self.currentPage = self.forwardStack.pop()
        print(f"Avanzaste a: {self.currentPage}")

    #Obtenemos el estado de la pagina
    def getStatus(self):
        print("----- ESTADO ACTUAL -----")
        print(f"Página actual: {self.currentPage}")
        print(f"Historial atrás: {self.backStack}")
        print(f"Historial adelante: {self.forwardStack}")
        print("-------------------------")

browser = BrowserNavigation()

#Menú de opciones para utilizar el navegador
while True:
    print(" === Menú de navegación ===")
    print("1. Cargar página")
    print("2. Ir atrás")
    print("3. Ir adelante")
    print("4. Ver estado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1": 
        url = input("Ingrese la Url de la pagina: ")
        browser.loadPage(url)
        if url: 
            browser.loadPage(url)
        else: 
            print("La URL no puede estar vacía.")

    elif opcion == "2":
        browser.goBack()

    elif opcion == "3": 
        browser.goForward()

    elif opcion == "4": 
        browser.getStatus()

    elif opcion == "5":
        print("Saliendo del navegador...")
        break

    else: 
        print("Opción invalida, intente nuevamente.") 
        