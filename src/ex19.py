def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("Or we can do something like this.")
print("Enter number of cheeses you want: ")
cheese_count = input("> ")
print("Enter number of boxes of crackers you want: ")
boxes_of_crackers = input("> ")
cheese_and_crackers(cheese_count, boxes_of_crackers)

print("Or we can do something like this.")
another_cheese_count = 20
another_boxes_of_crackers = 30
cheese_and_crackers(another_cheese_count, another_boxes_of_crackers)

print("Or we can do something like this.")
cheese_and_crackers(20 + 5, 30 + 5)
