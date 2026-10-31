
# stores key value pairs
person = {
    "name": "Timmy",
    "age": 21,
    "city": "Toronto"
}
#access the name
print(person["name"])
#or safe lookup(avoid error)
print(person.get("name"))
#lets add something not in the dictornary
print(person.get("hobby"))
#see how it returns none

#lets add a new field in dict person
person["job"] = "Software Designer"
print(person.get("job"))