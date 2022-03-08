from aiogram.dispatcher.filters.state import StatesGroup,State
# States
class GoogleTarjima(StatesGroup):
    src=State()
    dest=State()
    text=State()