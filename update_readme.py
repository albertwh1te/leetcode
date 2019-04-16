import os
import json
import requests
from functools import reduce
from operator import add


def get_all_problems():
    leetcode_url = "https://leetcode.com/api/problems/algorithms/"
    raw = requests.get(leetcode_url)
    return json.loads(raw.content)


def get_solved_numbers():
    dir_list = ["./cpluscplus/", "./Python/", "./Golang/"]
    files_list = [os.listdir(x) for x in dir_list]
    files = set([
        int(x.split(".")[0]) for x in reduce(add, files_list)
        if x.split(".")[0].isdigit()
    ])
    return files


def get_solved_by_language():
    dir_list = ["./Python/", "./cpluscplus/", "./Golang/"]
    files_list = [os.listdir(x) for x in dir_list]
    files_list = [[
        int(name.split(".")[0]) for name in names
        if name.split(".")[0].isdigit()
    ] for names in files_list]
    return tuple(files_list)


def solved_filter(item):
    numbers = get_solved_numbers()
    if item["stat"]["question_id"] in numbers:
        return True
    return False


def generate_markdown_head(file_path):
    with open(file_path, 'w') as f:
        f.write(
            "# :smiley: Let's have fun with LeetCode! [![Build Status](https://travis-ci.org/MarkWh1te/leetcode.svg?branch=master)](https://travis-ci.org/MarkWh1te/leetcode)\n\n"
        )
        f.write(
            "## My LeetCode account is :point_right: [here.](https://leetcode.com/iamwh1temark/)\n\n"
        )


def generate_markdown_table(file_path, items):
    python_ids, cplusplus_ids, golang_ids = get_solved_by_language()
    github_leetcode_url = 'https://github.com/hey-bruce/algorithms_and_oj/blob/master/leetcode-algorithms/'
    leetcode_url = 'https://leetcode.com/problems/'
    with open(file_path, 'a') as f:
        f.write("I have solved these problems.\n\n")
        f.write("\n")
        f.write("| ID | Title | Python | C++ | Go |\n")
        f.write('|---' * 5 + '|\n')
        for item in items:
            info = item['stat']
            question_id = info["question_id"]
            question_title = info["question__title"]
            question_url = leetcode_url + info[
                "question__title_slug"] + '/description/'

            python_path = "https://github.com/MarkWh1te/leetcode/blob/master/Python/{number}.py".format(
                number=question_id)
            Python_value = '[Python]({})'.format(
                python_path) if question_id in python_ids else 'TODO'
            cplusplus_path = "https://github.com/MarkWh1te/leetcode/blob/master/cpluscplus/{number}.cpp".format(
                number=question_id)
            cplusplus_value = '[C++]({})'.format(
                cplusplus_path) if question_id in cplusplus_ids else 'TODO'
            golang_path = "https://github.com/MarkWh1te/leetcode/blob/master/Golang/{number}/{number}.go".format(
                number=question_id)
            golang_value = '[Go]({})'.format(
                golang_path) if question_id in golang_ids else 'TODO'

            data = {
                'id': question_id,
                'title': '[{}]({})'.format(question_title, question_url),
                'Python': Python_value,
                'C++': cplusplus_value,
                'Go': golang_value
            }
            line = '|{id}|{title}|{Python}|{C++}|{Go}|\n'.format(**data)
            f.write(line)


def generate_markdown(items):
    file_path = './README.md'
    generate_markdown_head(file_path)
    generate_markdown_table(file_path, items)


def main():
    problems = reversed(get_all_problems()["stat_status_pairs"])
    solved = list(filter(solved_filter, problems))
    generate_markdown(solved)
    print("update README.md success!")


if __name__ == "__main__":
    main()