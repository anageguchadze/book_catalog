Library Catalog Project
This project is a Django-based library catalog application that allows users to view, add, edit, and delete books. 
The app includes features like managing book details (title, author, genre, and publication year) through an easy-to-use interface. 
The admin panel is customized to display and manage the catalog of books efficiently.

Features
Book Management: Users can view, add, edit, and delete books.
Book Details: View detailed information for each book by its title.
Admin Panel: Customize and manage books via Django's admin interface.
User Authentication: Allows users to log in and log out for personalizing the experience.

Technologies Used
Django: Web framework for building the application.
Django Admin: For managing the catalog of books.
HTML/CSS: Frontend for displaying the catalog and book details.
SQLite: Default database for storing book information.

Installation
Clone the repository:
git clone https://github.com/anageguchadze/book_catalog.git


Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser (for admin access):
python manage.py createsuperuser

Run the development server:
python manage.py runserver
Access the application: Open http://127.0.0.1:8000/ in your browser.

Admin Panel: Access the admin panel at http://127.0.0.1:8000/admin/ to manage books.

File Structure
urls.py: Contains URL routing for different pages, including home, book details, add/edit/delete books, and user login/logout.
views.py: Includes the logic for rendering the views (book list, book details, etc.).
models.py: Defines the Book model, including fields for title, author, published year, and genre.
forms.py: Contains the form for adding and editing books.
templates/: Includes HTML templates for the application (e.g., index.html, book_detail.html, add_book.html).
admin.py: Registers the Book model with the admin interface and customizes the display.

File Descriptions
catalog/: Main app containing models, views, and URLs for managing books.
users/: App for handling user login and logout.
index.html: Displays the list of books.
book_detail.html: Displays details of a selected book.
add_book.html: Form for adding a new book.
edit_book.html: Form for editing an existing book.
delete_book.html: Confirmation page for deleting a book.

License
This project is licensed under the MIT License.
