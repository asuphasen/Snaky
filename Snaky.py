from tkinter import *
import random
import time
import sys

root = Tk()
root.title("The Predator")

W = 800
H = 600
Body_size = 20

################################################################
class Intro:
	def __init__(self):
		self.root = root
		self.f_menu = Frame(self.root)
		self.f_menu.pack()
		self.m_c = Canvas(self.f_menu, width = 800, height = 600, bg = "GreenYellow")
		self.m_c.pack()
		self.logo = self.m_c.create_text(400,150,text="SNAKY", font = ("fixedsys",120))
		self.logo2 = self.m_c.create_text(400,250,text="I NEED AN APPLE", font = ("fixedsys",40))
		self.logo2 = self.m_c.create_text(400,500,text="Game for fun ©", font = ("fixedsys",20))
		self.bt_Goto = Button(self.m_c,text="START GAME",font=("fixedsys",30), command = self.runapp)
		self.bt_Goto.place(x=80, y=350)
		self.bt_quit = Button(self.m_c,text=" QUIT GAME ",font=("fixedsys",30), command = quit)
		self.bt_quit.place(x=430, y=350)

	def runapp(self):
	 	self.f_menu.destroy()
	 	self.game = Snaky()
#################################################################
class Snaky:
	def __init__(self):
		self.canvas = Canvas(root, width = W, height = H, bg = "GreenYellow")
		self.canvas.pack()
		self.x = 0
		self.y = 0
		self.speedx = 20
		self.speedy = 0
		self.speed = 20
		self.score = 0
		self.s = 150
		self.gameover = False
		self.canvas.bind('<Key>', self.direction)
		self.canvas.focus_set()
		self.Food()
		self.Snake()
		self.Wall()
		self.draw()

	# 
	def Snake(self):
		self.snake = self.canvas.create_rectangle(self.x, self.y, self.x+Body_size, self.y+Body_size, width= 0, fill="#1C1C1C")

	def Wall(self):
		self.wall_lx = 80
		self.wall_rx = 200
		self.wall_uy = 80
		self.wall_dy = 120
		self.wall = self.canvas.create_rectangle(self.wall_lx, self.wall_uy, self.wall_rx, self.wall_dy,width = 0, fill="LightCyan")
		self.wall2_lx = 80
		self.wall2_rx = 120
		self.wall2_uy = 120
		self.wall2_dy = 200
		self.wall2 = self.canvas.create_rectangle(self.wall2_lx, self.wall2_uy, self.wall2_rx, self.wall2_dy,width = 0, fill="LightCyan")
		self.wall3_lx = 600
		self.wall3_rx = 720
		self.wall3_uy = 80
		self.wall3_dy = 120
		self.wall3 = self.canvas.create_rectangle(self.wall3_lx, self.wall3_uy, self.wall3_rx, self.wall3_dy,width = 0, fill="LightCyan")
		self.wall4_lx = 680
		self.wall4_rx = 720
		self.wall4_uy = 120
		self.wall4_dy = 200
		self.wall4 = self.canvas.create_rectangle(self.wall4_lx, self.wall4_uy, self.wall4_rx, self.wall4_dy,width = 0, fill="LightCyan")
		self.wall5_lx = 80
		self.wall5_rx = 120
		self.wall5_uy = 400
		self.wall5_dy = 520
		self.wall5 = self.canvas.create_rectangle(self.wall5_lx, self.wall5_uy, self.wall5_rx, self.wall5_dy,width = 0, fill="LightCyan")
		self.wall6_lx = 80
		self.wall6_rx = 200
		self.wall6_uy = 480
		self.wall6_dy = 520
		self.wall6 = self.canvas.create_rectangle(self.wall6_lx, self.wall6_uy, self.wall6_rx, self.wall6_dy,width = 0, fill="LightCyan")
		self.wall7_lx = 680
		self.wall7_rx = 720
		self.wall7_uy = 400
		self.wall7_dy = 480
		self.wall7 = self.canvas.create_rectangle(self.wall7_lx, self.wall7_uy, self.wall7_rx, self.wall7_dy,width = 0, fill="LightCyan")
		self.wall8_lx = 600
		self.wall8_rx = 720
		self.wall8_uy = 480
		self.wall8_dy = 520
		self.wall8 = self.canvas.create_rectangle(self.wall8_lx, self.wall8_uy, self.wall8_rx, self.wall8_dy,width = 0, fill="LightCyan")
		self.wall9_lx = 180
		self.wall9_rx = 300
		self.wall9_uy = 220
		self.wall9_dy = 240
		self.wall9 = self.canvas.create_rectangle(self.wall9_lx, self.wall9_uy, self.wall9_rx, self.wall9_dy,width = 0, fill="LightCyan")
		self.wall10_lx = 180
		self.wall10_rx = 300
		self.wall10_uy = 360
		self.wall10_dy = 380
		self.wall10 = self.canvas.create_rectangle(self.wall10_lx, self.wall10_uy, self.wall10_rx, self.wall10_dy,width = 0, fill="LightCyan")
		self.wall11_lx = 240
		self.wall11_rx = 300
		self.wall11_uy = 300
		self.wall11_dy = 320
		self.wall11 = self.canvas.create_rectangle(self.wall11_lx, self.wall11_uy, self.wall11_rx, self.wall11_dy,width = 0, fill="LightCyan")
		self.wall12_lx = 180
		self.wall12_rx = 200
		self.wall12_uy = 240
		self.wall12_dy = 280
		self.wall12 = self.canvas.create_rectangle(self.wall12_lx, self.wall12_uy, self.wall12_rx, self.wall12_dy,width = 0, fill="LightCyan")
		self.wall13_lx = 280
		self.wall13_rx = 300
		self.wall13_uy = 320
		self.wall13_dy = 360
		self.wall13 = self.canvas.create_rectangle(self.wall13_lx, self.wall13_uy, self.wall13_rx, self.wall13_dy,width = 0, fill="LightCyan")
		self.wall14_lx = 360
		self.wall14_rx = 480
		self.wall14_uy = 220
		self.wall14_dy = 240
		self.wall14 = self.canvas.create_rectangle(self.wall14_lx, self.wall14_uy, self.wall14_rx, self.wall14_dy,width = 0, fill="LightCyan")
		self.wall15_lx = 360
		self.wall15_rx = 480
		self.wall15_uy = 360
		self.wall15_dy = 380
		self.wall15 = self.canvas.create_rectangle(self.wall15_lx, self.wall15_uy, self.wall15_rx, self.wall15_dy,width = 0, fill="LightCyan")
		self.wall16_lx = 360
		self.wall16_rx = 380
		self.wall16_uy = 240
		self.wall16_dy = 280
		self.wall16 = self.canvas.create_rectangle(self.wall16_lx, self.wall16_uy, self.wall16_rx, self.wall16_dy,width = 0, fill="LightCyan")
		self.wall17_lx = 460
		self.wall17_rx = 480
		self.wall17_uy = 240
		self.wall17_dy = 280
		self.wall17 = self.canvas.create_rectangle(self.wall17_lx, self.wall17_uy, self.wall17_rx, self.wall17_dy,width = 0, fill="LightCyan")
		self.wall18_lx = 520
		self.wall18_rx = 620
		self.wall18_uy = 220
		self.wall18_dy = 240
		self.wall18 = self.canvas.create_rectangle(self.wall18_lx, self.wall18_uy, self.wall18_rx, self.wall18_dy,width = 0, fill="LightCyan")
		self.wall19_lx = 560
		self.wall19_rx = 580
		self.wall19_uy = 240
		self.wall19_dy = 280
		self.wall19 = self.canvas.create_rectangle(self.wall19_lx, self.wall19_uy, self.wall19_rx, self.wall19_dy,width = 0, fill="LightCyan")
		self.wall20_lx = 180
		self.wall20_rx = 200
		self.wall20_uy = 320
		self.wall20_dy = 360
		self.wall20 = self.canvas.create_rectangle(self.wall20_lx, self.wall20_uy, self.wall20_rx, self.wall20_dy,width = 0, fill="LightCyan")
		self.wall21_lx = 360
		self.wall21_rx = 380
		self.wall21_uy = 320
		self.wall21_dy = 360
		self.wall21 = self.canvas.create_rectangle(self.wall21_lx, self.wall21_uy, self.wall21_rx, self.wall21_dy,width = 0, fill="LightCyan")
		self.wall22_lx = 460
		self.wall22_rx = 480
		self.wall22_uy = 320
		self.wall22_dy = 360
		self.wall22 = self.canvas.create_rectangle(self.wall22_lx, self.wall22_uy, self.wall22_rx, self.wall22_dy,width = 0, fill="LightCyan")
		self.wall23_lx = 560
		self.wall23_rx = 580
		self.wall23_uy = 320
		self.wall23_dy = 380
		self.wall23 = self.canvas.create_rectangle(self.wall23_lx, self.wall23_uy, self.wall23_rx, self.wall23_dy,width = 0, fill="LightCyan")


	def Food(self):
		self.px = Body_size*random.randint(1, (W-Body_size)/Body_size)
		self.py = Body_size*random.randint(1, (H-Body_size)/Body_size)
		self.food = self.canvas.create_oval(self.px, self.py, self.px+Body_size, self.py+Body_size, fill="Crimson")

	def direction(self, event):
		if event.keycode == 37:
			self.speedx = -self.speed
			self.speedy = 0
		elif event.keycode == 38:
			self.speedy = -self.speed
			self.speedx = 0
		elif event.keycode == 39:
			self.speedx = self.speed
			self.speedy = 0
		elif event.keycode == 40:
			self.speedy = self.speed
			self.speedx = 0

	def eat(self):
		if self.x == self.px and self.y == self.py:
			self.canvas.delete(self.food)
			self.Food()
			self.score = self.score + 1000
			self.s -= 10

	def crash(self):
		if self.x < 0 or self.x > W-Body_size or self.y < 0 or self.y > H-Body_size :
			self.gameover = True
			self.endgame()
		elif self.wall_lx - Body_size < self.x < self.wall_rx and self.wall_uy - Body_size < self.y < self.wall_dy or\
			self.wall2_lx - Body_size < self.x < self.wall2_rx and self.wall2_uy - Body_size < self.y < self.wall2_dy or\
			self.wall3_lx - Body_size < self.x < self.wall3_rx and self.wall3_uy - Body_size < self.y < self.wall3_dy or\
			self.wall4_lx - Body_size < self.x < self.wall4_rx and self.wall4_uy - Body_size < self.y < self.wall4_dy or\
			self.wall5_lx - Body_size < self.x < self.wall5_rx and self.wall5_uy - Body_size < self.y < self.wall5_dy or\
			self.wall6_lx - Body_size < self.x < self.wall6_rx and self.wall6_uy - Body_size < self.y < self.wall6_dy or\
			self.wall7_lx - Body_size < self.x < self.wall7_rx and self.wall7_uy - Body_size < self.y < self.wall7_dy or\
			self.wall8_lx - Body_size < self.x < self.wall8_rx and self.wall8_uy - Body_size < self.y < self.wall8_dy or\
			self.wall9_lx - Body_size < self.x < self.wall9_rx and self.wall9_uy - Body_size < self.y < self.wall9_dy or\
			self.wall10_lx - Body_size < self.x < self.wall10_rx and self.wall10_uy - Body_size < self.y < self.wall10_dy or\
			self.wall11_lx - Body_size < self.x < self.wall11_rx and self.wall11_uy - Body_size < self.y < self.wall11_dy or\
			self.wall12_lx - Body_size < self.x < self.wall12_rx and self.wall12_uy - Body_size < self.y < self.wall12_dy or\
			self.wall13_lx - Body_size < self.x < self.wall13_rx and self.wall13_uy - Body_size < self.y < self.wall13_dy or\
			self.wall14_lx - Body_size < self.x < self.wall14_rx and self.wall14_uy - Body_size < self.y < self.wall14_dy or\
			self.wall15_lx - Body_size < self.x < self.wall15_rx and self.wall15_uy - Body_size < self.y < self.wall15_dy or\
			self.wall16_lx - Body_size < self.x < self.wall16_rx and self.wall16_uy - Body_size < self.y < self.wall16_dy or\
			self.wall17_lx - Body_size < self.x < self.wall17_rx and self.wall17_uy - Body_size < self.y < self.wall17_dy or\
			self.wall18_lx - Body_size < self.x < self.wall18_rx and self.wall18_uy - Body_size < self.y < self.wall18_dy or\
			self.wall19_lx - Body_size < self.x < self.wall19_rx and self.wall19_uy - Body_size < self.y < self.wall19_dy or\
			self.wall20_lx - Body_size < self.x < self.wall20_rx and self.wall20_uy - Body_size < self.y < self.wall20_dy or\
			self.wall21_lx - Body_size < self.x < self.wall21_rx and self.wall21_uy - Body_size < self.y < self.wall21_dy or\
			self.wall22_lx - Body_size < self.x < self.wall22_rx and self.wall22_uy - Body_size < self.y < self.wall22_dy or\
			self.wall23_lx - Body_size < self.x < self.wall23_rx and self.wall23_uy - Body_size < self.y < self.wall23_dy :
			self.gameover = True
			self.endgame()

	def endgame(self):
		self.canvas.delete(ALL)
		self.canvas.create_text(W/2, 200, text="GAME OVER", font="fixedsys 100", fill="#1C1C1C")
		self.bt_Goto = Button(self.canvas,text="TRY AGIAN",font=("fixedsys",30), command = self.endgame2)
		self.bt_Goto.place(x=80, y=350)
		self.bt_quit = Button(self.canvas,text="   QUIT   ",font=("fixedsys",30), command = quit)
		self.bt_quit.place(x=430, y=350)
		self.canvas.create_text(W/2, 300, text=("You Score : "+str(self.score)), font="fixedsys 20", fill="#1C1C1C")
		self.end = The_end()

	def update(self):
		self.x = self.x + self.speedx
		self.y = self.y + self.speedy

	def draw(self):
		if self.gameover == False:
			self.Wall()
			self.update()
			self.eat()
			self.crash()
			self.canvas.move(self.snake, self.speedx, self.speedy)
			self.canvas.after(self.s, self.draw)

	def endgame2(self):
		self.canvas.destroy()
		self.re = Snaky()
################################################################
# class The_end:
# 	def __init__(self):
# 		self.root = root
# 		self.end_menu = Frame(self.root)
# 		self.end_menu.pack()
# 		self.c = Canvas(self.end_menu, width = 800, height = 600, bg = "GreenYellow")
# 		self.c.pack()
# 		self.c.create_text(W/2, 200, text="GAME OVER", font="fixedsys 100", fill="#1C1C1C")
# 		self.bt_Goto = Button(self.c,text="TRY AGIAN",font=("fixedsys",30), command = self.endgame2)
# 		self.bt_Goto.place(x=80, y=350)
# 		self.bt_quit = Button(self.c,text="   QUIT   ",font=("fixedsys",30), command = quit)
# 		self.bt_quit.place(x=430, y=350)
# 		self.c.create_text(W/2, 400, text="score : "+str(self.Score), font="fixedsys 50", fill="#1C1C1C")

# 	def endgame2(self):
# 		self.end_menu.destroy()
# 		self.game = Snaky()
################################################################
Intro()
root.mainloop()
