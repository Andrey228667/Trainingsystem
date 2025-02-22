from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
	i = 0
	
	def build(self):
		bl=BoxLayout(orientation='vertical')
		self.lbl1=Label(text =str(self.i),font_size=150)
		btn1=Button(text="+1",size_hint=(1,.1),pos_hint={'center_x':.5,'top_y':1})
		btn2=Button(text = "+10",size_hint=(1,.1))
		btn3=Button(text = "Reset",size_hint=(1,.1))
		btn4=Button(text="-10",size_hint=(1,.1))
		btn5=Button(text="-1",size_hint=(1,.1))
		btn1.bind(on_press=self.btn1)
		btn2.bind(on_press=self.btn2)
		btn3.bind(on_press=self.btn3)
		btn4.bind(on_press=self.btn4)
		btn5.bind(on_press=self.btn5)
		bl.add_widget(self.lbl1)
		bl.add_widget(btn5)
		bl.add_widget(btn4)
		bl.add_widget(btn1)
		bl.add_widget(btn2)
		bl.add_widget(btn3)
		return bl
	
	def btn1(self,instance):
		self.i+=1
		self.lbl1.text=str(self.i  )
	def btn2(self,instance):
		self.i+=10
		self.lbl1.text=str(self.i  )
	def btn3(self,instance):
		self.i=0
		self.lbl1.text=str(self.i )
	def btn4(self,instance):
		self.i-=10
		if self.i <=0:
			self.i=0
		self.lbl1.text=str(self.i  )
	def btn5(self,instance):
		self.i-=1
		if self.i <=0:
			self.i=0
		self.lbl1.text=str(self.i  )
	
		
		
if __name__=="__main__":
	MyApp().run()
	
	