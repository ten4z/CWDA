from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("gui/capitulos.kv")

class Sc_Capitulos(Screen):
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


def leitura_cap01():
	Sc_Capitulos().leitura_c1()
	Sc_Capitulos().exercicios_c1()
	Sc_Capitulos().solucao_exercicio("ex1", "m5")

