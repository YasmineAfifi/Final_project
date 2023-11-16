import flask

app = flask.Flask('adress_book')
# function for return html page that i call 
def get_html(page_name):
  html_page = open(page_name+".html")
  content = html_page.read()
  html_page.close()
  return content

# function return my contacts 
def contact():
  contacts = open("contact.txt")
  contact_list = contacts.read()
  user_contact = contact_list.split("\n")
  contacts.close()

  return user_contact


# function for display contacts in html 
@app.route('/contact')
def get_All_contact():
  contact_page = get_html("contact")
  users = contact()
  user_contacts = ""
  for user in users:
    user_contacts +="<p>"+user+"</p>"
  return contact_page.replace("$$contact_list$$",user_contacts)

@app.route("/")
def index_page():
    index_page = get_html("index")
    return index_page
