import functools
import xmlrpc.client
HOST = 'localhost'
PORT = 80
DB = 'it4_db'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Logged in as %s (uid:%d)" % (USER,uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('it4life_academy.session','search_read', [], ['start_date','duration'])
for session in sessions:
    print("Session %s (%s duration)" % (session['start_date'], session['duration']))
# 3.create a new session
session_id = call('it4life_academy.session', 'create', {
    'start_date' : '10/05/2020',
    'course_id' : 2,
})
