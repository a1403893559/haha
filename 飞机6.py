import random
import pygame
from feiji2 import *




class PlaneGame(object):
	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		self.enemy = Enemy()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,5000)
#		pygame.time.set_timer(ENEMY,500)
	def start(self):
		print("开始游戏")
		while True:
			self.clock.tick(60)

			self.__event_handler()

			self.__check_collide()

			self.__update_sprites()

			pygame.display.update()
			

	def __create_sprites(self):    #创建精灵族

		bg1 = Backgroup('/home/jiu/桌面/__pycache__/资源/images/background.png')

		bg2 = Backgroup('/home/jiu/桌面/__pycache__/资源/images/background.png')
		bg2.rect.x = bg2.rect.width
		self.back_group = pygame.sprite.Group(bg1,bg2)   #背景组

		self.hero = Hero()
		self.hero1 = Hero()
		self.enemy_group = pygame.sprite.Group()  #敌机组
		self.hero_group = pygame.sprite.Group(self.hero,self.hero1)  #英雄组
		self.bullets = pygame.sprite.Group()
		self.fj1 = Fj()
		self.dfj1 = Fj()
		self.fj2 = Fj2()
		self.dfj2 = Fj2()
		self.fjs = pygame.sprite.Group(self.fj1,self.fj2,self.dfj1,self.dfj2)
	def __event_handler(self):     #事件监听
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				self.__game_over()
			elif event.type == CREATE_ENEMY_EVENT: 
				self.enemy = Enemy()
				self.enemy_group.add(self.enemy)
				if self.enemy.speed == 2:
					self.enemy.fire1()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.hero1.fire()
				elif event.key == 271:
					self.hero.fire()
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[115]:
			self.hero1.speed = 2
			self.fj1.speed = 2
			self.fj2.speed = 2
		elif keys_pressed[119]:
			self.hero1.speed = -2

			self.fj1.speed = -2
			self.fj2.speed = -2


		else:
			self.hero1.speed = 0
			
			self.fj1.speed = 0
			self.fj2.speed = 0

		if keys_pressed[pygame.K_DOWN]:
			self.hero.speed = 2
			self.dfj1.speed = 2
			self.dfj2.speed = 2



		elif keys_pressed[pygame.K_UP]:
			self.hero.speed = -2

			self.dfj1.speed = -2
			self.dfj2.speed = -2


		else:
			self.hero.speed = 0
 
			self.dfj1.speed = 0
			self.dfj2.speed = 0


	def __check_collide(self):    #碰撞检测
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

		pygame.sprite.groupcollide(self.hero1.bullets,self.enemy_group,True,True)
		enemies1 = pygame.sprite.spritecollide(self.hero1,self.enemy_group,True)
		
	#	pygame.sprite.spritecollide(self.hero,self.enemy.bullets1,True,True)
		enemies2 = pygame.sprite.spritecollide(self.hero,self.enemy.bullets1,True)	
		enemies3 = pygame.sprite.spritecollide(self.hero1,self.enemy.bullets1,True)
		if len(enemies)>0 or len(enemies1)>0 or len(enemies2)>0 or len(enemies3)>0:

			self.hero.kill()
# 结束游戏
			PlaneGame.__game_over()


 


	def __update_sprites(self):
		

   #更新精灵族
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero1.bullets,self.bullets,self.enemy.bullets1,self.fjs]:
			group.update()
			group.draw(self.screen)
	@staticmethod
	def __game_over():
		print('游戏结束')
		
		pygame.quit()

		exit()








if __name__ == "__main__":
	game = PlaneGame()
	game.start()
