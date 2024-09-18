# 💰 Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python, como parte dos desafios do Bootcamp Python DIO. O sistema permite criar usuários, contas correntes, realizar depósitos, saques e exibir extratos, além de listar todas as contas cadastradas.


![Demonstração do Sistema Bancario](https://github.com/SamilMoret/sistema_bancario/blob/main/sistema__bancario_vi2.gif)

## 🚀 Funcionalidades

- **Criar Usuário**: Registra um novo usuário no sistema com nome, CPF, data de nascimento e endereço.
- **Criar Conta Corrente**: Cria uma nova conta corrente associada a um usuário existente.
- **Depositar**: Permite realizar depósitos em uma conta corrente.
- **Sacar**: Realiza saques dentro de um limite diário e valor máximo por saque.
- **Extrato**: Exibe o extrato de todas as movimentações (depósitos e saques) de uma conta.
- **Listar Contas**: Mostra todas as contas cadastradas com informações detalhadas (agência, número da conta, nome e CPF do titular).

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.

## 📦 Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd sistema_bancario_python
   ```
3. **Execute o arquivo principal:**

   Se você tiver Python instalado, basta rodar o script no terminal:

   ```bash
   python sistema_bancario.py
   ```
4. **Siga as instruções no console para utilizar as funcionalidades do sistema.**

## 📝 Como Usar
   Ao rodar o programa, você verá o seguinte menu no terminal:
```
   Bem-vindo ao Banco!
[1] Criar Usuário
[2] Criar Conta Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar Contas
[7] Sair
Escolha uma operação:
```
### Exemplos de Uso:
    
- **Criar um novo usuário**: Escolha a opção `1` e insira os dados solicitados, como nome, CPF, data de nascimento, endereço, etc.
- **Criar uma conta corrente**: Escolha a opção `2` e informe o CPF do usuário já cadastrado.
- **Depositar e Sacar**: Para depositar, escolha a opção `3`, insira o valor e o sistema atualizará o saldo. Para sacar, escolha a opção `4` e insira o valor, respeitando o limite diário de 3 saques.
- **Exibir Extrato**: Para visualizar o extrato de transações da conta, escolha a opção `5`.
- **Listar Contas**: Para listar todas as contas cadastradas no sistema, escolha a opção `6`.

## 📚 Estrutura do Código

O código foi organizado em funções para melhorar a modularidade:

- **`deposito`**: Função para realizar depósitos, recebe argumentos por posição.
- **`saque`**: Função para realizar saques, recebe argumentos por nome.
- **`exibir_extrato`**: Função que exibe o extrato, recebendo argumentos por posição e nome.
- **`criar_usuario`**: Cadastra um novo usuário, validando o CPF para evitar duplicações.
- **`criar_conta`**: Cria uma conta corrente vinculada a um usuário existente.
- **`listar_contas`**: Lista todas as contas cadastradas com detalhes.

---
## 🧑‍💻 Feito por:
Samil Moret

[![LinkedIn](https://img.icons8.com/color/48/linkedin.png)](https://www.linkedin.com/in/samilmoret/)
[![WhatsApp](https://img.icons8.com/color/48/whatsapp--v1.png)](https://linkwhats.app/f27e11)







 



