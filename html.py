import statistics
import myfunction
import gastos
def produce_bar_chart(fn):
    mes, gasto = gastos.read_gastos_data(fn)
    
    if not gasto:
        return None

    valores = list(gasto.values())
    valor_maximo = max(valores)
    media = round(statistics.mean(valores), 2)
    
    titulo = f"Relatório de gastos: {mes}"
    
    # HTML com meta tag UTF-8 para o navegador exibir acentos
    header = f"""<!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="UTF-8">
                        <title>{titulo}</title>
                    </head>
                    <body style="font-family: sans-serif; padding: 20px;">
                        <h3>{titulo}</h3>"""
    body = ""
    
    for nome, valor in gasto.items():
        largura_barra = myfunction.convert2range(valor, 0, valor_maximo, 0, 350)
        body += f"""
                <div style="margin-bottom: 10px; display: flex; align-items: center;">
                    <div style="width: 150px;"><strong>{nome}:</strong></div>
                    <svg height="20" width="360" style="margin-right: 10px;">
                        <rect height="20" width="{largura_barra}" style="fill:royalblue;" />
                    </svg>
                    <span> R$ {valor:,.2f}</span>
                </div>"""
                
    footer = f"""
                        <hr style="width: 550px; margin-left: 0;">
                        <p><strong>Média Geral:</strong> R$ {media:,.2f}</p>
                    </body>
                </html>"""
    
    pagina = header + body + footer
    caminho_salvamento = f"{fn.removesuffix('.txt')}.html"
    
    # ADICIONADO: encoding="utf-8" para salvar o arquivo com acentos
    with open(caminho_salvamento, "w", encoding="utf-8") as sf:
        sf.write(pagina)

    return caminho_salvamento