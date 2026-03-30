# 南京信息工程大学 实验二 Quiz2.py
# 功能：Python知识问答测验 + LED灯光反馈（正确绿灯亮，错误红灯亮）
# 硬件：绿灯 -> GPIO17，红灯 -> GPIO18，树莓派GPIO控制

# 导入树莓派GPIO库和延时库
import RPi.GPIO as GPIO
import time

# -------------------------- 硬件引脚配置 --------------------------
# 定义LED引脚
GREEN_LED = 17  # 绿灯引脚
RED_LED = 18    # 红灯引脚

# -------------------------- GPIO初始化 --------------------------
# 设置GPIO模式为BCM编码
GPIO.setmode(GPIO.BCM)
# 关闭GPIO警告提示
GPIO.setwarnings(False)
# 设置LED引脚为输出模式
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# 初始状态：所有LED熄灭
GPIO.output(GREEN_LED, GPIO.LOW)
GPIO.output(RED_LED, GPIO.LOW)

# -------------------------- 测验题目与答案 --------------------------
def quiz_game():
    # 5道Python测验题
    questions = [
        "1. 以下哪一项不属于Python的数据类型？\na)int  b)float  c)rational  d)string  e)bool\n请输入答案(a-e)：",
        "2. 以下哪一项不属于Python的内置操作？\na)+  b)%  c)abs()  d)sqrt()\n请输入答案(a-d)：",
        "3. 混合整数和浮点数表达式中，Python的类型转换是？\na)浮点数转整数  b)整数转字符串  c)都转字符串  d)整数转浮点数\n请输入答案(a-d)：",
        "4. Python多分支判断的最优语句是？\na)if  b)if-else  c)if-elif-else  d)try\n请输入答案(a-d)：",
        "5. 循环体中终止循环的语句是？\na)if  b)exit  c)continue  d)break\n请输入答案(a-d)："
    ]

    # 正确答案（小写）
    correct_answers = ["c", "d", "d", "c", "d"]
    score = 0  # 初始化分数

    print("="*50)
    print("      Python知识小测验（LED版）")
    print("="*50)

    # 遍历所有题目
    for i in range(len(questions)):
        # 获取用户答案（去除空格、转小写）
        user_ans = input(questions[i]).strip().lower()

        # 判断答案是否正确
        if user_ans == correct_answers[i]:
            # 正确：点亮绿灯
            GPIO.output(GREEN_LED, GPIO.HIGH)
            print("✅ 答案正确！")
            score += 1
        else:
            # 错误：点亮红灯
            GPIO.output(RED_LED, GPIO.HIGH)
            print(f"❌ 答案错误！正确答案：{correct_answers[i]}")

        # 延时1秒，保持灯光状态
        time.sleep(1)
        # 熄灭所有LED，准备下一题
        GPIO.output(GREEN_LED, GPIO.LOW)
        GPIO.output(RED_LED, GPIO.LOW)
        print("-"*50)

    # 最终成绩展示
    print("\n🎉 测验完成！")
    print(f"你的最终得分：{score}/{len(questions)}")
    print("="*50)

# -------------------------- 程序主入口 --------------------------
if __name__ == "__main__":
    try:
        # 运行测验游戏
        quiz_game()
    except KeyboardInterrupt:
        # 处理Ctrl+C退出程序
        print("\n\n程序已手动退出")
    finally:
        # 无论程序如何结束，都清理GPIO资源
        GPIO.cleanup()
        print("GPIO资源已清理")
