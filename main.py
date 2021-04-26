from flask import Flask, render_template, request
from random import choice
from linked_list import LinkedList, Node
from queue import Queue

web_site = Flask(__name__)

lista2 = Queue()

@web_site.route('/')
def index():
	return render_template('index.html',lista=lista2)

@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)

@web_site.route('/enqueue')
def enqueque():
  print(request.args.get("link"))
  print(request.args.get('nombre'))
  m_link=request.args.get('link')
  m_nombre=request.args.get('nombre')
  lista2.enqueue(Node(m_link +'|'+m_nombre))
  #print(lista2)
  return render_template('index.html',lista=lista2)

@web_site.route('/dequeue')  
def dequeue():
  lista2.dequeue()
  return render_template('index.html',lista=lista2)


web_site.run(host='0.0.0.0', port=8080)