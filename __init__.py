import os

from nonebot import on_command
from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, ArgPlainText
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
)


from .download import download_main, save_readme
from .readme import readme_main, read_readme

__help__plugin_name__ = "readme"
__des__ = "获取 nonebot 插件 readme 文档"
__cmd__ = f"""
触发方式：readme + 插件名称 + 参数
发送“readme”查看支持的指令
""".strip()
__short_cmd__ = 'readme {name} {command}'
__example__ = """
readme
readme update
readme upgrade
readme nonebot_plugin_manager
""".strip()
__usage__ = f"{__des__}\n\nUsage:\n{__cmd__}\n\nExamples:\n{__example__}"


readme = on_command("readme", rule=to_me(), aliases={"读我", "文档"}, priority=1)


@readme.handle()
async def readme_help(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 发送命令时跟随的参数，例：readme update，args为update
    if plain_text:
        matcher.set_arg("para", args)  # 如果用户发送了参数则直接赋值
    else:
        readme_text = await read_readme()
        await readme.finish(readme_text)


@readme.got("para")
async def handle_para(bot: Bot, event: MessageEvent, para_name: str = ArgPlainText("para")):
    if para_name not in ['update', 'upgrade']:
        readme_text = await read_readme(para_name)
        try:
            await readme.finish(readme_text)
        except:
            await readme.finish('查询插件readme过长，请联系机器人管理员')
    else:
        if str(event.user_id) in bot.config.superusers:
            if para_name == 'update':
                save_readme()
            else:
                download_main()
                readme_main()
            readme_text = '更新完成！请查看工作目录plugin.json, 查看readme！'
        else:
            readme_text = '插件 readme 的更新需要管理员权限！'
        await readme.finish(readme_text)
