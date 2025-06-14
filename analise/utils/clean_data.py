import nltk
import re
import ftfy
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

# Downloads necessários do NLTK
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('punkt')

# Inicializar stemmer e stopwords em português
stemmer = RSLPStemmer()
stop_words = set(stopwords.words('portuguese'))

# Função para aplicar stemming (radicalização)
def aplicar_stemming(texto):
    palavras = texto.split()
    palavras_stemmizadas = [stemmer.stem(palavra) for palavra in palavras]
    return ' '.join(palavras_stemmizadas)

# Função para limpar o texto, mantendo hashtags, emojis e menções
def limpar_texto(texto):
    texto = str(texto)
    texto = ftfy.fix_text(texto)  # Corrige erros de codificação
    texto = re.sub(r'k{2,}', '', texto)  # Remove sequência de "kkk"
    texto = re.sub(r'\bRT\b', '', texto, flags=re.IGNORECASE)  # Remove "RT"
    texto = re.sub(r'\d+', '', texto)  # Remove números
    texto = re.sub(r'\s?:\s?', ' ', texto)  # Remove ":"
    texto = re.sub(r'[^\w\s#@🙂-🙿]', '', texto)  # Mantém hashtags, menções e emojis
    texto = texto.lower()  # Converte para minúsculas
    return texto

# Função para remover stopwords
def remover_stopwords(texto):
    if isinstance(texto, str):
        return ' '.join([palavra for palavra in texto.split() if palavra.lower() not in stop_words])
    return texto

# Função principal de limpeza
def limpar_dados(df, coluna_id, coluna_texto):
    print("Removendo duplicatas...")
    df = df.sort_values(by='published_at', ascending=False).drop_duplicates(subset=coluna_id, keep='first')

    print("Limpando texto...")
    df[coluna_texto] = df[coluna_texto].apply(limpar_texto)

    print("Removendo stopwords...")
    df[coluna_texto] = df[coluna_texto].apply(remover_stopwords)

    print("Aplicando stemming...")
    df[coluna_texto] = df[coluna_texto].apply(aplicar_stemming)

    print("Removendo linhas vazias...")
    df.dropna(subset=[coluna_texto], inplace=True)
    df = df[df[coluna_texto].str.strip() != '']

    if coluna_texto == 'text':
        print("Filtrando por tamanho mínimo do texto...")
        df = df[df[coluna_texto].apply(lambda x: len(x) > 25)]

    return df
