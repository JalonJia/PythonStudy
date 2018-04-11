
'''
text = input("What's your name?")
print('Welcome %s' % text)
'''

#猜谜游戏
iResult = 38

answer = input("请猜出答案，答案是一个1到100之间的数字：")
youranswer = int(answer)
while youranswer != iResult:
    if youranswer < iResult:
        notice = "对不起，你猜猜的数字太小了，请继续猜"
    else :
        notice = "对不起，你猜猜的数字太大了，请继续猜"
        
    answer = input(notice)
    youranswer = int(answer)

print("恭喜，你猜对了！")


