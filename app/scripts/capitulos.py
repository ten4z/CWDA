from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file("gui/principal.kv")

class Sc_Capitulos(Screen):
	def leitura_c1(self):
		print("capitulo 1 página 1")

def leitura_cap01():
	Sc_Capitulos().leitura_c1()

