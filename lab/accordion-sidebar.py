from kivy.app import App 
from kivy.lang.builder import Builder 

kv = Builder.load_string("""
BoxLayout:
	orientation: "horizontal"
	Accordion: 
		id: acc
		size_hint:0.3, 1 
		AccordionItem:
			Button: 
				text: "menu"
		AccordionItem:
			BoxLayout:
				orientation: "vertical"
				Button:
					text: "hello"
				Button: 
					text: "button"
				Button: 
					text: "other button"
					on_release:
						acc.collapse = False
		


	BoxLayout:
		orientation: "horizontal"
		Button:
			text: "Other"
		Button:
			text: "And Other"
		Button:
			text: "Other more"
""")
class MyApp(App):
	def build(self):
		return kv 

if __name__ == "__main__":
	MyApp().run()