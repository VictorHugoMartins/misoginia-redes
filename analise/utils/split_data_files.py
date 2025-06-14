import pandas as pd
import os

# Função para remover duplicatas e manter os registros mais recentes
def remove_duplicates(df, id_column, date_column):
    # Ordena por data de forma decrescente e remove duplicatas mantendo o mais recente
    df_sorted = df.sort_values(by=date_column, ascending=False)
    df_unique = df_sorted.drop_duplicates(subset=id_column, keep='first')
    return df_unique

# Função para dividir o arquivo CSV em arquivos menores de 10.000 registros, após remover duplicatas
def split_csv(csv_file, output_dir, id_column, date_column, chunk_size=10000):
    # Criar o diretório de saída, se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ler o arquivo CSV em pedaços e remover duplicatas em cada pedaço
    df_iterator = pd.read_csv(csv_file, chunksize=chunk_size)
    
    # Para cada pedaço de 10.000 registros, remover duplicatas e salvar como novo CSV
    for i, chunk in enumerate(df_iterator):
        # Remove duplicatas mantendo os mais recentes
        chunk_cleaned = remove_duplicates(chunk, id_column, date_column)
        
        output_file = os.path.join(output_dir, f'lote_{i + 1}.csv')
        chunk_cleaned.to_csv(output_file, index=False)
        print(f"Lote {i + 1} salvo em: {output_file}")