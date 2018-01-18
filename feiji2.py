import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,700,480)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERP_FIRE_EVENT = pygame.USEREVENT + 1
ENEMY = pygame.USEREVENT + 1 
#ENEMY_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)  #加载图像
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.x -= self.speed


class Backgroup(GameSprite):

#	def __init__(self):
#		super().__init__(image_name)


	def update(self):
		super().update()
		if self.rect.x <= -SCREEN_RECT.width:
			self.rect.x = self.rect.width



class Hero(GameSprite):
	def __init__(self):
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/life.png',0)

		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()
		self.fjs = pygame.sprite.Group()

	def update(self):

		self.rect.y += self.speed
		if self.rect.top < 47:
			self.rect.top = 47
		elif self.rect.bottom > SCREEN_RECT.bottom - 51:
			self.rect.bottom = SCREEN_RECT.bottom - 51


	def fire(self):
		bullet = Bullet()
		bullet.rect.bottom = self.rect.centery + 45
		bullet.rect.centerx = self.rect.centerx

		bullet1 = Bullet()
		bullet1.rect.bottom = self.rect.centery 
		bullet1.rect.centerx = self.rect.centerx
		bullet2 = Bullet()

		bullet2.rect.bottom = self.rect.centery - 45
		bullet2.rect.centerx = self.rect.centerx
		self.bullets.add(bullet,bullet1,bullet2)
class Enemy(GameSprite):
	def __init__(self):
		
		
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/enemy2.png')
		#d = [a,b,c]




		a = '/home/jiu/桌面/__pycache__/资源/images/enemy3_down1.png'
		b = '/home/jiu/桌面/__pycache__/资源/images/enemy2.png'
		c = '/home/jiu/桌面/__pycache__/资源/images/enemy1.png'

		d = random.randint(1,4)
		if d == 1:
					
			super().__init__(a)
		elif d == 2:
			
			super().__init__(b)
		elif d == 3:	
	
			super().__init__(c)
		else:
			
			super().__init__(a)
		self.speed = random.randint(1,3)
		self.rect.bottom = 0

		self.bullets1 = pygame.sprite.Group()

		max_y = SCREEN_RECT.height - self.rect.height
		self.rect.y = random.randint(0,max_y)
		self.rect.x = SCREEN_RECT.width - self.speed
	def fire1(self):
		bullet1 = EnemyBullet()
		bullet1.rect.y = self.rect.bottom + 20
		bullet1.rect.centerx = self.rect.centerx
		self.bullets1.add(bullet1)



	def update(self):
		super().update()
		if self.rect.x < 0:
			self.kill()
	
	def __del__(self):
		print("%s飞机死了啦"%self.rect)


class Bullet(GameSprite):

	def __init__(self):
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/bullet2.png',-5)

	def update(self):
		super().update()
		if self.rect.y >= 480:
			self.kill()
	def __del__(self):
		print("没了")
class EnemyBullet(GameSprite):
	def __init__(self):
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/bomb.png',5)
	def update(self):
		super().update()
		if self.rect.x < 0:
			self.kill()
	def __del__(self):
		print("子弹消失了")
class Fj(GameSprite):
	def __init__(self):
			
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/enemy1_down1.png',0)
		self.rect.x = 300
		self.rect.y = 270
		



	def update(self):

		self.rect.y += self.speed
		if self.rect.top < 2:
			self.rect.top = 2
		elif self.rect.bottom > SCREEN_RECT.bottom - 85:
			self.rect.bottom = SCREEN_RECT.bottom - 85




class Fj2(GameSprite):
	def __init__(self):
			
		super().__init__('/home/jiu/桌面/__pycache__/资源/images/enemy1_down1.png',0)
		self.rect.x = 300
		self.rect.y = 350
		



	def update(self):

		self.rect.y += self.speed
		if self.rect.top < 82:
			self.rect.top = 82
		elif self.rect.bottom > SCREEN_RECT.bottom - 4:
			self.rect.bottom = SCREEN_RECT.bottom - 4

















