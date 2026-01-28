# Cybersecurity Log Monitoring
Projeto simples para simular atividades de um Analista de Segurança em um SOC,
com foco na análise de logs de autenticação em ambientes Linux.

## Objetivo
Identificar tentativas suspeitas de acesso, como possíveis ataques de força bruta,
a partir da análise de logs de autenticação.

## Tecnologias
- Linux
- Python

## Funcionamento
O script lê o arquivo `auth.log`, identifica tentativas de login falhas e gera alertas
quando um mesmo IP ultrapassa o limite definido.

## Execução
python3 log_analyzer.py


### Autor
Matheus Nascimento
