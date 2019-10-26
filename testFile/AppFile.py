import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout #Other types, look into them
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color

from kivy.uix.floatlayout import FloatLayout

class Touch(Widget):
	def __init__(self, **kwargs):
		super(Touch, self).__init__(**kwargs)
		
		with self.canvas:
			#RGBA: 0<=a<=1
			Color(1,0,0,0.5, mode= 'rgba')
			selfrect= Rectangle(pos=(0,0), size= (50,50))
			Color(1,0,0,0.5, mode= 'rgba')
			self.react= Rectangle(pos=(200,300), size=(100,50))
	#btn= ObjectProperty(None)
	
	def on_touch_down(self,touch):
		print("Mouse Down", touch)
		self.btn.opacity= 0.5
	def on_touch_move(self,touch):
		print("Mouse move", touch)
		
	def on_touch_up(self,touch):
		print("Mouse UP", touch)
		self.btn.opacity= 1
'''
class MyGrid(Widget):
	nameFromClass= ObjectProperty(None)
	emailFromClass= ObjectProperty(None)
	
	def button(self):
		print("Name:", self.nameFromClass.text, "email:", self.emailFromClass.text)
'''

'''#Old MyGrid class
class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs) #Call to MyGrid
		
		self.inside= GridLayout()
		self.inside.cols= 2
		
		self.cols= 1 # number of columns
		self.inside.add_widget(Label(text= "First Name: ")) #We can call this because its part of the GridLayout method class
		self.firstName= TextInput(multiline= False)
		self.inside.add_widget(self.firstName)
		
		self.inside.add_widget(Label(text= "Last Name: ")) #We can call this because its part of the GridLayout method class
		self.lastName= TextInput(multiline= False)
		self.inside.add_widget(self.lastName)
		
		self.inside.add_widget(Label(text= "Email: ")) #We can call this because its part of the GridLayout method class
		self.email= TextInput(multiline= False)
		self.inside.add_widget(self.email)
		
		
		self.add_widget(self.inside)
		
		self.submit= Button(text="Submit", font_size= 40)
		self.submit.bind(on_press= self.pressed)
		self.add_widget(self.submit)
	
	def pressed(self, instance):
		name= self.firstName.text
		last= self.lastName.text
		email= self.email.text
		
		print("Name: %s, Last Name: %s, Email: %s" % (name, last, email))
		self.firstName.text= ""
		self.lastName.text= ""
		self.email.text= ""
'''
	
#When defining kv files, must be the same as the class below but all lower case ad without the "App" syntax at the end.	
class MyApp(App): #Relates to the idea of inheritance.
	
	def build(self):
		#return MyGrid()
		#return Label(text="Hello World Title Label")
		#return FloatLayout()
		return Touch()
	
if __name__ == "__main__":
	MyApp().run()