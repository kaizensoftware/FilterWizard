import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'BMK_Media_Search')
API_ID = int(environ.get('API_ID', '1'))
API_HASH = environ.get('API_HASH', None)
BOT_TOKEN = environ.get('BOT_TOKEN', None)

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/9400e40a362dec4d85676.jpg https://telegra.ph/file/9400e40a362dec4d85676.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '1').split()] #Database Channels
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS
AUTH_CHANNEL = environ.get('AUTH_CHANNEL', None) #ForceSubcribe Channel
AUTH_GROUPS = [int(ch) for ch in environ.get("AUTH_GROUPS", '1').split()] #Allowed Chat IDs

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://FurmanDurman:c1kulat@cluster1.1i25cyg.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Kaizenbase")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Kaizen_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'bmkdestekhattibot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'True')), True)
IMDB = is_enabled((environ.get('IMDB', 'False')), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>📂 İçerik Adı:</b><i> {file_caption}</i>\n💠 <b>Dosya Boyutu:</b> <i>{file_size}\n\n📌 <b>[Bir Mühendisin Kanalları](https://t.me/birmuhendisinkanallari)</i></b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b>📂 İçerik Adı:</b><i> {file_caption}</i>\n💠 <b>Dosya Boyutu:</b> <i>{file_size}\n\n📌 <b>[Bir Mühendisin Kanalları](https://t.me/birmuhendisinkanallari)</i></b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 İçerik Adı: <a href={url}>{title}</a>\n🔢 Imdb ID: <code>{imdb_id}</code>\n🔮 Yıl: {year} \n⭐️ Puan: {rating}/ 10 \n🎭 Tür: {genres} \n\nİsteği yapan kişinin bilgileri:\n\nID: {user_id}\nİsim: {user_name}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
