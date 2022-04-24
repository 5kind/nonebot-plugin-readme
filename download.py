import asyncio
import json
import os

import aiofiles
import aiohttp

current_path = os.path.dirname(__file__)
readme_path = os.path.join(current_path, 'data', 'readme')


def get_page(module_name, url) -> str:
    """
        读取 rules 内 module_name 列表为 url 变换规则：
        0. 满足则返回去除 /tree /master 添加 /README.md，否则添加 /README.md
        1. md 替换为 markdown
        2. 无 README （或用户禁用了更新） 返回空字符串
    """
    url = url.replace('https://github.com/', 'https://cdn.jsdelivr.net/gh/')
    with open(os.path.join(current_path,'rules.json'), encoding='utf-8') as f:
        rules = json.load(f)
        if module_name in rules[0]:
            return url.replace('/tree', '').replace('/master', '') + '/README.md'
        url = url + '/README.md'
        if module_name in rules[1]:
            url = url.replace('md', 'markdown')
        if module_name in rules[2]:
            url = ''
        return url


async def download_url(url, path):
    """
    下载 url 到 path
    1. await 下载
    2. await 写入
    """
    async def fetch(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def fwrite(path, text):
        async with aiofiles.open(path, 'w+', encoding='utf-8') as f:
            await f.write(text)

    async def fmain(url, path):
        text = await fetch(url)
        await fwrite(path, text)

    try:
        dir_name = os.path.dirname(path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        await asyncio.gather(fmain(url, path))
    except Exception as e:
        if url == '':
            return str(path)+'没有README文档, 或已禁用更新'
        else:
            return str(url)+'下载失败\n错误代码'+str(e)


async def save_readme(download_dict=None):
    """解析并依据字典下载 json 或 readme"""
    tasks = []
    # return_info = ''
    if not download_dict:
        tasks.append(download_url('https://cdn.jsdelivr.net/gh/nonebot/nonebot2/website/static/plugins.json',
                                  os.path.join(current_path, 'plugins.json')))
    else:
        for key, value in download_dict.items():
            """key 作为 readme 下载 path 或 plugins.json 下载参数, value 作为 下载 url"""
            path = os.path.join(readme_path, key, 'README.md')
            tasks.append(download_url(value, path))
    await asyncio.gather(*tasks)


async def download_main():
    while not os.path.isfile(os.path.join(current_path,'plugins.json')):
        """下载 plugins.json"""
        await save_readme()
    with open(os.path.join(current_path,'plugins.json'), encoding='utf-8') as f:
        """读取 json """
        plugins_json = json.load(f)
    readme_dict = {}
    for plugins_dict in plugins_json:
        """readme_dict: key 作为 readme 下载 path , value 作为 下载 url"""
        module_name = plugins_dict['module_name']
        url = get_page(module_name, plugins_dict['homepage'])
        readme_dict[module_name] = url
    await save_readme(readme_dict)


if __name__ == '__main__':
    """需要 rule.json"""
    import time
    start = time.time()
    current_path = os.path.dirname(__file__)
    readme_path = os.path.join(current_path, 'data', 'readme')
    asyncio.get_event_loop().run_until_complete(download_main())
    print('完成, 用时', time.time() - start)
