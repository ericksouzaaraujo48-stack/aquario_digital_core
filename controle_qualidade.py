class ControleQualidadeAgua:
    def __init__(self, ph, temperatura):
        # Declarando as variáveis como "privadas" usando __
        self.__ph = ph
        self.__temperatura = temperatura

    def verificar_parametros(self):
        if self.__ph < 6.8 or self.__ph > 7.6:
            print("ALERTA QA: Nível de pH fora do limite ideal!")
            return False
            
        if self.__temperatura < 22.0 or self.__temperatura > 28.0:
            print("ALERTA QA: Temperatura fora do limite seguro!")
            return False
            
        print("STATUS: Parâmetros da água em níveis ideais.")
        return True
    # O seu código da classe fica aqui em cima...

# 1. Criando um aquário de teste com pH 7.0 e temperatura 25.0
meu_aquario = ControleQualidadeAgua(7.0, 25.0)

# 2. Chamando o método e desempacotando a tupla nas variáveis
status_ok, mensagem = meu_aquario.verificar_parametros()

# 3. Mandando imprimir na tela para você conseguir ver
print(f"Está tudo dentro do limite? {status_ok}")
print(f"Mensagem do sistema: {mensagem}")