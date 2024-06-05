import re
def get_calculo(expression):
    """
    Recebe uma string contendo uma expressão matemática simples e retorna o resultado.
    """
    try:
        # Substituir palavras por símbolos matemáticos
        expression = re.sub(r'^\s*box\s*', '', expression.lower())
        expression = expression.lower()
        expression = expression.replace("x", "*")
        expression = expression.replace("dividido por", "/")
        expression = expression.replace("dividido", "/")  

        # Utilizar uma expressão regular para identificar e substituir operações matemáticas básicas
        expression = re.sub(r'[^0-9+\-*/(). ]', '', expression)
        result = round(eval(expression),2)
        return f"O resultado da operação {expression} é {result}."
    except Exception as e:
        return f"Erro ao calcular a operação: {str(e)}"