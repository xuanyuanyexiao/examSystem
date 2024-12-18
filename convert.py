import docx
import re
import json


# 读取Word文档
def read_word_file(file_path):
    doc = docx.Document(file_path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]


# 提取问题和选项
def parse_questions(text_lines):
    questions = []
    current_question = {}

    # 用于匹配问题和答案（包括括号内的答案字母）
    question_pattern = re.compile(r'(\d+)\.(.*?)（\s*([A-D]{1,4})\s*）')
    # 用于匹配选项的正则表达式，去除多余的空格并提取选项
    options_pattern = re.compile(r'([A-D])、\s*(.*?)\s*$')

    for line in text_lines:
        # 查找问题和答案
        match_question = question_pattern.match(line)
        if match_question:
            # 如果找到匹配的题目格式，保存问题内容和答案
            if current_question:
                questions.append(current_question)
            current_question = {
                "question": match_question.group(2).strip(),  # 问题文本
                "options": [],
                "answer": match_question.group(3).strip()  # 答案字母
            }
        # 查找选项
        match_option = options_pattern.match(line)
        if match_option:
            # 将选项字母与内容结合，并添加到当前问题的选项列表中
            current_question["options"].append(f'{match_option.group(1)}. {match_option.group(2).strip()}')

    # 添加最后一题
    if current_question:
        questions.append(current_question)

    return questions


# 将数据转换成JSON格式并保存
def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 主函数
def main(input_file, output_file):
    text_lines = read_word_file(input_file)  # 读取文件内容
    questions = parse_questions(text_lines)  # 解析问题
    save_to_json(questions, output_file)  # 保存为JSON格式


# 示例用法
if __name__ == "__main__":
    input_file = 'input.docx'  # 输入的Word文件路径
    output_file = 'output.json'  # 输出的JSON文件路径
    main(input_file, output_file)
    print("输出成功")
