import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

API_KEYS = [
    os.getenv('YOUTUBE_API_KEY_1'),
    os.getenv('YOUTUBE_API_KEY_2'),
    os.getenv('YOUTUBE_API_KEY_3'),
    os.getenv('YOUTUBE_API_KEY_4'),
    os.getenv('YOUTUBE_API_KEY_5'),
    os.getenv('YOUTUBE_API_KEY_6'),
    os.getenv('YOUTUBE_API_KEY_7'),
    os.getenv('YOUTUBE_API_KEY_8'),
    os.getenv('YOUTUBE_API_KEY_9'),
]

NEWS_API_KEYS = [
    os.getenv('NEWS_API_KEY_1'),
]

OPENAI_KEYS = [
    os.getenv('NEWS_API_KEY_1'),
]

OPENAI_KEY = os.getenv('NEWS_API_KEY_1')

result_index = '2025_06_10'

key_words = []
    # 'terrorists', 'massacre', 'attack', 'october', 'jihad', 'terror', 'isis',
    # 'antisemitic', 'captors', 'kidnap', 'zion', 'settler', 'occupy', 'occupation',
    # 'bombardment', 'siege', 'genocide', 'aggression', 'displace',
#     'ceasefire', 'israeli', 'palestinian', 'trump', 'ceasefire', 'intifada', 'two state',
#     "israel", "palestine", 'hamas', 'gaza', 'west bank', 'netanyahu'
# ]