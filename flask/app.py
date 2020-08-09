from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql
from database import DatabaseConnection

app = Flask(__name__)

# Creating the Library System Database Object
library_system_DB = DatabaseConnection('IP','C9_USER',"",'library_system')

conn = library_system_DB.get_conn()

def create_cursor():
    library_system_cursor = conn.cursor()
    return library_system_cursor

# <--------------------------------STRONG ENTITIES----------------------------------->


# <---------------------------------CRUD PUBLISHERS ------------------------------->

# Display all publishers
@app.route('/publishers')
def show_publishers():
    cursor = create_cursor()
    try:
        sql = "select * from publishers"
        cursor.execute(sql)
        return render_template('display/show_publishers.template.html',publishers=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))

# Create the publisher and add to the database
@app.route('/publishers/create',methods=['POST','GET'])
def create_publishers():
    if request.method =='GET':
        try:
            return render_template('create/create_publishers.template.html')
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO publishers (fname,faddress,contact_email) VALUES (%s,%s,%s)
            """
            cursor.execute(sql,[
                request.form.get('fname'),
                request.form.get('faddress'),
                request.form.get('contact_email')
            ])
            conn.commit()
            return "The Publisher has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))


# Edits the publisher in the database
@app.route('/publishers/edit/<publisher_id>',methods=['POST','GET'])
def edit_publishers(publisher_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from publishers where publisher_id = %s
            """
            cursor.execute(sql,(publisher_id))
            publishers = cursor.fetchone()

            return render_template('edit/edit_publishers.template.html',publishers=publishers)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update publishers set fname=%s, faddress=%s, contact_email=%s where publisher_id=%s
            """
            cursor.execute(sql,[
                request.form.get('fname'),
                request.form.get('faddress'),
                request.form.get('contact_email'),
                publisher_id
            ])

            conn.commit()
            return "The Publisher has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


#deletes the publisher in the database
@app.route('/publishers/delete/<publisher_id>', methods=['GET','POST'])
def delete_publishers(publisher_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from publishers where publisher_id = %s
            """
            cursor.execute(sql,(publisher_id))
            publishers = cursor.fetchone()
            return render_template("delete/delete_publishers.template.html",publishers=publishers)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from publishers where publisher_id = %s
            """
            cursor.execute(sql,(publisher_id))
            conn.commit()
            return "The Publisher has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))



# <---------------------------------CRUD AUTHORS ---------------------------------->


@app.route('/authors')
def show_authors():
    cursor = create_cursor()
    try:
        sql = "select * from authors"
        cursor.execute(sql)
        return render_template('display/show_authors.template.html',authors=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))



# Create the author and add to the database
@app.route('/authors/create',methods=['POST','GET'])
def create_authors():
    if request.method =='GET':
        try:
            return render_template('create/create_authors.template.html')
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO authors (fname,lname,date_of_birth) VALUES (%s,%s,%s)
            """
            cursor.execute(sql,[
                request.form.get('fname'),
                request.form.get('lname'),
                request.form.get('date_of_birth')
            ])
            conn.commit()
            return "The Author has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))


