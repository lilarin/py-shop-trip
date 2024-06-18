from datetime import datetime
from math import dist
from app.customer import Customer
from app.shop import Shop


def trip(customer: Customer, shops: list[Shop], fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    min_price = float("inf")
    min_shop = None

    for shop in shops:
        distance = dist(customer.location, shop.location)
        distance_price = (distance / 100) * customer.car.fuel_consumption * fuel_price * 2
        product_price = 0

        for product, amount in customer.product_cart.items():
            cost = shop.products[product] * amount
            product_price += cost

        if distance_price + product_price < min_price:
            min_price = distance_price + product_price
            min_shop = shop

        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {round(distance_price + product_price, 2)}")

    if min_price > customer.money:
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
        return

    print(f"{customer.name} rides to {min_shop.name}\n")

    current_date = datetime(
        2021, 1, 4, 12,33,41
    ).strftime("%d/%m/%Y %H:%M:%S")
    total_cost = 0

    print(f"Date: {current_date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")

    for product, amount in customer.product_cart.items():
        cost = min_shop.products[product] * amount
        if cost != int(cost):
            cost_str = str(round(cost, 2))
        else:
            cost_str = str(int(cost))
        print(f"{amount} {product}s for {cost_str} dollars")
        total_cost += cost

    print(f"Total cost is {total_cost} dollars")
    print("See you again!\n")

    print(f"{customer.name} rides home")

    customer.money -= min_price
    print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
