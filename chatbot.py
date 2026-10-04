# learning-chat-bot 简易本地对话机器人
# 仅用于个人学习，代码演示文本问答基础能力
def chatbot_reply(user_input):
    user_input = user_input.strip().lower()
    if "python" in user_input or "代码" in user_input:
        return "Python是一门易上手的编程语言，可以用来写脚本、开发小工具。"
    elif "笔记" in user_input or "整理" in user_input:
        return "可以使用Markdown格式整理学习笔记，结构清晰方便查阅。"
    elif "快速排序" in user_input:
        return "快速排序采用分治思想，选基准值，把数组分成大小两部分递归排序。"
    elif "你好" in user_input:
        return "你好！我是本地学习助手，有什么学习问题可以问我。"
    else:
        return "收到你的问题，我可以帮你梳理知识点、讲解编程相关内容。"

if __name__ == "__main__":
    print("=== 本地学习Bot已启动 ===")
    print("输入你的问题，输入exit退出程序\n")
    while True:
        question = input("user：")
        if question.lower() == "exit":
            print("Bot：程序结束")
            break
        resp = chatbot_reply(question)
        print(f"bot：{resp}\n")
