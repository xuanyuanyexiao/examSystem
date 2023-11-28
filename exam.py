import time
import random
import json

score = 0
wrong_questions = []  # 错题列表


def display_question(question):
    print(question['question'])
    for option in question['options']:
        print(option)


def check_answer(question, answer):
    global score
    if answer == question['answer']:
        score += 1
    else:
        print("很遗憾，你错了呢，正确答案是：", question['answer'])
        wrong_questions.append(question)  # 将错题添加到错题列表


def review_wrong_questions():
    global score
    print("开始复习错题...")
    print("ps:多选题请按字母顺序选择")

    wrong_count = len(wrong_questions)  # 错题数量
    score = 0
    while wrong_questions:
        question = wrong_questions.pop(0)
        print("剩余错题数量：", len(wrong_questions)+1)
        display_question(question)
        user_answer = input("请输入您的答案：")
        check_answer(question, user_answer.upper())
    if score == wrong_count:
        print('恭喜您复习错题全部正确，程序将在5秒后退出，祝您考试顺利')
        time.sleep(5)
    else:
        review_wrong_questions()


def random_quiz():
    global score
    random.shuffle(questions)

    print("欢迎使用马克思主义原理概论选择题科目一式刷题系统")
    print("请注意，只有将题目全部选择正确，程序才会停止，否则接着刷错题！")
    print("ps:多选题请按字母顺序选择")

    for i, question in enumerate(questions):
        print("第", i + 1, "题")
        display_question(question)
        user_answer = input("请输入您的答案：")
        check_answer(question, user_answer.upper())
    print(f"您本轮的最终成绩为：{score}/{len(questions)}" )
    if score == len(questions):
        print('恭喜您选择题全对，程序将在5秒后退出，祝您考试顺利')
        time.sleep(5)
    else:
        review_wrong_questions()


if __name__ == '__main__':
    with open('questions.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)

    random_quiz()
