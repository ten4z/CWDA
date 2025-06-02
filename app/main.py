from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("gui/principal.kv")

class Sc_Login(Screen):
	pass

class Sc_Menu(Screen):
	pass

class Sc_Manager(ScreenManager):
	pass

class CWDA(App):
	def build(self):
		self.scm = Sc_Manager()
		return self.scm



if __name__ == "__main__":
	CWDA().run()