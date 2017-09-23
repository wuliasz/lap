#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for

#from forumdb_initial import get_posts, add_post
from lapdb import getMostPop3

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Logs Analysis</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Logs Analysis</h1>
    <form method=post>


      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
<!---------
I WANT THREE BUTTONS... 
	1. What are the most popular three articles of all time?
	2. Who are the most popular article authors of all time?
	3. On which days did more than 1% of requests lead to errors?
	-------------->


    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
  #'''Main page of the forum.'''
  #posts = "".join(POST % (date, text) for text, date in get_posts())
  #html = HTML_WRAP % posts
  #return html

  #9/19/17 first the simple method... simply run each query and return the results
  #run a query. 
  ##	results = getMostPop3()
  ##	html = HTML_WRAP % results
  #return the html, which is HTML_WRAP % theQueryRecords  #but theQueryRecords replace the %s built into HTMLWRAP
  ##	return html
  return 'testing'


#@app.route('/', methods=['POST'])
#def post():
#  '''New post submission.'''
#  message = request.form['content']
#  add_post(message)
#  return redirect(url_for('main'))


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8001)
