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
        # Verificar se há tentativa de divisão por zero
        if re.search(r'/\s*0\b', expression):
            return "Divisão por 0 é inválida."
        result = round(eval(expression),2)
        expression = expression.replace("*", "vezes")
        
        return f"{expression} é {result}."
    except Exception as e:
        return "Erro ao calcular a operação"