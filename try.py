a = '''{
  "books": [
    {
      "bookId": 1,
      "bookName": "Koko the jumper",
      "author": "Zamari",
      "category": "adventure",
      "language": "english",
      "age": "12",
      "grade": "6"
    },
    {
      "bookId": 2,
      "bookName": "Mathematics for primary",
      "author": "KIE",
      "category": "mathematics",
      "language": "english",
      "age": "10",
      "grade": "4"
    },
    {
      "bookId": 3,
      "bookName": "Kamusi ya methali",
      "author": "KIE",
      "category": "kiswahili",
      "language": "kiswahili",
      "age": "13",
      "grade": "7"
    },
    {
      "bookId": 4,
      "bookName": "Science Experiments",
      "author": "Professor Science",
      "category": "science",
      "language": "science",
      "age": "all",
      "grade": "all"
    },
    {
      "bookId": 5,
      "bookName": "Kamusi ya methali",
      "author": "KIE",
      "category": "kiswahili",
      "language": "kiswahili",
      "age": "13",
      "grade": "7"
    },
    {
      "bookId": 6,
      "bookName": "Underwater",
      "author": "John Plums",
      "category": "adventure",
      "language": "English",
      "age": "14",
      "grade": "8"
    }
  ]
}
'''



data = json.loads(a)
for book in data['books']:
    print(book['bookId'])