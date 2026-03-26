## APS - Testes Automatizados e Adequação de Testes

Este repositório contém a suíte de testes automatizados para o sistema `Scholarship Eligibility Evaluator`.

## Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Framework de Testes:** pytest

## Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Para instalar o framework de testes, execute o seguinte comando no terminal:
```bash
pip install pytest
```

## Como executar os testes
1. Abra o terminal na pasta onde os arquivos `scholarship.py` (código-fonte) e `test_scholarship.py` (suíte de testes) estão localizados.
2. Execute o comando principal abaixo para rodar toda a suíte de testes com o detalhamento das saídas:

```bash
pytest test_scholarship.py -v
```

Ao final da execução, o terminal exibirá o status de todos os testes (passaram ou falharam) e a porcentagem de conclusão.