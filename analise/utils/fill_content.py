import os
import pandas as pd
from tqdm import tqdm
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import re

execution = 'local'
# execution = 'cloud'

base_path = 'data' if execution == 'local' else 'cloud'
country = 'palestine'

# Função para obter a transcrição pela youtube_transcript_api
def get_transcription(id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id, languages=['en'])  # Ajuste idiomas, se necessário
        transcription_text = " ".join([entry['text'] for entry in transcript])
        return transcription_text
    except Exception:
        return None

# Função principal para buscar transcrições ou legendas e adicionar ao DataFrame
def add_transcriptions_to_df(df_videos, ids, column='video_id'):
    errors = 0  # Contador de erros

    for video_id in tqdm(ids, desc="Processando vídeos"):
        # Se já houver texto na linha correspondente, mantém o existente
        existing_text = df_videos.loc[df_videos[column] == video_id, 'text'].values
        if existing_text.size > 0 and pd.notna(existing_text[0]):
            continue  # Pula para o próximo vídeo

        # Caso contrário, busca a transcrição
        transcription_text = get_transcription(video_id)

        # Atualiza o DataFrame ou conta o erro
        if transcription_text:
            df_videos.loc[df_videos[column] == video_id, 'text'] = transcription_text
        else:
            errors += 1

    return df_videos, errors

# Carregar disfluências do arquivo
def load_disfluencies(file_path):
    with open(file_path, 'r') as file:
        disfluencies = file.read().splitlines()
    # Criar a expressão regular unindo as disfluências com '|'
    return r'\b(' + '|'.join(re.escape(word) for word in disfluencies) + r')\b'

# Função para remover disfluências
def remove_disfluencies(text, disfluencies_pattern):
    try:
        if text is None:
            return text
        # Remove as disfluências usando a expressão regular
        clean_text = re.sub(disfluencies_pattern, "", text, flags=re.IGNORECASE)
        # Remove espaços extras
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        return clean_text
    except:
        return text

def fill_videos(df, column='video_id'):
    # Atualiza o DataFrame com as transcrições ou legendas
    remaining_videos = df[df['text'].isnull()][column].unique()

    # Exibe a quantidade de vídeos restantes e o total de vídeos
    total_videos = len(df)
    remaining_count = len(remaining_videos)
    print(f"Total de vídeos: {total_videos}")
    print(f"Vídeos restantes para processar: {remaining_count}")

    # Adiciona as transcrições ou legendas com barra de progresso
    df, error_count = add_transcriptions_to_df(df, remaining_videos, column)

    # Exibe o total de erros no final
    print(f"Erro ao obter {error_count} transcrições")
    print(f"Cleaning disfluencies...")
    
    # # Carregar a lista de disfluências
    # disfluencies_file = 'disfluencies.txt'
    # disfluencies_pattern = load_disfluencies(disfluencies_file)

    # # Aplicar a função de limpeza na coluna 'text'
    # df['text'] = df['text'].apply(lambda x: remove_disfluencies(x, disfluencies_pattern))
    
    return df
