import pygame


class Rede:
	cor = (255, 255, 255)
	tamanho = (15, 15)
	
	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)
		self.tamanho = [(440, 0),(440, 10),(440, 20),(440, 30),(440, 40),(440, 50),
		                (440, 60),(440, 70),(440, 80),(440, 90),(440, 100),(440, 110),
		                (440, 120),(440, 130),(440, 140),(440, 150),(440, 160),(440, 170),
		                (440, 180),(440, 190),(440, 200),(440, 210),(440, 220),(440, 230),
		                (440, 240),(440, 250),(440, 260),(440, 270),(440, 280),(440, 290),
		                (440, 300),(440, 310),(440, 320),(440, 330),(440, 340),(440, 350),
		                (440, 360),(440, 370),(440, 380),(440, 390),(440, 400),(440, 410),
		                (440, 420),(440, 430),(440, 440),(440, 450),(440, 460),(440, 470),
		                (440, 480),(440, 490)]
			
		
	def tela(self, tela):
		for posicao in self.tamanho:
			tela.blit(self.textura, posicao)
	


class Bolinha:
	cor = (255, 0, 0)
	tamanho = (10, 10)
	velocidade = 10

	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)

		self.corpo = [(0, 0)]
		self.direcao = 'direita'
		self.pontos = 0

	def tela(self, tela):
		for posicao in self.corpo:
			tela.blit(self.textura, posicao)
	
	def andar(self):
		
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		
		if self.direcao == 'direita':
			self.corpo.insert(0, (x + self.velocidade, y))
			
		elif self.direcao == 'esquerda':
			self.corpo.insert(0, (x - self.velocidade, y))
			
		elif self.direcao == 'cima':
			self.corpo.insert(0, (x, y - self.velocidade))
			
		elif self.direcao == 'baixo':
			self.corpo.insert(0, (x, y + self.velocidade))
			
		self.corpo.pop(-1)
		
	
	

class Jogador1:
	cor = (255, 255, 255)
	tamanho = (10, 10)
	velocidade = 10

	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)

		self.corpo = [(890, 100),(890, 110),(890, 120),(890, 130),(890, 140),(890, 150),(890, 160)]
		self.direcao = 'cima'

	def tela(self, tela):
		for posicao in self.corpo:
			tela.blit(self.textura, posicao)

	def andar(self):
		
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		
		if self.direcao == 'direita':
			self.corpo.insert(0, (x + self.velocidade, y))
			
		elif self.direcao == 'esquerda':
			self.corpo.insert(0, (x - self.velocidade, y))
			
		elif self.direcao == 'cima':
			self.corpo.insert(0, (x, y - self.velocidade))
			
		elif self.direcao == 'baixo':
			self.corpo.insert(0, (x, y + self.velocidade))
			
		self.corpo.pop(-1)
		
	def cima(self):
		if self.direcao != 'cima':
			self.direcao = 'cima'	
		
	def baixo(self):
		if self.direcao != 'baixo':
			self.direcao = 'baixo'	

class Jogador2:
	cor = (255, 255, 255)
	tamanho = (10, 10)
	velocidade = 10

	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)

		self.corpo = [(0, 100),(0, 110),(0, 120),(0, 130),(0, 140),(0, 150),(0, 160)]
		self.direcao = 'cima'

	def tela(self, tela):
		for posicao in self.corpo:
			tela.blit(self.textura, posicao)

	def andar(self):
		
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		
		if self.direcao == 'direita':
			self.corpo.insert(0, (x + self.velocidade, y))
			
		elif self.direcao == 'esquerda':
			self.corpo.insert(0, (x - self.velocidade, y))
			
		elif self.direcao == 'cima':
			self.corpo.insert(0, (x, y - self.velocidade))
			
		elif self.direcao == 'baixo':
			self.corpo.insert(0, (x, y + self.velocidade))
			
		self.corpo.pop(-1)
	
	def colisao(self):
		corpo = self.corpo[0]
		x = corpo[0]
		y = corpo[1]
		
		if  x < 0 or y < 0 or x > 490 or y > 490:
			if self.direcao != 'cima':
				self.direcao = 'cima'	
			
			if self.direcao != 'baixo':
				self.direcao = 'baixo'	
			
	
		
	
if __name__ == "__main__":
	#inicia o pygame
	pygame.init()

	#resolução da tela
	resolucao = (900,500)
	tela = pygame.display.set_mode(resolucao)

	#nome do jogo na tela
	pygame.display.set_caption('Ping-Pong')

	#definir fps
	clock = pygame.time.Clock()

	#cor da tela
	cor_tela =(0, 0, 0)
	
	bolinha = Bolinha()
	rede = Rede()
	jogador1 = Jogador1()
	jogador2 = Jogador2()

while True:
	clock.tick(20)
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
			
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					jogador1.cima()
				elif event.key == pygame.K_DOWN:
					jogador1.baixo()
	
	if jogador2.colisao():
		jogador2 = Jogador2()

	jogador2.andar()			
	bolinha.andar()	
	jogador1.andar()
	
	
	tela.fill(cor_tela)
		
	bolinha.tela(tela)
	
	rede.tela(tela)
	
	jogador1.tela(tela)
	jogador2.tela(tela)
	
	
	pygame.display.update()
