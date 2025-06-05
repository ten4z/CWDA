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
from kivy.properties import ObjectProperty, StringProperty, ListProperty


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
				 RecycleGridLayout):
	pass
class SelectableButton(RecycleDataViewBehavior, Button):
	def on_press(self):
		
		popup = ExercícioPopup(self)
		popup.open() 

class ExercícioPopup(Popup): 
	id_exercicio = ObjectProperty(None)
	txt_exercicio = ObjectProperty(None)
	txt_enunciado = ObjectProperty(None)	
	def __init__(self, obj, **kwargs):
		super(ExercícioPopup, self).__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor
		

		sql = "SELECT  id, unidade, modulo, exercicio, enunciado, pagina FROM tb_exercicios Where (exercicio = ?) ORDER BY id ASC"""
		self.cursor.execute(sql, (obj.text,))
		exercicio = self.cursor.fetchone()
		if exercicio is not None: 			
			self.txt_exercicio.text = "Ler Solução Ex. " + str(exercicio[0])			
			self.txt_enunciado.text = str(exercicio[4])


Builder.load_file("gui/unidades.kv")

class Sc_Unidade1(Screen):
	campo_busca = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Sc_Unidade1, self).__init__(**kwargs)
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
			self.current_app.cursor.execute("SELECT  id, modulo, exercicio, enunciado, pagina FROM tb_exercicios ORDER BY id ASC")
			rows = self.current_app.cursor.fetchall()
			for conteudo in rows:
				if search:
					if text.lower() in conteudo[2].lower() or text.lower() in conteudo[2].lower():
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
		lista = [[1, 1, 1, 'imagem 1','Exercício 1', '1. O número 0,666... é igual a uma certa fração f. Essa fração está representada na reta numérica abaixo: O ponto que representa a fração é: \na) A. b) B. c) C. d) D.',10],[2, 1,1, 'Nenhuma', 'Exercício 2', '2. Numa classe de 8ª série com 40 alunos, foram arrecadados R$ 2.749,60 para as comemorações da formatura. As despesas foram as seguintes: R$ 754,15 para o conjunto musical, R$ 285,35 para os enfeites da igreja e do salão de baile e R$ 880,50 para a excursão. A sobra foi repartida igualmente entre os alunos dessa classe. Quanto cada aluno recebeu? \na) R$ 116,74 b) R$ 82,96 c) R$ 48,00 d)R$ 20,74 ', 10],[3, 1, 1, 'imagem','Exercício 3.','3. A prefeitura de uma determinada cidade sorteou 120 apartamentos em um sistema de casas populares. Três grupos inscreveram-se nesse programa: grupo A de funcionários da prefeitura; grupo B de moradores com renda mensal abaixo de 2 salários mínimos; grupo c de moradores com renda mensal de 2 a 3 salários mínimos. Desse total, 1/4 dos apartamentos foram destinado para o grupo A e 1/3 para o grupo B. Sabendo que o restante era para o grupo C, qua a fração correspondente a ele: \n a) 2/7 b)5/7 c) 5/12 d) 7/12', 10],[4,1, 1, 'imagem','Exercício 4','4. Calculando se √30, obtém se 5,4772255..., número que tem representação decimal finita, mas não é dízima periódica. Conclui-se então que √30 é um número: \n a) natural. b) inteiro. c) racional. d) irracional. ', 11],[5, 1 ,1,'imagem', 'Exercício 5', '5. Simplificando a expressão √(62 + √(1 + √9)), obtemos: \na) 6. b) 8. c) 16. d) √40.',12]]

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


def leitura_cap01():
	Sc_Unidade1().leitura_c1()
	Sc_Unidade1().exercicios_c1()
	Sc_Unidade1().solucao_exercicio("ex1", "m5")

