#Clase para sistema de recomendación 
class RecommendationSystem: 
    # Diccionario: usuario -> conjunto de productos comprados
    def __init__(self):
        self.user_purchases ={}

    #Funcion para añadir una compra al usuario n
    def addPurchase(self, user, product):
        
        if user not in self.user_purchases:
            self.user_purchases[user] = set()
        self.user_purchases[user].add(product)

    #Funcion para añadir una compra al usuario
    def getRecommendations(self, user):
        if user not in self.user_purchases:
            return []
        
        purchased = self.user_purchases[user]
        recomendations = set()

        for other_user, other_products in self.user_purchases.items():
            if other_user != user:
                if purchased & other_products:
                    recomendations.update(other_products)
        return list(recomendations - purchased)

if __name__ == "__main__":
    system = RecommendationSystem()

    # Compras de ejemplo
    system.addPurchase("Carlos", "Laptop")
    system.addPurchase("Carlos", "Mouse")

    system.addPurchase("Laura", "Laptop")
    system.addPurchase("Laura", "Teclado")

    system.addPurchase("Andres", "Mouse")
    system.addPurchase("Andres", "Audifonos")

    system.addPurchase("Sofia", "Laptop")
    system.addPurchase("Sofia", "Mouse")
    system.addPurchase("Sofia", "Base_refrigerante")

    print("Recomendaciones para Carlos:")
    print(system.getRecommendations("Carlos"))

    print("\nRecomendaciones para Laura:")
    print(system.getRecommendations("Laura"))

    print("\nRecomendaciones para Andres:")
    print(system.getRecommendations("Andres"))