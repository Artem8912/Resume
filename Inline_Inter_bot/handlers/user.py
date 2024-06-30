from aiogram import F, Router, html
import uuid
from Data.data_inline import links,photo_links
from aiogram.filters import CommandStart
from aiogram.types import (Message,CallbackQuery,InlineKeyboardButton,
                           InlineKeyboardMarkup,InlineQuery,
                           InlineQueryResultArticle, InputTextMessageContent,InputMediaPhoto,
                           InlineQueryResultCachedPhoto,InlineQueryResultPhoto)
from fluentogram import TranslatorRunner
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner

user_router = Router()

@user_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
f'Привет! Это инлайн-бот, который поможет вам получить информацию ' 
f'о самых популярных сайтах для туристов. Чтобы получить информацию на:\n'
f'1. Английском языке - введите user_name бота + tour_info_en\n'
f'2. Русском языке - введите user_name бота + tour_info_ru\n'
f'3. Французском языке - введите user_name бота + tour_info_fr'
                         )
    
@user_router.inline_query(F.query == 'tour_info_en')
async def show_inline(inl_q:InlineQuery,i18n_en:TranslatorRunner):
               
        result = [InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_en.skyrunner.title(),description=i18n_en.skyrunner.description(),input_message_content=InputTextMessageContent(message_text=i18n_en.skyrunner.description(),title=i18n_en.skyrunner.title(),parse_mode='HTML'),url=links[1],thumbnail_url=photo_links[1]),
                 InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_en.travelata.title(),description=i18n_en.travelata.description(),input_message_content=InputTextMessageContent(message_text=i18n_en.travelata.description(),title=i18n_en.travelata.title(),parse_mode='HTML'),url=links[2],thumbnail_url=photo_links[2]),
                 InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_en.OnlineTours.title(),description=i18n_en.OnlineTours.description(),input_message_content=InputTextMessageContent(message_text=i18n_en.OnlineTours.description(),title=i18n_en.OnlineTours.title(),parse_mode='HTML'),url=links[3],thumbnail_url=photo_links[3]) ,
                 InlineQueryResultPhoto(id=str(uuid.uuid4()),photo_height=None,photo_width=None,photo_url=photo_links[4],title='',caption='',input_message_content=InputTextMessageContent(message_text='',title = ''),description='фото' ,thumbnail_url=photo_links[4])]
            
        await inl_q.answer(id=inl_q.id,results=result,is_personal=True,cache_time=1)
        
@user_router.inline_query(F.query == 'tour_info_ru')
async def show_inline(inl_q:InlineQuery,i18n_ru:TranslatorRunner):
               
        result = [InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_ru.skyrunner.title(),description=i18n_ru.skyrunner.description(),input_message_content=InputTextMessageContent(message_text=i18n_ru.skyrunner.description(),title=i18n_ru.skyrunner.title(),parse_mode='HTML'),url=links[1],thumbnail_url=photo_links[1]),
                 InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_ru.travelata.title(),description=i18n_ru.travelata.description(),input_message_content=InputTextMessageContent(message_text=i18n_ru.travelata.description(),title=i18n_ru.travelata.title(),parse_mode='HTML'),url=links[2],thumbnail_url=photo_links[2]),
                 InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_ru.OnlineTours.title(),description=i18n_ru.OnlineTours.description(),input_message_content=InputTextMessageContent(message_text=i18n_ru.OnlineTours.description(),title=i18n_ru.OnlineTours.title(),parse_mode='HTML'),url=links[3],thumbnail_url=photo_links[3]) ,
                 InlineQueryResultPhoto(id=str(uuid.uuid4()),photo_height=None,photo_width=None,photo_url=photo_links[4],title='',caption='',input_message_content=InputTextMessageContent(message_text='',title = ''),description='фото' ,thumbnail_url=photo_links[4])]
            
        await inl_q.answer(id=inl_q.id,results=result,is_personal=True,cache_time=1)
        
@user_router.inline_query(F.query == 'tour_info_fr')
async def show_inline(inl_q:InlineQuery,i18n_fr:TranslatorRunner):
               
        result = [InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_fr.skyrunner.title(),description=i18n_fr.skyrunner.description(),input_message_content=InputTextMessageContent(message_text=i18n_fr.skyrunner.description(),title=i18n_fr.skyrunner.title(),parse_mode='HTML'),url=links[1],thumbnail_url=photo_links[1]),
                 InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_fr.travelata.title(),description=i18n_fr.travelata.description(),input_message_content=InputTextMessageContent(message_text=i18n_fr.travelata.description(),title=i18n_fr.travelata.title(),parse_mode='HTML'),url=links[2],thumbnail_url=photo_links[2]),
                 InlineQueryResultArticle(id=str(uuid.uuid4()),title=i18n_fr.OnlineTours.title(),description=i18n_fr.OnlineTours.description(),input_message_content=InputTextMessageContent(message_text=i18n_fr.OnlineTours.description(),title=i18n_fr.OnlineTours.title(),parse_mode='HTML'),url=links[3],thumbnail_url=photo_links[3]) ,
                 InlineQueryResultPhoto(id=str(uuid.uuid4()),photo_height=None,photo_width=None,photo_url=photo_links[4],title='',caption='',input_message_content=InputTextMessageContent(message_text='',title = ''),description='фото' ,thumbnail_url=photo_links[4])]
            
        await inl_q.answer(id=inl_q.id,results=result,is_personal=True,cache_time=1)


