def saluta(nome: str) -> str:
    """Restituisce un saluto personalizzato."""
    return f"Ciao, {nome}! Benvenuto nel tuo primo pacchetto Python."

def saluta_lista(nomi: list) -> list:
    """Restituisce una lista di saluti."""
    return [saluta(nome) for nome in nomi]
