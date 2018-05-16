import random 
import time 
import tkinter as tk 
import datetime 
import time 
class LoveYou(): 
 	def __init__(self): 
 		d = datetime.datetime.now() 
		self.window = tk.Tk()
		self.text = tk.StringVar() 
		self.count = tk.StringVar() 
		self.day= d.weekday()+1 
		self.list=["薛栋炎","刘瑞涛","娄雪嫚","张轩轩","郝竟良","张晨波","王晓俊","李鑫","刘明松","崔利艳","张圆","那思源","韩月瑞","王保轩","贾纪闯","翟宏乐","杨振亚","闫子雄","梁文琦","陈怡杰","韩迪","张世豪","李明瑞","王淋","于奇林","吴金航","王含青","王润泽","庞源松"] 
		#第2步，给窗口的可视化起名字 
		self.window.title('班级考单词程序') 
		#第3步，设定窗口的大小(长＊宽) 
		self.window.geometry('600x400')  
		#安置lable的方法有：1）l.pack();2)l.place(); 
	def find(self): 
		for l in range(50): 
			str = '' 
			if l == 47: 
				time.sleep(0.5) 
			elif l == 48: 
				time.sleep(0.6) 
			elif l == 48: 
				time.sleep(0.7) 
			elif l == 49: 
				time.sleep(0.9) 
			else: 
				time.sleep(0.1)	 
			i = random.randint(0,len(self.list)-1) 
			str += "呦,你被上帝选中了:-----%s\n"%self.list[i] 
			if l == 49: 
				self.list.pop(i) 
			j = random.randint(0,len(self.list)-1) 
			str += "呦，你看着也很不错呀:------%s\n"%self.list[j] 
			self.text.set(str) 
			self.window.update() 
			if l == 49: 
				self.savePeople(str)	 
	def kill(self): 
		str1 = time.strftime('%Y-%m-%d',time.localtime(time.time()))+"  星期"+str(self.day) 
		if self.day == 1: 
			count = random.randint(50,100) 
			str1+="上帝奖励了你们组%d遍"%(count) 
			self.count.set(str1) 
		elif self.day == 2:	 
			count = random.randint(50,120) 
			str1+="上帝奖励了你们组%d遍"%(count) 
			self.count.set(str1) 
		elif self.day == 3:	 
			count = random.randint(50,140) 
			str1+="上帝奖励了你们组%d遍"%(count) 
			self.count.set(str1) 
		elif self.day == 4:	 
			count = random.randint(50,160) 
			str1+="上帝奖励了你们组%d遍"%(count) 
			self.count.set(str1) 
		elif self.day == 5:	 
			count = random.randint(50,180) 
			str1+="上帝奖励了你们组%d遍"%(count) 
			self.count.set(str1) 
		self.window.update()	 
		self.saveCount(str1)
	def savePeople(self,person,encoding='utf-8'): 
		with open('log.txt','a') as f: 
			f.write(person) 
	def saveCount(self,count): 
		with open('log.txt','a',encoding='utf-8') as f: 
			f.write(str(count)+'\n')		 
			f.write('--------------------------------')	 				 
	def main(self): 
		#第4步，在图形界面上设定标签 
		now = time.strftime('%Y-%m-%d',time.localtime(time.time()))+"  星期"+str(self.day) 
		now += "\n班级总人数:%s人"%str(len(self.list)) 
		now	+= "\n正在合理计算中\n" 
		l2= tk.Label(self.window,fg = 'red',text=now,width=500,height=5)         
		l2.config(font = 'Helvetica -%d bold' % 15) 
		l2.pack() 
		#第4步，在图形界面上设定标签 
		l= tk.Label(self.window,fg = 'red',textvariable=self.text,width=500,height=3)         
		l.config(font = 'Helvetica -%d bold' % 20) 
		#说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高 
		#第5步，安置标签 
		l.pack() 
		#第4步，在图形界面上设定标签 
		l1= tk.Label(self.window,fg = 'red',textvariable=self.count,width=500,height=3)         
		l1.config(font = 'Helvetica -%d bold' % 20) 
		#说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高 
		#第5步，安置标签 
		l1.pack() 
		b=tk.Button(self.window,text="筛选",width=15,height=2,command=self.find) 
		b.pack() 
		b1=tk.Button(self.window,text="惩罚",width=15,height=2,command=self.kill) 
		b1.pack() 
		#第6步， 
		self.window.mainloop() 
if __name__ == '__main__': 
	loveyou  = LoveYou() 
	loveyou.main() 
