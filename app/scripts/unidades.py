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
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
import scripts.solucoes as solucoes
import scripts.data as data

class ImageView(BoxLayout):
	imagem = StringProperty("")
	def __init__(self, **kwargs):
		super(ImageView, self).__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor		

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
				 RecycleGridLayout):
	pass

class SelectableButton(RecycleDataViewBehavior, Button):
	def on_press(self):		
		popup = ExercicioPopup(self)
		popup.open() 
class SolucaoCompButton(Button):
	def on_press(self):
		pop_soc = SolucaoCompPopup()
		pop_soc.open()

class SolucaoM1Button(Button):
	def on_press(self):		
		pop_m1 = SolucaoM1Popup()
		pop_m1.open() 

class SolucaoM2Button(Button):
	def on_press(self):		
		pop_m2 = SolucaoM2Popup()
		pop_m2.open() 

class SolucaoM3Button(Button):
	def on_press(self):		
		pop_m3 = SolucaoM3Popup()
		pop_m3.open() 

class SolucaoM4Button(Button):
	def on_press(self):		
		pop_m4 = SolucaoM4Popup()
		pop_m4.open()

class ExercicioPopup(Popup): 
	id_exercicio = ObjectProperty(None)	
	txt_enunciado = ObjectProperty(None)	
	image_layout = ObjectProperty(None)	
	acc = ObjectProperty(None)
	active_accordion = ObjectProperty(None)
	imagem = StringProperty("")
	img_view = ObjectProperty(None)
	def on_open(self):			
		self.acc.select(self.acc.children[1]) 

	def __init__(self, obj, **kwargs):
		super(ExercicioPopup, self).__init__(**kwargs)
		
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor						
		sql = "SELECT  id, unidade, modulo, exercicio, enunciado, imagem, pagina FROM tb_exercicios Where (exercicio = ?) ORDER BY id ASC"""
		self.cursor.execute(sql, (obj.text,))
		exercicio = self.cursor.fetchone()
		if exercicio is not None: 						
			self.txt_enunciado.text = str(exercicio[4])
			self.imagem = str(exercicio[5])		
		self.img_view = ImageView()		
		if self.imagem is not None or self.imagem != "":
			self.img_view.imagem = self.imagem
			self.image_layout.add_widget(self.img_view)
		else:			
			self.img_view.source = ""
			self.image_layout.remove_widget(self.img_view)
			
class SolucaoCompPopup(Popup): 
	pass 

class SolucaoM1Popup(Popup): 
	so_ex1_m1 = solucoes.so_ex1_m1 

class SolucaoM2Popup(Popup): 
	so_ex1_m2 = solucoes.so_ex1_m2 

class SolucaoM3Popup(Popup): 
	so_ex1_m3 = solucoes.so_ex1_m3

class SolucaoM4Popup(Popup): 
	so_ex1_m4 = solucoes.so_ex1_m4

Builder.load_file("gui/unidades.kv")

class Sc_Unidade1(Screen):
	campo_busca = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Sc_Unidade1, self).__init__(**kwargs)
		self.current_app = App.get_running_app()

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
			self.current_app.cursor.execute("SELECT  id, modulo, exercicio, enunciado, pagina FROM tb_exercicios ORDER BY id ASC")
			rows = self.current_app.cursor.fetchall()
			for conteudo in rows:
				if search:
					if text in conteudo[3].lower() or text.lower() in conteudo[3].lower():
						selecionar_exercicio(conteudo[2])
				else:
					selecionar_exercicio(conteudo[2])

	def inserir_unidades(self):
		sql = "INSERT INTO tb_unidades(id_unidade, id_modulo, tema) VALUES (1, 'Revisão do Ensino Fundamental', 'Álgebra')"
		self.current_app.cursor.execute(sql)
		self.current_app.conexao.commit()

	def inserir_modulos(self):
		sql = "INSERT INTO tb_modulos(id_modulo, titulo, paginas) VALUES (1, 'Revisão do Ensino Fundamental', 4)"
		self.current_app.cursor.execute(sql)
		self.current_app.conexao.commit()

	def inserir_exercicios(self):		
		lista = data.data_table

		for item in lista:			
			exercicios_data = (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
			self.current_app.cursor.execute("INSERT INTO tb_exercicios(id, unidade, modulo, imagem, exercicio, enunciado, pagina) VALUES (?, ?, ?, ?, ?, ?, ?)", exercicios_data)
			self.current_app.conexao.commit()
			
	def criar_tabelas(self):
		self.current_app.cursor.execute("PRAGMA foreign_keys = ON;")		
		sql_unidade = "CREATE TABLE IF NOT EXISTS tb_unidades(id_unidade integer PRIMARY KEY, id_modulo, tema text NOT NULL)"
		self.current_app.conexao.execute(sql_unidade)
		self.current_app.cursor.execute("SELECT * FROM tb_unidades")
		data = self.current_app.cursor.fetchall()
		if len(data)==0 or data==None:
			self.inserir_unidades()
		sql_modulo = "CREATE TABLE IF NOT EXISTS tb_modulos(id_modulo integer PRIMARY KEY, titulo text NOT NULL, paginas integer NOT NULL)"
		self.current_app.conexao.execute(sql_modulo)
		self.current_app.cursor.execute("SELECT * FROM tb_modulos")
		data = self.current_app.cursor.fetchall()
		if len(data)==0 or data==None:
			self.inserir_modulos()
		sql_exercicio = "CREATE TABLE IF NOT EXISTS tb_exercicios(id integer PRIMARY KEY, unidade integer KEY, modulo integer KEY, exercicio text, imagem text, enunciado text NOT NULL, pagina text NOT NULL, FOREIGN KEY(unidade) REFERENCES tb_unidades(id_unidade), FOREIGN KEY(modulo) REFERENCES tb_modulos(id_modulo))"		
		self.current_app.conexao.execute(sql_exercicio)
		self.current_app.cursor.execute("SELECT * FROM tb_exercicios")
		data = self.current_app.cursor.fetchall()
		if len(data)==0 or data==None:
			self.inserir_exercicios()

class Sc_Unidade2(Screen):
	pass

class Sc_Unidade3(Screen):
	pass

class Sc_Unidade4(Screen):
	pass

class Sc_Unidade5(Screen):
	pass

class Sc_Unidade6(Screen):
	pass

class Sc_Unidade7(Screen):
	pass

class Sc_Unidade8(Screen):
	pass