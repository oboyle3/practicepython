person = {
    "nm1": "Pat",
    "fav_food_nm1": "apples",
    "nm2": "Jim",
    "fav_food_nm2": "cherrys",
    "nm3": "Jack",
    "fav_food_nm3": "pears",

}
#task 1 print one persons favorite food:
print(f"{person.get("nm1")}'s favorite food is {person.get("fav_food_nm1")}")
#task 2 add a new name to the dictonary and add a score and level 
person.update({"nm4": "Tommy","score":10, "level":2})
print(f" person after update {person}")
#task 3  Create a dictionary of three book titles and their authors
# Use .get() to look up a title that isn’t in the dictionary, with "Not found" as the default value.
books = {
    "title1": "The Summons",
    "title2": "The Lawyer",
    "title3": "The Hobbit",
}
print(f"lets check for title4 (not in dictionary) {books.get("title4")}")
#task 4 count the elements
groceries = {"apples": 4, "bread": 1, "eggs": 12}
counter = 0
for y in groceries:
    counter = counter+1
    print(y)
print(f"items in groceries list = {counter}")
#task 5 