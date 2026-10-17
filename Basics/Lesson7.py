# Dictionary is a collection of key-value pair
print("--------------------------------------------------")
authors = ['Paulo Coehlo', 'Second Author','Third Author']

firstBook = {'name':'The Alchemist', 'author': authors[0], 'Pages': 300, 'format':'hardcover'}
print("Type of myBook :", type(firstBook))
print("The Dictionary:", firstBook)
print("Author of the book:", firstBook['author'])
firstBook['format'] = 'Digital'
print("The new format of the book:" , firstBook['format'])

secondBook = dict({'name':'Introduction to Python', 'author': authors[1]})
# adding a key-value pair to the dictionary
secondBook['Pages'] = 450   
secondBook['format'] = 'Softcover'
print("Information about second book:", secondBook)
# removing a key-value from the dictionary
del secondBook['format']
print("Updated information about second book:", secondBook)
print("All the keys of the second book:", secondBook.keys())

# Assignment
print("-------------------------Assignment-------------------------")
countries = {'Austria':'Vienna', 'Belarus':'Minsk', 'China':'Beijing', 'Denmark':'Copenhagen', 'England':'London',
             'France':'Paris', 'Germany':'Berlin', 'Hungary':'Budapest', 'Iceland': 'Reyjavik','Japan':'Tokyo'}
print("Available countries", countries.keys())
country = input("Select a country from the above:").strip()
print("Capital of ", country," is ", countries[country])
print("-------------------------End of Assignment-------------------------")