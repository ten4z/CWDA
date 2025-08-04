from kivy.app import App 
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import scripts.unidades as unidades
import sqlite3
import webbrowser
from kivy.uix.button import Button
from kivy.uix.popup import Popup
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
	acc_menu = ObjectProperty(None)
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def on_enter(self):
		self.acc_menu.select(self.acc_menu.children[1]) 

class Sc_Livros(Screen):
	pass

class Sc_Manager(ScreenManager):
	pass

class Avaliar_Btn(Button):
	def on_press(self):		
		popup = Avaliar_Popup()
		popup.open() 
		

class Avaliar_Popup(Popup):
	def link_avaliar(self):
		webbrowser.open("https://play.google.com/store/apps/details?id=com.zigasistemas.cwda")

class Sc_Politica(Screen):
	pass

class CWDA(App):
	conexao = sqlite3.connect("media_data.db")
	cursor = conexao.cursor()

	politiva_privacidade = """[b]Aplicação CWDA[/b]\n
Modo Interessante de Aprender Matemática[/b]\n
[b]https://play.google.com/store/apps/details?id=com.zigasistemas.cwda[/b]\n
\n
[b]• Respeito à privacidade[/b]\n
Esta aplicação tem publico alvo a consumidores finais que têm vários perfis de profissionais, respeitamos a todos os dados gerados, pessoais e confidenciais de nossos usuários, nós da Ziga Sistemas levamos a sério as consequências de mau uso ou irresponsabilidade, entendemos que não estamos infringindo ou quebrando as regras, respeitamos as individualidades de cada usuário, acompanhamos o conteúdo que nossos usuários geram, nós desejamos criar um ecossistema sustentável, agradável e de valor.\n
[b]• Liberdade de consumo de conteúdo[/b]\n
Nossos usuários podem desinstalar a aplicação quando bem entenderem, eles leem o conteúdo que escrevemos e interagem na aplicação, respeitamos a opinião deles, e entendemos quando eles não querem mais fazerem uso de nossos serviços por vontade própria, ou mudança de opinião.\n
[b]• Consciência da Ética, Moral e Cidadania[/b]\n
Aplicamos boas práticas no desenvolvimento da aplicação e fazemos constantes atualizações e melhorias com a finalidade de gerar inovação, estratégias de negócios ambas de maneira que respeitamos os anseios individuais e proporcionarmos boa manutenção de nossos produtos e serviços em todos os ciclos de vida.\n
[b]• Desenvolvimento Auto-Sustentável[/b]\n
Usamos anúncios em vários formatos com a finalidade de darmos manutenção na aplicação, estabelecermos um ecossistema sustentável e confortável para a Ziga Sistemas, parceiras e usuários. \n
[b][u]O que armazenamos para manutenção do aplicativo:[/u][/b]
[b]E-mail:[/b]O endereço do correio eletrônico de nossos usuários é de fundamental importância para nossa estratégia de marketing e de divulgação de novidades da aplicação bem como de podermos estabelecermos 
contatos e engajarmos nossos usuários da aplicação em torno dos produtos que desenvolvemos.\n
[b]Endereço Físico:[/b]Sabermos o endereço físico de nossos usuários é importante para , afim de que possamos firmarmos parcerias e mantermos um relacionamento saudável e duradouro em nossa plataforma.
[b][u]O que desejamos armazenar mas ainda não os fazemos:[/u][/b]\n
[b]Câmera: [/b]Desejamos conhecer as pessoas que usam nossos serviços, para melhorarmos nossos relacionamentos, estabelecer uma comunidade, 
e produzirmos produtos atrativos e de alta qualidade.\n
[b]Contatos: [/b]Sabermos o telefone pessoal de contato de nossos usuários é interessante para podermos firmarmos parcerias de negócios bem como também podermos estabelecer um contato direto com nossos usuários além de identificarmos os interesses destes ao usarem nossos produtos e serviços.\n
[b]Localização: [/b]Atrativo para sabermos o perfil do usuário da aplicação, direcionarmos conteúdo, produtos e serviços, e identificarmos abrangência e alcance da aplicação em determinados nichos e regiões.\n
[b]Microfone: [/b]Nossa aplicação faz uso de tecnologia de identificação do texto para fala e conversão de fala para texto, portanto fazemos uso deste recurso para agregarmos funcionalidade na aplicação bem como melhorarmos nossa comunicação e melhoria de nossos produtos e serviços.\n
[b]Missão, Visão e Valores da Ziga Sistemas[/b]\n
[b]Missão: [/b]Entregar soluções estratégias de negócios baseadas em bases de dados.\n
[b]Visão: [/b]A excelência é desejável, trata-se de um costume praticado com constante aperfeiçoamento.\n
[b]Valores: [/b]Mentoria, Gestão, Comunicação, Transparência, Sustentabilidade.\n
[b]Website pessoal[/b]
http://www.josielsoares.com\n
[b]Link auto contido deste documento:[/b]\n http://www.josielsoares.com/documentos/politica-de-privacidade-cwda.html \n
[b]Edição dia 14 de julho de 2025 | Josiel Soares. Gestor da Ziga Sistemas[/b]\n"""				
	

	def abrir_link(self, link):
		webbrowser.open(link)

	def build(self):
		Window.size = (853, 480) #landscape
		self.scm = Sc_Manager()		
		return self.scm

if __name__ == "__main__":
	CWDA().run()