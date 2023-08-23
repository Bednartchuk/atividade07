class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
    
    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario
    
    def exibir(self):
        base_info = super().exibir()
        return f"{base_info}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data
    
    def exibir(self):
        base_info = super().exibir()
        return f"{base_info}, Data: {self.data}"

documento = Documento("Documento Geral", "Este é um documento genérico.")
print(documento.exibir())

email = Email("Assunto importante", "Conteúdo confidencial", "remetente@example.com", "destinatario@example.com")
print(email.exibir())

relatorio = Relatorio("Relatório Mensal", "Aqui estão os resultados do mês", "2023-08-22")
print(relatorio.exibir())
