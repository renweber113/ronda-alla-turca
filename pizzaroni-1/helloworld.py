#http://www.youtube.com/watch?v=U1KhwqVa9fo
  
import webapp2
import cgi
import os
import jinja2
from gaesessions import get_current_session
 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        firstName = session.get('firstName', '')
        familyName = session.get('familyName', '')
        message = session.get('message', '')
        jinja_environment = jinja2.Environment(autoescape = True,
            loader = jinja2.FileSystemLoader(os.path.join(
               os.path.dirname(__file__), 'templates')))
        tpl_vars = { "message": message, "firstName": firstName,
            "familyName": familyName }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(tpl_vars))
    
    def post(self):
        firstName = self.request.get("firstName")
        familyName = self.request.get("familyName")
        session = get_current_session()
        session['firstName'] = firstName
        session['familyName'] = familyName
        session['message'] = ''
        if len(firstName) < 2 or len(familyName) < 2:
            session['message'] = "First Name and Family Name are mandatory"
            self.redirect("/")
        self.response.out.write("First Name: " + firstName
           + " Family Name: " + familyName)
 
app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)

