print(12, 34, sep=';', end='##\n') #sep = separator / end = final da linha
print(12, 34, sep=';', end='##') #sep = separator / end = final da linha

"""
    * Operadores não nomeados são passados pela posição
    
    Ex:
    
    def saudacao(nome, idade):
    print(f"{nome} tem {idade} anos")

    saudacao("Ana", 25)  # "Ana" vai para nome, 25 vai para idade

    A ordem portanto importa, se invertermos, dará errou ou mudará o resultado.
    
    * Já os nomeados indicam o nome do parâmetro.
    
    EX:
    
    saudacao(idade=25, nome="Ana")  # a ordem não importa aqui
    
    Podemos até combinar ambos, porém os nomeados devem vir primeiro
"""