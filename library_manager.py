import json
import os

data_file = "library.txt"

# Function to load the library data from a file
def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

# Function to save the library data to a file
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

# Function to add a book to the library
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = input("Enter the year of publication: ")
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    print(f"✅ Book '{title}' added to the library.")

# Function to remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    initial_length = len(library)
    library = [book for book in library if book["title"].lower() != title.lower()]

    if len(library) < initial_length:
        save_library(library)
        print(f"✅ Book '{title}' removed from the library.")
    else:
        print(f"❌ Book '{title}' not found in the library.")

# Function to search for books
def search_books(library):
    search_term = input("Enter a search term (title, author, genre): ").lower()
    results = [book for book in library if any(search_term in str(value).lower() for value in book.values())]

    if results:
        print("\n📚 Search results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("❌ No books found matching the search term.")

# Function to display all books in the library
def display_books(library):
    if library:
        print("\n📖 Books in the library:")
        for book in library:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("❌ The library is empty.")

# Function to display library statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"✅ Books read: {read_books}")
    print(f"📖 Books unread: {unread_books}")
    print(f"📈 Percentage of books read: {percentage_read:.2f}%")

# Main function to run the library program
def main():
    library = load_library()

    while True:
        print("Welcome to the Library Management System!")
        print("\n📚 Library Menu:")
        print("1️⃣ Add a book")
        print("2️⃣ Remove a book")
        print("3️⃣ Search for books")
        print("4️⃣ Display all books")
        print("5️⃣ Display statistics")
        print("6️⃣ Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("👋 Exiting Library Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
