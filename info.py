import re
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#--------------ʙᴏᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ----------#

SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '13687927'))
API_HASH = environ.get('API_HASH', '469e3f62b54f83f9839216aefab5136f')
BOT_TOKEN = environ.get('BOT_TOKEN', '6180535160:AAGu1FahR2tqFxeQLFWkVqrYCsgj1PwVsfM')

#---------------ᴀʟʟ ᴘɪᴄs---------------#

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://graph.org/file/e15701660c1edf9372117.jpg https://graph.org/file/f3beb7b86a3c2377b4378.jpg https://graph.org/file/e7d2481f061b1a49e74f0.jpg https://graph.org/file/2365944d148b74e6d1997.jpg https://graph.org/file/7629ab4f405aa927873f7.jpg https://graph.org/file/eab51b97cb42bcceed57a.jpg https://graph.org/file/73145b1a2b9be6e3aa55f.jpg https://graph.org/file/fa26792327c20e7cf2d09.jpg https://graph.org/file/0a853d08adaa779add51d.jpg https://graph.org/file/c5f952f87edd9bfa6da24.jpg https://graph.org/file/44a324098c0659733f8d7.jpg https://graph.org/file/272a244b58675b1d730a2.jpg https://graph.org/file/13b00b324008a295d5d6c.jpg https://graph.org/file/522087a01de3b04d08acc.jpg https://graph.org/file/3dd1217ccdd904acfd8de.jpg https://graph.org/file/01940fd3939ef490b1abc.jpg')).split()
HS_PICS = (environ.get('HS_PICS', 'https://graph.org/file/6dad69cbee10d97de02ff.jpg')).split()
JOIN_PICS = (environ.get('JOIN_PICS', 'https://graph.org/file/c886730e0a7608a768c8a.jpg')).split()
YT_PICS = (environ.get('YT_PICS', 'https://graph.org/file/02a10ffcb137fde6ee10a.jpg https://graph.org/file/2af71f046b5d65c42f3e7.jpg')).split()

#-------------ᴡᴇʟᴄᴏᴍᴇ ɪᴍᴀɢᴇ------------------#

MELCOW_IMG = environ.get('MELCOW_IMG',"https://te.legra.ph/file/35610b78fd5d031c2ec6a.jpg")

#------------ᴀᴅᴍɪɴs,ᴄʜᴀɴɴᴇʟ & ᴜsᴇʀs-----------#

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1426588906 1892306299').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001749649685').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

#------------ᴍᴏɴɢᴏ-ᴅʙ ɪɴғᴏʀᴍᴀᴛᴏɪɴ-----------#

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://girirajmeena30:girirajmeena30@cluster0.cl0y3pj.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "girirajmeena30")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

########------ʟᴏɢɪɴ-ᴄʜᴀɴɴᴇʟ-----#########

login_channel = environ.get('LOGIN_CHANNEL', '-1001970743839')
LOGIN_CHANNEL = int(login_channel) if login_channel and id_pattern.search(login_channel) else None

# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", False)
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

     #-------------------ᴏᴛʜᴇʀs----------------#

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001797791175'))
MSG_ALRT = environ.get('MSG_ALRT', '𝒉𝒔-𝒃𝒐𝒕...☄️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION) 
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

##---------------ᴇxᴛᴇʀ ғᴇᴀᴛᴜʀᴇs-----------------##

           # ᴅᴏᴡɴʟᴏᴀᴅ ᴛᴜᴛᴏʀɪᴀʟ ʙᴜᴛᴛᴏɴ #
HOW_TO_DOWNLOAD =  environ.get('HOW_TO_DOWNLOAD', 'https://t.me/Sharath_Links/13')
FILE_REQ_CHANNEL = int(environ.get('FILE_REQ_CHANNEL', LOG_CHANNEL))
     
               # ᴜʀʟ sʜᴏʀᴛ-ʟɪɴᴋ #
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'omegalinks.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '64d0231e85bf77018c452d58eab769a98f81626b')

      # ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ғᴏʀ ɢʀᴏᴜᴘ ᴏɴʟʏ (sᴇʟғ ᴅᴇʟᴇᴛᴇ) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

               # ʟᴀɴɢᴜᴀɢᴇ ғᴇᴀᴛᴜʀᴇ #
LANGUAGES = ["tamil", "malayalam", "english", "hindi", "telugu", "kannada"]
