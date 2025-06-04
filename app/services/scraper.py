import requests
from bs4 import BeautifulSoup

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

def scrape_data(ano: int, categoria: str, subcategoria: str):
    params = {
        "ano": ano,
        "opcao": f"opt_0{categoria}",
        "subopcao": f"subopt_0{subcategoria}"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    if not table:
        raise ValueError("Tabela não encontrada na página.")
    data = []
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    for row in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all("td")]
        if cells:
            data.append(dict(zip(headers, cells)))
    return data