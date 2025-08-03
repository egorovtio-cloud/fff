import asyncio
import random
import aiohttp
from hikka import utils, loader

class DDOSMod(loader.Module):
    """DDOS модуль для Hikka Userbot"""
    strings = {"name": "DDOSAttack"}

    async def ddoscmd(self, message):
        """Запустить DDOS атаку"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "Укажи URL сайта, еблан.")
            return

        url = args if args.startswith(("http://", "https://")) else f"http://{args}"
        
        # Анимация проверки CloudFlare
        progress = await utils.answer(message, "🔍 Проверяем есть ли CloudFlare...")
        await asyncio.sleep(2)
        
        has_cf = random.choice([True, False])  # 50/50
        
        if has_cf:
            await utils.answer(progress, "🛡️ CloudFlare Присутствует (Шанс успеха: 25%)")
        else:
            await utils.answer(progress, "❌ CloudFlare Отсутствует (Шанс успеха: 75%)")
        
        await asyncio.sleep(1)
        await utils.answer(progress, "🔥 Начинаем DDOS-атаку...")
        
        # Имитация атаки
        steps = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%"]
        for step in steps:
            await asyncio.sleep(1)
            if "30" in step:
                await utils.answer(progress, f"⚡ {step} — сайт начинает нагружаться...")
            elif "60" in step:
                await utils.answer(progress, f"💥 {step} — сервера начинают отключаться...")
            else:
                await utils.answer(progress, f"⏳ {step}...")
        
        await asyncio.sleep(1)
        success = random.random() < (0.25 if has_cf else 0.75)
        
        if success:
            await utils.answer(progress, f"✅ Сайт {url} успешно положен нахуй!")
        else:
            await utils.answer(progress, f"❌ Неудача, феймов хуйлан. Сервер держится.")
        
        # Реальная часть (не рекомендуется, но если надо — раскомментируй)
        # async with aiohttp.ClientSession() as session:
        #     while True:
        #         try:
        #             async with session.get(url) as resp:
        #                 pass
        #         except:
        #             pass
