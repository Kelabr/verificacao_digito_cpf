# Verificador de dígitos verificadores de CPF
|![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)|
| ------------------------------------------|-----------------------------------------|


## Descrição
Essa aplicação tem como foco introduzir uma validação prévia e mínima, visando  verificar os dígitos verificadores de qualquer CPF.

Construir esse script em python devido a uma pauta que foi levantada sobre criptografia e validação de dados no curso de ciber segurança que estou fazendo. Percebi que algumas aplicações não tem o mínimo de validação, em questão ao CPF, para descobri se no mínimo ele realmente é válido. Pesquisei por dois minutos sobre "como verificar os dígitos verificadores de um cpf" e bum, estava lançada a ideia e depois de meia hora de código estava pronto o script
## Referencia
Tive como referencia esse [post]([https://www.campuscode.com.br/conteudos/o-calculo-do-digito-verificador-do-cpf-e-do-cnpj](https://www.campuscode.com.br/conteudos/o-calculo-do-digito-verificador-do-cpf-e-do-cnpj)) no site campuscode.com.br. Ele me deu o algoritmo/calculo para efetuar a verificação dos CPFs
## Instruções 
- Versão do Python usado: `Python 3.13.4`
- Substitua o valor da variável `cpf`  pelo valor do CPF que deseja verificar (sem pontos ou traços)
- Após preencher a variável `cpf` inicie o script rodando o comando `python main.py` no terminal
## Saídas
```
Digitos invalidos!! :(
1° Digito (correto) : x
2° Digito (correto) : x`

Quando não há  erro nos dígitos:
Digitos validos!! :)`
1° Digito: x
2° Digito: x


