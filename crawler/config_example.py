from utils import generate_queries, key_words

config = {
  # Configuração da região da coleta -> Formato: ISO 3166-1 alpha-2
  'region_code': 'US',         

  # Configuração da linguagem da coleta -> Formato: ISO 639-1   
  'relevance_language': 'en',     

  # A coleta ocorre da data final para a data inicial -> [ano, mês, dia]
  'start_date': [2015, 1, 1], 
  'end_date': [2025, 5, 31],

  # API que receberá uma requisição PATCH com payload de um JSON contendo informações acerca da coleta
  # Mantenha uma string vazia '' Caso não tenha configurado
  'api_endpoint': '',
  # Intervalo, em segundos, entre cada envio de dados para a API
  'api_cooldown': 60,                                                   

  # Intervalo, em segundos, entre cada tentativa de requisição para a API apos falha
  'try_again_timeout': 60,                                              

  # Palavras que serão utilizadas para filtrar os títulos dos vídeos
  'key_words': key_words,
  
  # KEYs da API v3 do YouTube
  'youtube_keys': [],

  # Queries que serão utilizadas na pesquisa
'queries': generate_queries()
}