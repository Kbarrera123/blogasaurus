#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.appengine.api import users
import jinja2
import webapp2
import os

env=jinja2.Environment(loader=jinja2.FileSystemLoader(''))
"""
navigation_variables = dict(
    animal_pictures_link=users.create_login_url("/Animal_Pictures"),
    art_link=users.create_login_url("/Art"),
    contact_me_link=users.create_login_url("/Contact_Me"),
    home_link=users.create_login_url("/"),)
)
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in with a Google account</a>' %
                users.create_login_url('/'))
        # self.response.write('<html><body>%s</body></html>' % greeting)
        template = env.get_template('html_files/Kayla.html')
        self.response.write(template.render(greeting=greeting,
                                            user=user,
                                            animal_pictures_link=users.create_login_url("/Animal_Pictures"),
                                            art_link=users.create_login_url("/Art"),
                                            contact_me_link=users.create_login_url("/Contact_Me"),
                                            home_link=users.create_login_url("/"),))







class AnimalHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('html_files/Animal_Pictures.html')
        # self.response.write(template.render(navigation_variables)
        self.response.write(template.render(#greeting=greeting,
                                            #user=user,
                                            animal_pictures_link=users.create_login_url("/Animal_Pictures"),
                                            art_link=users.create_login_url("/Art"),
                                            contact_me_link=users.create_login_url("/Contact_Me"),
                                            home_link=users.create_login_url("/"),))

class ArtHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('html_files/Art.html')
        self.response.write(template.render(#greeting=greeting,
                                            #user=user,
                                            animal_pictures_link=users.create_login_url("/Animal_Pictures"),
                                            art_link=users.create_login_url("/Art"),
                                            contact_me_link=users.create_login_url("/Contact_Me"),
                                            home_link=users.create_login_url("/"),))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('html_files/Contact_Me.html')
        self.response.write(template.render(#greeting=greeting,
                                            #user=user,
                                            animal_pictures_link=users.create_login_url("/Animal_Pictures"),
                                            art_link=users.create_login_url("/Art"),
                                            contact_me_link=users.create_login_url("/Contact_Me"),
                                            home_link=users.create_login_url("/"),))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Animal_Pictures', AnimalHandler),
    ('/Art', ArtHandler),
    ('/Contact_Me', ContactHandler),


], debug=True)
