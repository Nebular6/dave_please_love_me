#try to complete a recursive linear search, returning the index of the item, or -1
def linear_search_recursive(items, search_item, n):
    n =+ 1
    if items[0] == search_item:
        return print("position ",n,)
    elif len(items) <= 0:
        return "false"
    else:
        x = len(items)
        return linear_search_recursive(items[1:x], search_item, n)

#print(linear_search_recursive([1,2,3,4,5,6,7,8,9],10,-1))