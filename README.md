# 🌊 Projeto Aquavita — Missão de Monitoramento de Qualidade da Água

Script em Python para verificação automática dos parâmetros de qualidade da água (pH e temperatura) em um aquário ou sistema similar, utilizando Programação Orientada a Objetos.

## Sobre a Missão

O **Projeto Aquavita** tem como objetivo automatizar o monitoramento das condições da água em ambientes controlados (aquários, tanques de cultivo e sistemas de aquaponia), garantindo que pH e temperatura permaneçam dentro dos limites seguros para a saúde dos organismos aquáticos, com alertas automáticos em caso de desvio.

## Ambientes do Projeto

| Camada        | Finalidade                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| **develop**   | Ambiente de desenvolvimento local. Usado pela equipe para escrever e testar novas funcionalidades antes de qualquer validação formal. Dados fictícios/simulados. |
| **stage**     | Ambiente de homologação. Réplica do ambiente de produção usada para testes de integração e validação junto à equipe de biologia, antes do deploy final. Pode usar dados reais em modo de leitura ou sensores de teste. |
| **main**      | Ambiente de produção. Versão estável e validada, conectada aos sensores reais dos aquários/tanques. Qualquer alteração aqui impacta o monitoramento ao vivo. |

## Equipe Responsável

| Nome                  | Função                        |
|-----------------------|-------------------------------|
| Dra. Camila Rezende   | Bióloga responsável — parâmetros de qualidade da água |
| Dr. Rafael Nogueira   | Biólogo — saúde e bem-estar animal |
| Juliana Petit         | Desenvolvedora — backend e integração com sensores |
| Marcos Vinícius Alves | Desenvolvedor — infraestrutura e ambientes (develop/stage/main) |

> **Nota:** os nomes acima foram sugeridos como placeholders para fins de documentação. Substitua pelos nomes reais da equipe do projeto.

## Descrição

A classe `ControleQualidadeAgua` encapsula os dados de pH e temperatura da água como atributos privados (usando o prefixo `__`, que aciona o *name mangling* do Python) e oferece um método para verificar se esses valores estão dentro dos limites considerados ideais.

## Estrutura da Classe

### `__init__(self, ph, temperatura)`
Construtor que inicializa o objeto com os valores de pH e temperatura informados.

- `self.__ph`: nível de pH da água (atributo privado)
- `self.__temperatura`: temperatura da água em °C (atributo privado)

### `verificar_parametros(self)`
Verifica se os parâmetros estão dentro dos limites seguros:

| Parâmetro    | Limite mínimo | Limite máximo |
|--------------|---------------|---------------|
| pH           | 6.8           | 7.6           |
| Temperatura  | 22.0 °C       | 28.0 °C       |

- Se o **pH** estiver fora da faixa, exibe um alerta e retorna `False`.
- Se a **temperatura** estiver fora da faixa, exibe um alerta e retorna `False`.
- Se ambos estiverem dentro da faixa, exibe uma mensagem de status positivo e retorna `True`.

## Exemplo de Uso

```python
meu_aquario = ControleQualidadeAgua(7.0, 25.0)
resultado = meu_aquario.verificar_parametros()
print(f"Está tudo dentro do limite? {resultado}")
```

## ⚠️ Atenção: bug no código de teste original

No trecho de teste fornecido, há uma linha que **vai gerar erro** ao ser executada:

```python
status_ok, mensagem = meu_aquario.verificar_parametros()
```

O método `verificar_parametros()` retorna **apenas um valor booleano** (`True` ou `False`), não uma tupla com duas posições. Tentar desempacotar um `bool` em duas variáveis (`status_ok, mensagem`) resulta em:

```
TypeError: cannot unpack non-iterable bool object
```

### Como corrigir

Existem duas abordagens possíveis, dependendo do que você deseja:

**Opção 1 — Usar apenas o retorno booleano (mais simples):**
```python
status_ok = meu_aquario.verificar_parametros()
print(f"Está tudo dentro do limite? {status_ok}")
```

**Opção 2 — Fazer o método retornar uma tupla `(bool, str)`:**
```python
def verificar_parametros(self):
    if self.__ph < 6.8 or self.__ph > 7.6:
        msg = "ALERTA QA: Nível de pH fora do limite ideal!"
        print(msg)
        return False, msg

    if self.__temperatura < 22.0 or self.__temperatura > 28.0:
        msg = "ALERTA QA: Temperatura fora do limite seguro!"
        print(msg)
        return False, msg

    msg = "STATUS: Parâmetros da água em níveis ideais."
    print(msg)
    return True, msg
```

Com a Opção 2, a linha original de desempacotamento (`status_ok, mensagem = ...`) passa a funcionar corretamente.

## Requisitos

- Python 3.x (não requer bibliotecas externas)

## Como executar

```bash
python controle_qualidade_agua.py
```
