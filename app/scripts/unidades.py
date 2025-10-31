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
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty

import scripts.data as data

class ImageView(BoxLayout):
	imagem = StringProperty("")
	def __init__(self, **kwargs):
		super(ImageView, self).__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor
		self.source = self.imagem		

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
	id_exercicio = NumericProperty(0)
	def __init__(self, **kwargs):
		super(SolucaoM1Button, self).__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor			

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
	buttons_layout = ObjectProperty(None)
	arquivo_imagem = StringProperty("")
	
	imagem = StringProperty("")
	img_view = ObjectProperty(None)
	txt_reposta_m1 = StringProperty("")
	def __init__(self, **kwargs):
		super(ExercicioPopup, self).__init__(**kwargs)
		self.current_app = App.get_running_app()
	'''
	def on_open(self): # on open apenas para popups
		self.acc.select(self.acc.children[1]) 
	'''
	def btn_pop1(self,  callback):		
		pop = SolucaoM1Popup()							
		pop.img.source = self.imagem
		

	def btn_pop2(self,  callback):		
		pop = SolucaoM2Popup()							
		pop.label_so1.text = self.txt_reposta_m1
				
	def selecionar_resposta(self, id_ex):
		return "exercício2"

	def __init__(self, obj, **kwargs):
		super(ExercicioPopup, self).__init__(**kwargs)		
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor						
		sql = "SELECT  id, unidade, modulo, exercicio, enunciado, imagem, pagina FROM tb_exercicios WHERE (exercicio = ?) ORDER BY id ASC"""
		self.cursor.execute(sql, (obj.text,))
		exercicio = self.cursor.fetchone()
		if exercicio is not None: 						
			self.txt_enunciado.text = str(exercicio[4])
			self.id_exercicio = exercicio[0]
			self.txt_reposta_m1 = self.selecionar_resposta(exercicio[3])						
			img = ImageView()
			img.imagem = exercicio[5]			
			self.image_layout.add_widget(img)
			sql = """SELECT  id, id_exercicio, imagem_resposta, calculadora_resposta, codigo_resposta,  software_resposta FROM tb_respostas WHERE (id = ?)"""
			self.cursor.execute(sql, (self.id_exercicio,))
			rows = self.current_app.cursor.fetchall()
			for conteudo in rows:
				if conteudo[2] is not None: 
					self.current_app.scm.get_screen("sc_unidade1").so_m1 = conteudo[2]
					self.current_app.scm.get_screen("sc_unidade1").so_m2 = conteudo[3]
					self.current_app.scm.get_screen("sc_unidade1").so_m3 = conteudo[4]
					self.current_app.scm.get_screen("sc_unidade1").so_m4 = conteudo[5]	
			s1 = SolucaoM1Button(text= "SM1")
			s1.bind(on_release=self.btn_pop1)	
			self.buttons_layout.add_widget(s1)					
			s1.id_exercicio = self.id_exercicio
				
class SolucaoCompPopup(Popup): 
	pass 

class SolucaoM1Popup(Popup): 
	so_ex1_m1 = StringProperty(None)
	imagem = StringProperty("")
	img = ObjectProperty(None)

class SolucaoM2Popup(Popup): 
	pass

class SolucaoM3Popup(Popup): 
	pass

class SolucaoM4Popup(Popup): 
	pass

Builder.load_file("gui/unidades.kv")


class Sc_ReFundamental(Screen):
	pass	
	campo_busca = ObjectProperty(None)
	ex_solucao = StringProperty("")
	so_m1 = StringProperty("")
	so_m2 = StringProperty("")
	so_m3 = StringProperty("")
	so_m4 = StringProperty("")

	def __init__(self, **kwargs):
		super(Sc_ReFundamental, self).__init__(**kwargs)
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

	def inserir_respostas(self):	
		lista1 = data.data_resp_01_10
		for item in lista1:			
			respostas_data = (item[0], item[1], item[2], item[3], item[4],item[5])
			self.current_app.cursor.execute("INSERT INTO tb_respostas(id, id_exercicio, imagem_resposta, calculadora_resposta, codigo_resposta,  software_resposta) VALUES (?, ?, ?, ?, ?, ?)", respostas_data,)
			self.current_app.conexao.commit()

		self.current_app.cursor.execute("SELECT id FROM tb_respostas")
		unidades1 = self.current_app.cursor.fetchall()
		
		
		if len(unidades1)==0 or unidades1==None:
			self.inserir_unidades()

		lista2 = data.data_resp_11_20
		for item in lista2:			
			respostas_data = (item[0], item[1], item[2], item[3], item[4],item[5])
			self.current_app.cursor.execute("INSERT INTO tb_respostas(id, id_exercicio, imagem_resposta, calculadora_resposta, codigo_resposta,  software_resposta) VALUES (?, ?, ?, ?, ?, ?)", respostas_data,)
			self.current_app.conexao.commit()

		self.current_app.cursor.execute("SELECT id FROM tb_respostas")
		unidades2 = self.current_app.cursor.fetchall()
		
		
		if len(unidades2)==0 or unidades2==None:
			self.inserir_unidades()
		
	def inserir_modulos(self):
		sql = "INSERT INTO tb_modulos(id_modulo, titulo, paginas) VALUES (1, 'Revisão do Ensino Fundamental', 4)"
		self.current_app.cursor.execute(sql)
		self.current_app.conexao.commit()

	def inserir_exercicios(self):		
		lista1 = data.data_table_01_10
		for item in lista1:			
			exercicios_data = (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
			self.current_app.cursor.execute("INSERT INTO tb_exercicios(id, unidade, modulo, imagem,exercicio, enunciado, pagina) VALUES (?, ?, ?, ?, ?, ?, ?)", exercicios_data)
			self.current_app.conexao.commit()

		lista2 = data.data_table_11_20
		for item in lista2:			
			exercicios_data = (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
			self.current_app.cursor.execute("INSERT INTO tb_exercicios(id, unidade, modulo, imagem,exercicio, enunciado, pagina) VALUES (?, ?, ?, ?, ?, ?, ?)", exercicios_data)
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

		sql_respostas = "CREATE TABLE IF NOT EXISTS tb_respostas(id integer PRIMARY KEY, id_exercicio integer KEY, imagem_resposta text, calculadora_resposta text, codigo_resposta text, software_resposta text, FOREIGN KEY(id_exercicio) REFERENCES tb_exercicios(id))"		
		self.current_app.conexao.execute(sql_respostas)
		self.current_app.cursor.execute("SELECT * FROM tb_respostas")
		data = self.current_app.cursor.fetchall()
		if len(data)==0 or data==None:
			self.inserir_respostas()		

class Sc_Unidade1(Screen):
	pass
	
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