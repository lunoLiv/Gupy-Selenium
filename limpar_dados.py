import re

def limpar_dados(dados,empresa):
    lista = re.findall(r'<li data-testid="job-list__listitem" class="sc-f5007364-2 euwBIb">(.*?)</li>', dados)

    jobs = []
    for i in lista:
        
        link  = re.findall(r'href="(.*?)\?', i)
        nome  = re.findall(r'sc-f5007364-4 [a-zA-Z0-9]{6}">(.*?)<', i)
        local = re.findall(r'KCtRP">(.*?)<', i)
        tempo = re.findall(r'gIgRzt">(.*?)<', i)

        dados_do_trabalho = [f'https://{empresa}.gupy.io{link[0]}',nome[0],local[0],tempo[0]]
        jobs.append(dados_do_trabalho)
    
    return jobs
    


