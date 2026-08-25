# Error Handling

def operar(a, b):
    
    try:
        return a/b
    except TypeError as variavel: #Ha varios tipos de erros
        print("Erro", variavel)
        
    except (ZeroDivisionError, ArithmeticError) as variavel: #Ha varios tipos de erros
        print("Erro 2", variavel)
    else: #Executado somente se NENHUM erro acontecer dentro do bloco try
        print("Obrigada")
    finally: #Executado SEMPRE, independentemente de ter ocorrido erro ou não, e mesmo se o código tiver um return
        print("Acabou")
        
print(operar(1,0))

#Outros usos do try-except-finally:
#-finally: fechamentos de conexões com o banco de dados e de arquivos
#-raise
