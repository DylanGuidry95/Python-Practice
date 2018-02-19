def list():
    collection = [1,4,2,4,21,9,0,23,1,3,4,100,230]
    new_collection = []
    for item in collection:
        if item < 5:
            new_collection.append(item)
    print new_collection

list()