import re
import os
import json


from .download import readme_path


def md2txt(md: str) -> str:
    """将 md 大部分内容转换为文本"""
    md = re.sub('(~~)(.*?)\1', '', md)  # 删除线
    md = re.sub('!\[]\((.*?)\)', '', md)  # [](图片)
    md = re.sub('(?=!)(.+)(?<=\))', '', md)  # !……)图片
    md = re.sub('(?=<)(.+?)(?<=>)', '', md)  # <尖括号>
    # * 粗体 斜体;  ` 代码;   # 标题;   []中括号;  杂项
    md = md.replace('*', '').replace('`', '').replace('#', '').replace('+', '')
    md = md.replace('[', '').replace(']', '').replace('<!--', '').replace('-->', '')
    md = re.sub('(?=\n)(\s+?)(?=\n)', '', md)  # 空白行
    return md


def get_readme(name: str):
    """读取 md，消除 markdown 符号，写入 readme"""
    with open(os.path.join(readme_path, name, 'README.md'), encoding='utf-8') as md:
        readme = md.read()
        with open(os.path.join(readme_path, name, 'readme'), 'w+', encoding='utf-8') as rd:
            rd.write(md2txt(readme))


async def read_readme(name: str = 'nonebot_plugin_readme') -> str:
    """文本方式读取 name 位置的 readme, 默认为本插件的readme"""
    try:
        with open(os.path.join(readme_path, name, 'readme'), encoding='utf-8') as f:
            readme = f.readlines()
    except:
        readme = '查找的插件不存在！请检查输入后重试。'
    return readme


def readme_main():
    with open('plugins.json', encoding='utf-8') as f:
        """读取 json """
        plugins_json = json.load(f)
    for plugins_dict in plugins_json:
        """读取 json 字典中 module_name 给 name"""
        try:
            """把 json 中匹配的文件全部转换为文本"""
            get_readme(name=plugins_dict['module_name'])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    readme_path = os.path.join(current_path, 'data', 'readme')
    readme_main()
