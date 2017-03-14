#coding=utf-8
#python定时爬取

import time,sched,os,urllib2,re,string
#sched是一种调度（延时处理机制）

#初始化sched模块 scheduler类
schedule=sched.scheduler(time.time,time.sleep)#参数（时间戳，延时方法)

#定时调取函数
def execute_command():#执行命令
	#爬取数据
	request = urllib2.Request("http://bbs.xuegod.cn")
	response = urllib2.urlopen(request)
	reader = response.read()
	response.close()
	#print reader
	#匹配规则
	usernump = re.compile(r'人数<br><em>.*?</em>')
	usernummatch = usernump.findall(reader)

	if usernummatch:
		#print usernummatch
		currentnum = usernummatch[0]
		currentnum = currentnum[string.index(currentnum,'>')+5:string.rindex(currentnum,'<')]
		#print currentnum
		print "当前时间：",time.strftime('%Y年%m月%d日%H时%M分',time.localtime(time.time())),'论坛在线人数：',currentnum

def timing(inc):
	schedule.enter(inc,0,timing,(inc,))
	execute_command()

def main(inc=10):
	schedule.enter(0,0,timing,(inc,))
	schedule.run()

#可以让你写的模块既可以导入到别的模块中使用，该模块自己也可以执行
if __name__=="__main__":
	main()


