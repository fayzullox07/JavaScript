import logging
from googletrans import Translator
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from markups import lan_btn, btn
from states import GoogleTarjima

# import googletrans
tarjimon = Translator()


# Aiogram Aunfecitaion
logging.basicConfig(level=logging.INFO)
TOKEN = '5179135848:AAESCXopLTEMjaxzJKOeD_QCXMRwyC34LtI'
bot = Bot(token=TOKEN)


dp = Dispatcher(bot, storage=MemoryStorage())
















































@dp.message_handler(command=['start'])
async def send_query(message):
    await message.reply(f"<i>Asaslomu alaykum <b>{message.chat.first_name}</b> men Google Translate ning telegramdagi maxsus versiyasiman! \n Matni qaysi tilda ekanligini tanlang</i>",parse_mode='html',reply_markup=btn)
    await GoogleTarjima.src.set()

@dp.callback_query_handler(state=GoogleTarjima.src)
async def get_lang(call: CallbackQuery,state: FSMContext):
    src = call.data
    await state.update_data(
        {"src": src}
    )
    print(src)

    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("<b>Matn qaysi tilga tarjima qilinsin!!!</b>", reply_markup=lan_btn,parse_mode='html')
    await GoogleTarjima.next()
@dp.callback_query_handler(state=GoogleTarjima.dest)
async def get_lang_word(call: CallbackQuery,state: FSMContext):
    dest = call.data
    await state.update_data(
        {"dest":dest}
    )

    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("<b>Iltimos kerakli matnni kiriting!!!</b>",parse_mode='html')
    await GoogleTarjima.next()

@dp.message_handler(state=GoogleTarjima.text)
async def return_word(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {"text": text}
    )
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    src = data.get("src")
    dest= data.get("dest")
    text = data.get("text")
    word=tarjimon.translate(text,dest=dest,src=src)
    print('#################')
    # print(xabar)
    print('Send loading')
    await message.answer(word.text)
    await state.finish()
    # await message.reply("")

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






