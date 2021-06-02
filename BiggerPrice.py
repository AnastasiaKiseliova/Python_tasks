import sys


def bigger_price(number=0, products=None):
    
    """ find biggest prices in list of dictionaries """

    if number > len(products):
        print("not enough items in the list")
        return -1

    if products:
        price_list = sorted(products, key=lambda k: k['price'], reverse=True) 
        
        result = []
        i = 0

        while i < number:
            result.append(price_list[i])
            i += 1
        return result
    else:
        print("price list is empty")
        return -1


if __name__ == "__main__":
    assert bigger_price(2, [
                        {"name": "bread", "price": 100},
                        {"name": "wine", "price": 138},
                        {"name": "meat", "price": 15},
                        {"name": "water", "price": 1}
                        ]) == [
                        {"name": "wine", "price": 138},
                        {"name": "bread", "price": 100}
                        ]
    assert bigger_price(1, [{"name": "pen", "price": 5},
                        {"name": "whiteboard", "price": 170}
                        ]) == [{"name": "whiteboard", "price": 170}]