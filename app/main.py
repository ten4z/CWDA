from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import scripts.unidades as unidades
import sqlite3
from kivy.lang.builder import Builder 



Builder.load_file("gui/principal.kv")



class Sc_Login(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor

class Sc_Menu(Screen):
	pass

class Sc_Livros(Screen):
	pass

class Sc_Manager(ScreenManager):
	pass

class CWDA(App):
	conexao = sqlite3.connect("media_data.db")
	cursor = conexao.cursor()

	def build(self):
		self.scm = Sc_Manager()		
		return self.scm

if __name__ == "__main__":
	CWDA().run()