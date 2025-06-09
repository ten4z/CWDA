from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import scripts.unidades as unidades
import sqlite3
import webbrowser
from kivy.lang.builder import Builder 
from kivy.core.window import Window

Builder.load_file("gui/principal.kv")

class Sc_Login(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.current_app = App.get_running_app()
		self.conexao = self.current_app.conexao
		self.cursor = self.current_app.cursor
		
class Sc_Home(Screen):
	pass

class Sc_Menu(Screen):
	pass

class Sc_Livros(Screen):
	pass

class Sc_Manager(ScreenManager):
	pass

class CWDA(App):
	conexao = sqlite3.connect("media_data.db")
	cursor = conexao.cursor()

	def abrir_link(self, link):
		webbrowser.open(link)

	def build(self):
		Window.size = (853, 480) #landscape
		self.scm = Sc_Manager()		
		return self.scm

if __name__ == "__main__":
	CWDA().run()