from tkinter import Tk, Frame, Canvas, Button, Label
import tkinter.font

class App(Tk):
	color = None
	longeur_trait = 20
	c_wd = 0
	c_he = 0
	tour = 0
	win = False
	winner = None
	combos = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	
	def __init__(self):
		super(App,self).__init__()
		#variables ---
		
		
		self.police = tkinter.font.Font(family='Arial',size=60)
		self.police2 = tkinter.font.Font(family='Arial',size=40)
		self.player = 1 #player 1 start by default
		self.dict_cases = {}
		
		#init fonctions -------
		self.title('Morpion')
		self.columnconfigure(0,weight=1)
		self.rowconfigure(1,weight=1)
		self.frame1 = Frame(self,bd=10,width=10)
		self.frame1.grid(sticky='ew',)
		self.label1 = Label(self.frame1,text ='')
		self.label1.pack(side='left')
		self.label2 = Label(self.frame1,text='')
		self.label2.pack(side='left')
		self.canvas = Canvas(self,bg='white')
		self.canvas.grid(row=1,padx=15,pady=15,sticky='nsew')
		self.canvas.bind('<Button-1>',self.Callback)
		self.frame = Frame(self,bd=10,width=10)#,bg='grey')
		self.frame.grid(row=2,sticky='ew')
		self.button = Button(self.frame,text='Start',height=1,command=self.create)
		self.button.pack(side='left',expand = 'true',fill='x') 
		self.quitter = Button(self.frame,text='Quitter',height=1,command = self.quit)
		self.quitter.pack(side='right')
		self.canvas.update()
		self.startup_Message()
		
	def startup_Message(self):
		self.get_canvas_info()
		self.canvas.create_text(self.c_wd/2,self.c_he/2,justify='center',text='Morpion\nPlayer1 start with : X')
		
	def is_empty(self,col,r):
		test = {(1,1):1,(2,1):2,(3,1):3,(1,2):4,(2,2):5,(3,2):6,(1,3):7,(2,3):8,(3,3):9}
		if len(self.dict_cases) > 0:
			value = self.dict_cases[test[col,r]]
			if value == None:
				self.dict_cases[test[col,r]] = self.player
				return True
			else:
				return False
		else:
			return None
		
	def get_canvas_info(self):
		self.c_wd = self.canvas.winfo_width()
		self.c_he = self.canvas.winfo_height()
		
	def create(self):
		self.color = 'black'
		self.button.config(text='Restart')
		self.player = 1
		self.win = False
		self.tour = 0
		self.dict_cases = {i: None for i in range(1,10)}
		self.label1.config(text="Player's turn : Player")
		self.label2.config(text=str(self.player))
		
		self.canvas.delete('all')
		self.get_canvas_info() 
		#update cabvas width and height to 		actual screen configuration
		wid = self.c_wd #local canvas width
		hei = self.c_he #local canvas height
		border = self.longeur_trait/2
		spacing_h = wid/3
		spacing_v = hei/3
		
		self.canvas.create_rectangle(spacing_h-border,0,spacing_h+border,hei,fill='black')
		self.canvas.create_rectangle(2*spacing_h-border,0,2*spacing_h+border,hei,fill='black')
		self.canvas.create_rectangle(0,spacing_v-border,wid,spacing_v+border,fill='black')
		self.canvas.create_rectangle(0,2*spacing_v-border,wid,2*spacing_v+border,fill='black')
		
		self.update()
		
	def checkRowColumn(self,x,y):
		row,column = 0,0
		_width = self.canvas.winfo_width()/3
		_height = self.canvas.winfo_height()/3
		if x <= _width:
			column = _width/2
			col = 1
		elif x <= 2*_width:
			column = _width+(_width/2)
			col = 2
		elif x <= 3*_width:
			column = 2*_width+(_width/2)
			col = 3
		
		if y <= _height:
			row = _height/2
			r = 1
		elif y <= 2*_height:
			row = _height+(_height/2)
			r = 2
		elif y <=3* _height:
			row = 2*_height+(_height/2)
			r = 3
			
		return column,row,col,r
		
	def get_player(self):
		current = self.player
		if current == 1:
			self.player = 2
			return 'X'
		else:
			self.player = 1
			return 'O'
	
	def check_equality(self,na,nb,nc):
		if self.dict_cases[na] == self.dict_cases[nb] == self.dict_cases[nc] == 1:
			self.winner = 'Player 1'
			self.color = 'blue'
			return True
		elif self.dict_cases[na] == self.dict_cases[nb] == self.dict_cases[nc] == 2:
			self.winner = 'Player 2'
			self.color = 'red'
			print(self.winner)
			return True
		else:
			return False
	
	def make_grey(self):
		canvas_item = self.canvas.find_all()
		for i in canvas_item:
			self.canvas.itemconfig(i,fill='lightgrey')
	def check_win(self):
		for i in self.combos:
			if self.check_equality(i[0],i[1],i[2]):
				self.win = True
				self.make_grey()
				self.canvas.create_text(self.c_wd/2,self.c_he/2,text='Winner\n'+self.winner,font = self.police2,fill=self.color)
		
	def Callback(self,event):
		x,y,col,r = self.checkRowColumn(event.x,event.y)
		value = self.is_empty(col,r)
		if value  and not self.win:
			self.canvas.create_text(x,y,text=self.get_player(),font=self.police)
			self.label2.config(text=str(self.player))
			self.tour+=1
			if self.tour >= 5:
				self.check_win()
			if self.tour==9 and not self.win:
				self.winner = 'Draw'
				self.make_grey()
				self.canvas.create_text(self.c_wd/2,self.c_he/2,text=self.winner,font = self.police2,fill=self.color)
				
		 
		
		
		 
		
if __name__ == '__main__':
	a = App()
	a.mainloop()
		
	
