from random import randint
import json

#色子类和用户类
class Die():
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		x = randint(1,self.sides)
		print("你摇到了："+str(x),end = ",")
		return x

class User():
	def __init__(self, user_name, money, choice = ''):   
		self.user_name = user_name
		self.money = money
		self.choice = choice
		self.win_record = 0


#局数
time = 1

#函数声明
def introduce_rules():
	"""介绍游戏规则"""
	print("-------欢迎您来到摇色子游戏-------")
	print("-------游戏规则介绍-------")
	print("本游戏两位玩家参与，摇10次色子，玩家押注并赌大更多或者小更多或者大小一样多（平），输的一方将把本局所有赌注给赢的一方，都猜对或猜错算平局")

def play():
	"""一局游戏"""	
	#摇到大和小的次数
	die = Die()
	big = 0
	little = 0
	for i in range(1,11):
		print("这是第"+str(i)+"次",end=",")
		j = die.roll_die()
		if j <= 3:
			little += 1
			print("属于 小")
		else:
			big += 1
			print("属于 大")
	if big > little:
		print("这局大更多")
		return "大"
	elif big <little:
		print("这局小更多")
		return "小"
	else:
		print("这局大小一样多")
		return "平"

def show_result(winner, loser, token, result):
	"""处理本局结果，输入赢家、输家、赌注、结果"""
	print("本局 "+winner.user_name.title()+" 胜，获得￥"+str(token))
	winner.money += token
	loser.money -= token
	if result == '平':
		winner.money += 2*token
		print(winner.user_name+"获得额外奖励：￥"+str(2*token))

#介绍规则
introduce_rules()

#创建玩家
name_temp = input("玩家1，请输入的昵称：")
money_temp = input("玩家1，您带了多少钱：")
user1 = User(name_temp,int(money_temp))

print("玩家1角色创建成功")
name_temp = input("玩家2，请输入的昵称：")
money_temp = input("玩家2，您带了多少钱：")
user2 = User(name_temp,int(money_temp))
print("玩家2角色创建成功")

#开始游戏
print("-------游戏开始-------")
standard_choice = ['大','小','平']
while True:
	print("~~~~~~~~~~")
	print("这是第"+str(time)+"局")
	print("~~~~~~~~~~")
	time += 1#局数自增1
	token = randint(1,100)
	print("这局的赌注是："+str(token))	
	#检查是否能开启本局
	if user1.money < token:
		print(user1.user_name+"的钱不够玩了……")
		break
	if user2.money < token:
		print(user2.user_name+"的钱不够玩了……")
		break	
	user1.choice = input(user1.user_name.title()+",你的选择是？（大、小还是平）")
	while user1.choice not in standard_choice:
		user1.choice = input(user1.user_name.title()+",你的选择是？（大、小还是平）")
	user2.choice = input(user2.user_name.title()+",你的选择是？（大、小还是平）")
	while user2.choice not in standard_choice:
		user2.choice = input(user2.user_name.title()+",你的选择是？（大、小还是平）")
	result = play()
	if user1.choice == result and user2.choice != result:
		show_result(user1, user2, token, result)
	elif user2.choice == result and user1.choice != result:
		show_result(user2, user1, token, result)
	else:
		print("这局平局，谁都不输不赢。")
		continue
	#目前状况
	print("$$$目前状况$$$")
	print(user1.user_name+"的余额还有：￥"+str(user1.money))
	print(user2.user_name+"的余额还有：￥"+str(user2.money))

print("-------游戏结束！-------")
print("获胜的是",end = '')
if user1.money > user2.money:
	print(user1.user_name)
else:
	print(user2.user_name)

	

#改进处
#1.将本局结果显示用函数show_result()处理
#2.增加了庄家角色
#3.随时可以结束当前轮游戏
#4.