# Database code for the DB Forum, full solution!

import psycopg2		#i don't think we need bleach in this one:   , bleach

DBNAME = "news"

def getMostPop3():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute('''	select path, count(id) as views
				from log
				where path <> '/'
				group by path
				order by views desc
				limit 3;
				''')
  mostPopular3 = c.fetchall()
  db.close()
  return mostPopular3

#def get_posts():
#  """Return all posts from the 'database', most recent first."""
#  db = psycopg2.connect(database=DBNAME)
#  c = db.cursor()
#  c.execute("select content, time from posts order by time desc")
#  posts = c.fetchall()
#  db.close()
#  return posts

#def add_post(content):
#  """Add a post to the 'database' with the current timestamp."""
#  db = psycopg2.connect(database=DBNAME)
#  c = db.cursor()
#  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
#  db.commit()
#  db.close()



