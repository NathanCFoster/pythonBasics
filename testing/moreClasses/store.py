from products import product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}
    def addProduct(self, newProduct, price, category, amnt):
        self.products[newProduct.lower()] = product(newProduct, price, category, amnt)
        print("You have shelved %d %ss in the %s aisle...\nThanks for your hard Work!" %(self.products[newProduct.lower()].numOfSelf, self.products[newProduct.lower()].name, self.products[newProduct.lower()].category))
        return self
    def sellProduct(self, product, id):
        for num in self.products[product.lower()].ids:
            if(id == num):
                self.products[product.lower()].sell(id)
                print("You have sold: %s for $%d\nThank you for shopping at %s!" %(product, self.products[product.lower()].numOfSelf, self.name))
                return self
        print("Couldn't find the ID, try again")
        return self
    def sellNonSpecProduct(self, product):
        self.products[product.lower()].numOfSelf -= 1
        print("You have sold: %s for $%d\nThank you for shopping at %s!" %(product, self.products[product.lower()].numOfSelf, self.name))
        return self
    def scanProducts(self, product):
        self.products[product.lower()].printInfo()
        return self
    def scanProduct(self, product, id):
        for num in self.products[product.lower()].ids:
            if(id == num):
                self.products[product.lower()].printInfo()
        return self
    def inflation(self,percentIncrease):
        for k in self.products:
            self.products[k].updatePrice(percentIncrease/100+1, True)
        return self
    def clearance(self, category, percentDiscount):
        self.products[category.lower()].updatePrice(percentDiscount/100+1,False)
        return self