import pgzero , pygame , pgzrun , numpy


WIDTH = 1280		
HEIGHT = 720

alien = Actor('alien')
alien.pos = (100 ,100)

alien2 = Actor('alien2')
alien2.pos = (WIDTH/2,HEIGHT/2)

botao = Actor('button')
botao.pos = (WIDTH/2 , HEIGHT/2)
 
emJogo = False



def update():
	pass


def draw():
    screen.clear()
    screen.blit('tela_inicial', (0,0))
    botao.draw()
    if emJogo:
    	screen.clear()
    	screen.blit('espaco', (0,0))
    	alien.draw()
    	alien2.draw()

def on_mouse_down(pos):
	global emJogo
	if botao.collidepoint(pos):
		emJogo = True


def on_key_down(key):
	global alien
	if key == key.A:
		alien.x = alien.x-15
	elif key == keys.D:
		alien.x = alien.x+ 15
	elif key == key.W:
		alien.y = alien.y - 15
	elif key == key.S:
		alien.y = alien.y + 15

	if key == key.J:
		alien2.x = alien2.x-15
	elif key == keys.L:
		alien2.x = alien2.x+ 15
	elif key == key.I:
		alien2.y = alien2.y - 15 
	elif key == key.K:
		alien2.y = alien2.y + 15


pgzrun.go()