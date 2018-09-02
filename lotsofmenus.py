from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = scoped_session(DBSession)


User1 = User(name="Harsimran Singh", email="harsimransingh362@gmail.com",
	     picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


#Menu for Punjabi Dhaba
restaurant1 = Restaurant(name = "Punjabi Dhaba")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Sandwich", description = "grilled sandwich", price = "$1.9", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Burger", description = "Potato Burger with tikki", price = "$3.0", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Pasta", description = "Red and White creamy Pasta", price = "$3.99", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Noodeles", description = "Chesse Noodeles", price = "$5.0", restaurant = restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Drinks", description = "Different types of drinkes", price = "$1.99", restaurant = restaurant1)

session.add(menuItem5)
session.commit()



#Menu for Sip N Bite
restaurant2 = Restaurant(name = "Sip N Bite")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name = "Shakes", description = "Different types of variety like: Chocolate, Strawberry and many more", price = "$10.0", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Patties", description = "Corn Patties, Aloo Patties, Grilled Panner Patties", price = "$2",restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Spring Roll", description = "There are a large variety of filled, rolled appetizers or dim sum ", price = "$4", restaurant = restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Icecream", description = "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. ", price = "$6", restaurant = restaurant2)

session.add(menuItem4)
session.commit()


#Menu for Lords Fast Foods
restaurant1 = Restaurant(name = "Lords Fast Foods")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Prantha", description = "It consists of different types like: Potato, Cauliflower", price = "$5.5", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chinese Dumplings", description = "a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", price = "$7", restaurant = restaurant1)

session.add(menuItem2)
session.commit()


#Menu for Cafeteria
restaurant1 = Restaurant(name = "Cafeteria ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Chocolate Cake", description = "Chocolate cake or Chocolate gateau is a cake flavored with melted chocolate, cocoa powder", price = "$8.5", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Roti Thali", description = "Consists of Roti, Dal ,Salad, Yogurt", price = "$10",restaurant = restaurant1)

session.add(menuItem2)
session.commit()



#Menu for Cafe 25
restaurant1 = Restaurant(name = " Cafe 25")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Coffee", description = "Coffee is a brewed drink prepared from roasted coffee beans, which are the seeds of berries from the Coffea plant.", price = "$5", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken and Rice", description = "chicken rice is a dish adapted from early Chinese immigrants originally from Hainan province in southern China", price = "$6", restaurant = restaurant1)

session.add(menuItem2)
session.commit()




#Menu for Nescafe
restaurant1 = Restaurant(name = "Nescafe")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Coffee", description = "Coffee is a brewed drink prepared from roasted coffee beans, which are the seeds of berries from the Coffea plant.", price = "$5", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Cappuccino", description = "A cappuccino is an espresso-based coffee drink that originated in Italy, and is traditionally prepared with double espresso, and steamed milk foam", price = "$7", restaurant = restaurant1)

session.add(menuItem2)
session.commit()



#Menu for Cafe Coffee Day
restaurant1 = Restaurant(name = "Cafe Coffee Day")

session.add(restaurant1)
session.commit()



menuItem1 = MenuItem(name = "Alphonso Mango Milkshake", description = "Added milk, sugar (to taste or according to sweetness of mango) and ice-cubes. Blend until smooth and creamy and there are no mango chunks in it.", price = "$15",restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Black Forest Cake", description = "Black Forest cake has multiple layers of chocolate sponge cake, cherries, and whipped cream", price = "$19", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Big Crunch Veg Spicy Burger", description = "Flavourful veggie patty cooked to perfection", price = "$14", restaurant = restaurant1)

session.add(menuItem3)
session.commit()



print ("added menu items!")
