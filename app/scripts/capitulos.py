from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder 
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
				 RecycleGridLayout):
	pass
class SelectableButton(RecycleDataViewBehavior, Button):
	def on_press(self):
		
		popup = ExercícioPopup(self)
		popup.open() 

class ExercícioPopup(Popup): 
	id_exercicio = ObjectProperty(None)
	txt_enunciado = ObjectProperty(None)
	def __init__(self, obj, **kwargs):
		super(ExercícioPopup, self).__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor
		sql = "SELECT  id, capitulo, enunciado, pagina FROM tb_exercicios WHERE enunciado = ? ORDER BY id ASC"""
		self.cursor.execute(sql, (obj.text,))
		exercicio = self.cursor.fetchone()
		if exercicio is not None: 
			self.id_exercicio.text =str(exercicio[0])
			self.txt_enunciado.text =str(exercicio[2])


Builder.load_file("gui/capitulos.kv")

class Sc_Capitulos(Screen):
	campo_busca = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Sc_Capitulos, self).__init__(**kwargs)
		self.current_app = App.get_running_app()

	def leitura_c1(self):
		print("capitulo 1 página 1")
	def exercicios_c1(self):
		print("exercício página 20")
	def solucao_exercicio(self, ex, md):		
		if md == "m1":
			print("solucionar exercício " +ex + " com papel e caneta")
		elif md == "m2":
			print("solucionar exercício " +ex + " com calculadora")
		elif md == "m3":
			print("solucionar exercício " +ex + " com algoritmo")
		elif md == "m4":
			print("solucionar exercício " +ex + " com software")
		elif md == "m5":
			print("solucionar exercício " +ex + " modo completo")


	def on_enter(self): 
		self.criar_tabelas()
		self.buscar_exercicio("", True)		

	def buscar_exercicio(self, text="", search=False):
		def selecionar_exercicio(text):
			self.ids.rv.data.append(
				{
					"viewclass": "SelectableButton",
					"text": text,
					"callback": lambda x: x,
				}
			)
		self.ids.rv.data = []
		with self.current_app.conexao:
			self.current_app.cursor.execute("SELECT  id, capitulo, enunciado, pagina FROM tb_exercicios ORDER BY id ASC")
			rows = self.current_app.cursor.fetchall()
			for conteudo in rows:
				if search:
					if text.lower() in conteudo[2].lower() or text.lower() in conteudo[2].lower():
						selecionar_exercicio(conteudo[2])
				else:
					selecionar_exercicio(conteudo[2])

	def inserir_capitulos(self):
		sql = "INSERT INTO tb_capitulos(id_capitulo, titulo, tema, paginas) VALUES (1, 'Revisão do Ensino Fundamental', 'Matemática Básica', 100)"
		self.current_app.cursor.execute(sql)
		self.current_app.conexao.commit()

	def inserir_exercicios(self):		
		lista = [[1, 1, 'Exercício 1 texto', 10],[2, 1, 'Exercício 2 problema 2', 10],[3, 1, 'Exercício 3 problema 3', 10],[4, 1, 'Exercício 4 problema 4', 11],[5, 1, 'Exercício 5 problema 5', 12]]

		for item in lista:
			
			exercicios_data = (item[0], item[1], item[2], item[3])
			self.current_app.cursor.execute("INSERT INTO tb_exercicios(id, capitulo, enunciado, pagina) VALUES (?, ?, ?, ?)", exercicios_data)
			self.current_app.conexao.commit()
			
	def criar_tabelas(self):
		self.current_app.cursor.execute("PRAGMA foreign_keys = ON;")
		sql_capitulos = "CREATE TABLE IF NOT EXISTS tb_capitulos(id_capitulo integer PRIMARY KEY, titulo text NOT NULL, tema text NOT NULL, paginas integer NOT NULL)"

		self.current_app.conexao.execute(sql_capitulos)
		self.current_app.cursor.execute("SELECT * FROM tb_capitulos")
		data = self.current_app.cursor.fetchall()
		if len(data)==0 or data==None:
			self.inserir_capitulos()

		sql_exercicios = "CREATE TABLE IF NOT EXISTS tb_exercicios(id integer PRIMARY KEY, capitulo integer KEY, enunciado text NOT NULL, pagina text NOT NULL, FOREIGN KEY(capitulo) REFERENCES tb_capitulos(id_capitulo))"

		self.current_app.conexao.execute(sql_exercicios)
		self.current_app.cursor.execute("SELECT * FROM tb_exercicios")
		data = self.current_app.cursor.fetchall()
		if len(data)==0 or data==None:
			self.inserir_exercicios()


def leitura_cap01():
	Sc_Capitulos().leitura_c1()
	Sc_Capitulos().exercicios_c1()
	Sc_Capitulos().solucao_exercicio("ex1", "m5")

