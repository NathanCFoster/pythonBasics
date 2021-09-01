from store import Store


wallyWorld = Store("Wally World").addProduct("cheese", 3, "dairy", 20).addProduct("milk", 5, "dairy", 15).addProduct("Roast Beef", 8, 'meat', 10).scanProducts(
    "Roast beef").sellProduct("Roast beef", 10).scanProducts("Roast beef").inflation(33).scanProducts("Milk").clearance("roast beef", 20).scanProducts("roast beef")
#Sooo because the id is completely random you have to try a few times before being able to sell the roast beef with a specific id... im not fixing that