# Edits the author in the database
@app.route('/authors/edit/<author_id>',methods=['POST','GET'])
def edit_authors(author_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from authors where author_id = %s
            """
            cursor.execute(sql,(author_id))
            authors = cursor.fetchone()

            return render_template('edit/edit_authors.template.html',authors=authors)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update authors set fname=%s, lname=%s, date_of_birth=%s where author_id=%s
            """
            
            cursor.execute(sql,[
                request.form.get('fname'),
                request.form.get('lname'),
                request.form.get('date_of_birth'),
                author_id
            ])

            conn.commit()
            return "The Author has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))



#deletes the author in the database
@app.route('/authors/delete/<author_id>', methods=['GET','POST'])
def delete_authors(author_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from authors where author_id = %s
            """
            cursor.execute(sql,(author_id))
            authors = cursor.fetchone()
            return render_template("delete/delete_authors.template.html",authors=authors)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from authors where author_id = %s
            """
            cursor.execute(sql,(author_id))
            conn.commit()
            return "The Author has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


# <----------------------------------CRUD MEMBERS -------------------------------->

# Display all members
@app.route('/members')
def show_members():
    cursor = create_cursor()
    try:
        sql = "select * from members"
        cursor.execute(sql)
        return render_template('display/show_members.template.html',members=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))


# Create the member and add to the database
@app.route('/members/create',methods=['POST','GET'])
def create_members():
    if request.method =='GET':
        try:
            return render_template('create/create_members.template.html')
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO members (fname,lname,faddress) VALUES (%s,%s,%s)
            """
            cursor.execute(sql,[
                request.form.get('fname'),
                request.form.get('lname'),
                request.form.get('faddress')
            ])
            conn.commit()
            return "The Member has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))


# Edit the member in the database
@app.route('/members/edit/<member_id>',methods=['POST','GET'])
def edit_members(member_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from members where member_id = %s
            """
            cursor.execute(sql,(member_id))
            members=cursor.fetchone()

            return render_template('edit/edit_members.template.html',members=members)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update members set fname=%s, lname=%s, faddress=%s where member_id=%s
            """
            
            cursor.execute(sql,[
                request.form.get('fname'),
                request.form.get('lname'),
                request.form.get('faddress'),
                member_id
            ])

            conn.commit()
            return "The Member has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


#deletes the member in the database
@app.route('/members/delete/<member_id>', methods=['GET','POST'])
def delete_members(member_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from members where member_id = %s
            """
            cursor.execute(sql,(member_id))
            members = cursor.fetchone()
            return render_template("delete/delete_members.template.html",members=members)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from members where member_id = %s
            """
            cursor.execute(sql,(member_id))
            conn.commit()
            return "The Member has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))




#  <--------------------------------CRUD BOOKS ----------------------------------->

# Display all books
@app.route('/books')
def show_books():
    cursor = create_cursor()
    try:
        sql = "select * from books"
        cursor.execute(sql)
        return render_template('display/show_books.template.html',books=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))
    
# Creates the Book and Add to Database
@app.route('/books/create',methods=['POST','GET'])
def create_books():
    if request.method =='GET':
        try:
            return render_template('create/create_books.template.html')
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO books (title) VALUES (%s)
            """
            cursor.execute(sql,
            (request.form.get('title')))
            conn.commit()
            return "Your Book has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))

#Edits the Book in the database
@app.route('/books/edit/<book_id>',methods=['POST','GET'])
def edit_books(book_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from books where book_id = %s
            """
            cursor.execute(sql,(book_id))
            books = cursor.fetchone()

            return render_template('edit/edit_books.template.html',books=books)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update books set title=%s where book_id =%s
            """
            cursor.execute(sql,(request.form.get('title'),book_id))

            conn.commit()
            return "Your Book has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))

# Deletes the book from the database
@app.route('/books/delete/<book_id>', methods=['GET','POST'])
def delete_books(book_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from books where book_id = %s
            """
            cursor.execute(sql,(book_id))
            books = cursor.fetchone()
            return render_template("delete/delete_books.template.html",books=books)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from books where book_id = %s
            """
            cursor.execute(sql,(book_id))
            conn.commit()
            return "Your Book has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


# <------------------------------------ END OF STRONG ENTITIES ------------------------------------->

# <--------------------------CRUD EDITIONS ---------------------------------->
# displays all the editions
@app.route('/editions')
def show_editions():
    cursor = create_cursor()
    try:
        sql = "select * from editions"
        cursor.execute(sql)
        return render_template('display/show_editions.template.html',editions=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))


# Create the edition and add to the database
@app.route('/editions/create',methods=['POST','GET'])
def create_editions():
    if request.method =='GET':
        try:
            cursor= create_cursor()
            cursor.execute("select publisher_id from publishers")
            bookCursor = create_cursor()
            bookCursor.execute("select book_id from books")
            return render_template('create/create_editions.template.html',books=bookCursor,publishers=cursor)
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO editions (isbn,publisher_id,book_id) VALUES (%s,%s,%s)
            """
            cursor.execute(sql,[
                request.form.get('isbn'),
                request.form.get('publisher_id'),
                request.form.get('book_id')
            ])
            conn.commit()
            return "The Edition has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))


# Edit the edition in the database
@app.route('/editions/edit/<edition_id>',methods=['POST','GET'])
def edit_editions(edition_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from editions where edition_id = %s
            """
            cursor.execute(sql,(edition_id))
            editions=cursor.fetchone()

            publisherCursor = create_cursor()
            publisherCursor.execute("select * from publishers")

            bookCursor = create_cursor()
            bookCursor.execute("select * from books")

            return render_template('edit/edit_editions.template.html',editions=editions,
                                    books=bookCursor,publishers=publisherCursor)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update editions set isbn=%s, publisher_id=%s, book_id=%s where edition_id=%s
            """
            
            cursor.execute(sql,[
                request.form.get('isbn'),
                request.form.get('publisher_id'),
                request.form.get('book_id'),
                edition_id
            ])

            conn.commit()
            return "The Edition has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


#deletes the edition in the database
@app.route('/editions/delete/<edition_id>', methods=['GET','POST'])
def delete_editions(edition_id):
    if request.method == "GET":
        cursor =create_cursor()
        try:
            sql = """
                select * from editions where edition_id = %s
            """
            cursor.execute(sql,(edition_id))
            editions = cursor.fetchone()
            return render_template("delete/delete_editions.template.html",editions=editions)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from editions where edition_id = %s
            """
            cursor.execute(sql,(edition_id))
            conn.commit()
            return "The Edition has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))



# <--------------------------------------------CRUD WritingCredits---------------------------------------------->

# Displays all writingcredits
@app.route('/writingcredits')
def show_writingcredits():
    cursor = create_cursor()
    try:
        sql = "select * from writingCredits"
        cursor.execute(sql)
        return render_template('display/show_writingcredits.template.html',writingCredits=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))



# Create the writingcredit and add to the database
@app.route('/writingcredits/create',methods=['POST','GET'])
def create_writingcredits():
    if request.method =='GET':
        try:
            cursor= create_cursor()
            cursor.execute("select author_id from authors")
            bookCursor = create_cursor()
            bookCursor.execute("select book_id from books")
            return render_template('create/create_writingcredits.template.html',books=bookCursor,authors=cursor)
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO writingCredits (author_id,book_id) VALUES (%s,%s)
            """
            cursor.execute(sql,[
                request.form.get('author_id'),
                request.form.get('book_id')
            ])
            conn.commit()
            return "The Writing Credit has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))


# Edit the writingcredit in the database
@app.route('/writingcredits/edit/<writing_credit_id>',methods=['POST','GET'])
def edit_writingcredits(writing_credit_id):
    if request.method == "GET":
        try:
            
            authorCursor = create_cursor()
            authorCursor.execute("select * from authors")

            bookCursor = create_cursor()
            bookCursor.execute("select * from books")

            return render_template('edit/edit_writingcredits.template.html',
                                    books=bookCursor,authors=authorCursor)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update writingCredits set  author_id=%s, book_id=%s where writing_credit_id=%s
            """
            
            cursor.execute(sql,[
                request.form.get('author_id'),
                request.form.get('book_id'),
                writing_credit_id
            ])

            conn.commit()
            return "The Writing Credit has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


#deletes the writing credit in the database
@app.route('/writingcredits/delete/<writing_credit_id>', methods=['GET','POST'])
def delete_writingcredits(writing_credit_id):
    if request.method == "GET":
        try:
            return render_template("delete/delete_writingcredits.template.html")
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from writingCredits where writing_credit_id = %s
            """
            cursor.execute(sql,(writing_credit_id))
            conn.commit()
            return "The Writing Credit has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))



# <--------------------------------------------CRUD Reservations---------------------------------------------->

# Displays all reservations
@app.route('/reservations')
def show_reservations():
    cursor = create_cursor()
    try:
        sql = "select * from reservations"
        cursor.execute(sql)
        return render_template('display/show_reservations.template.html',reservations=cursor)
    except Exception as e:
        return render_template('errors.template.html',error_msg = str(e))

# create the reservation and add to the database
@app.route('/reservations/create',methods=['POST','GET'])
def create_reservations():
    if request.method =='GET':
        try:
            cursor= create_cursor()
            cursor.execute("select member_id from members")
            return render_template('create/create_reservations.template.html',members=cursor)
        except Exception as e:
            return render_template('errors.template.html',error_msg = str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                INSERT INTO reservations (member_id) VALUES (%s)
            """
            cursor.execute(sql,[
                request.form.get('member_id')
            ])
            conn.commit()
            return "The reservation has been recorded into our database"

        except Exception as e:
            return render_template('errors.template.html',error_msg= str(e))


# Edit the reservation in the database
@app.route('/reservations/edit/<reservation_id>',methods=['POST','GET'])
def edit_reservations(reservation_id):
    if request.method == "GET":
        try:
            
            memberCursor = create_cursor()
            memberCursor.execute("select * from members")


            return render_template('edit/edit_reservations.template.html',
                                    members=memberCursor)
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor=create_cursor()
        try:
            sql= """
                update reservations set  member_id=%s where reservation_id = %s
            """
            
            cursor.execute(sql,[
                request.form.get('member_id'),
                reservation_id
            ])

            conn.commit()
            return "The Reservation has been updated in our database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))


# Delete the reservation from the database
@app.route('/reservations/delete/<reservation_id>', methods=['GET','POST'])
def delete_reservations(reservation_id):
    if request.method == "GET":
        try:
            return render_template("delete/delete_reservations.template.html")
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))
    else:
        cursor = create_cursor()
        try:
            sql = """
                delete from reservations where reservation_id = %s
            """
            cursor.execute(sql,(reservation_id))
            conn.commit()
            return "The Reservation has been deleted from the database"
        except Exception as e:
            return render_template('errors.template.html',error_msg =str(e))





if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
        