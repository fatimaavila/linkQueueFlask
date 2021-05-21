from flask import Flask, render_template, request
from random import choice
from linked_list import LinkedList, Node
from queue import Queue
from sort import selSort
from search import linearSearch
#from search import linearSearch

web_site = Flask(__name__)

lista2 = Queue()
linksy = []
sorteado = []


def gen_html():
  print(lista2)
  print(linksy)
  sorteado = selSort(linksy)
  #todo A_sorted=selSort(sorteado)
  #todo format A_sorted
  print(" Generar html del array")
  html=''
  for i in range(len(sorteado)):
    html=html + '<a href="'+sorteado[i].split("|")[0]+'" target="_blank">'+sorteado[i].split("|")[1]+'</a><br>'
  return html
#--------------------------- main 
@web_site.route('/')
def index():
  html=gen_html()
  return render_template('index.html',lista=lista2,a_sorted=html)

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
  #linksy.clear()
  lista2.enqueue(Node(m_link +'|'+m_nombre+'|'+m_prioridad)) 
  html = gen_html()
  return render_template('index.html',lista=lista2, a_sorted=html)

@web_site.route('/dequeue')  
def dequeue():
  lista2.dequeue()
  return render_template('index.html',lista=lista2)

@web_site.route('/search')  
def search():
  print("--------------------search")
  html = gen_html()
  print(request.args.get("buscar"))
  consulta = request.args.get("buscar")
  resultado=linearSearch(linksy,consulta)
  print(resultado)
  if(resultado == -1):
    resultado_text = "No ha ingresado este nombre :("
  else:
    resultado_text= ' <h4 style = "font-family:courier new,courier,monospace;"> ⬇️ Su resultado ⬇️ </h4> <a href="'+linksy[resultado].split("|")[0]+'" target="_blank">'+linksy[resultado].split("|")[1]+'</a>'

  return render_template('index.html',lista=lista2,a_sorted=html,resultado_search=resultado_text)


web_site.run(host='0.0.0.0', port=8080)