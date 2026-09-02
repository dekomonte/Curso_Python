import pymssql
import os

#Atualizaçao (com verificacao antes)
def atualizar_banco_dados(dado1, dado2, dado3):
    
    conn = pymssql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )
    
    cursor = conn.cursor()
    
    try:
       
        query_consultar = '''
            SELECT 1 FROM tabela 
            WHERE id1 = %s 
              AND id2 = %s 
              AND id3 = %s
        '''
        
        parametros_busca = (dado1, dado2, dado3)
        
        cursor.execute(query_consultar, parametros_busca)
        registro_existente = cursor.fetchone()
        
        # Organiza dados em um dicionario      
        dados = {
            'id1': dado1,
            'id2': dado2,
            'id3': dado3
        }
        
        # Trata strings vazias convertendo para None (NULL no SQL Server) (Gemini)
        dado_processado = {key: (value if value != '' else None) for key, value in dados.items()}
        
        if not registro_existente:
            
            colunas = ', '.join(dado_processado.keys())
            valores_placeholders = ', '.join(['%s'] * len(dado_processado))
            
            query_insert = f"INSERT INTO tabela ({colunas}) VALUES ({valores_placeholders})"
            valores_insercao = tuple(dado_processado.values())
            
            cursor.execute(query_insert, valores_insercao)
            conn.commit()
            
    finally:
        cursor.close()
        conn.close()
 
