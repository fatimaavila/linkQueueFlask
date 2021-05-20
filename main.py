from flask import Flask, render_template, request
from random import choice
from linked_list import LinkedList, Node
from queue import Queue
from sort import selSort
#from search import linearSearch

web_site = Flask(__name__)

lista2 = Queue()
sorteado = []

@web_site.route('/')
def index():
	return render_template('index.html',lista=lista2,A_sorted=sorteado )

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
  m_prioridad=request.args.get('prioridad')
  lista2.enqueue(Node(m_link +'|'+m_nombre+'|'+m_prioridad))
  A_sorted=selSort(sorteado)
  #print(lista2)
  #todo A_sorted=selSort(sorteado)
  #todo format A_sorted
  return render_template('index.html',lista=lista2, A_sorted=sorteado)

@web_site.route('/dequeue')  
def dequeue():
  lista2.dequeue()
  return render_template('index.html',lista=lista2)


web_site.run(host='0.0.0.0', port=8080)