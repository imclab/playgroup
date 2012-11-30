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
#

import os
import webapp2
from google.appengine.api import channel
from google.appengine.ext.webapp import template

class Recorder(webapp2.RequestHandler):
    def get(self):
        token = channel.create_channel('123456')
        
        template_values = {
            'token' : token
        }
        
        path = os.path.join(os.path.dirname(__file__), 'recorder.html')
        self.response.out.write(template.render(path, template_values))
    
app = webapp2.WSGIApplication([
    ('/', Recorder)
], debug=True)
