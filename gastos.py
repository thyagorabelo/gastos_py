
def read_gastos_data(filename):
    mes = filename.removesuffix(".txt")
    gastos = {}
    
    # ADICIONADO: encoding="utf-8" para ler acentos corretamente
    with open(filename, "r", encoding="utf-8") as file:
        for linha in file:
            if ":" in linha:
                categoria, valor_str = linha.split(":", 1)
                # Limpeza de R$, pontos de milhar e troca de vírgula por ponto
                valor_limpo = valor_str.strip().replace("R$", "").replace(".", "").replace(",", ".")    
                try:
                    gastos[categoria.strip()] = float(valor_limpo)
                except ValueError:
                    continue 
 
    return mes, gastos


