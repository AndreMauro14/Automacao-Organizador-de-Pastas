# Organizador automático de Pastas

A pasta **Downloads** sempre vira bagunça: PDF misturado com imagens, instaladores, `.zip` e vários outros tipos de arquivos tudo no mesmo lugar. Com o tempo, eu comecei a perder muito tempo tentando achar um arquivo específico no meio de dezenas de downloads recentes. Esse projeto nasceu exatamente dessa dor: a dificuldade em encontrar arquivos importantes na minha própria máquina.

Para resolver isso, criei uma automação em **Python** que organiza automaticamente a pasta Downloads, separando os arquivos por extensão em subpastas (por exemplo: `pdf`, `jpg`, `exe`, `zip`, `iso` etc.). Assim, em vez de ficar caçando arquivo manualmente, basta abrir a pasta da extensão correspondente e o arquivo já está lá, no lugar certo.

## Como funciona

- Lê todos os arquivos da pasta atual (onde o script está sendo executado).
- Ignora o próprio arquivo `.py`, para não ser movido.
- Identifica a extensão de cada arquivo.
- Cria automaticamente uma pasta para cada extensão encontrada (se ainda não existir).
- Move cada arquivo para a pasta da sua respectiva extensão, organizando tudo de forma automática.

Também criei um segundo script que faz o caminho inverso: ele entra em cada subpasta, pega os arquivos e move de volta para a pasta Downloads, caso eu queira desfazer a organização ou reestruturar tudo de novo.

## Tecnologias utilizadas

- **Linguagem:** Python  
- **Biblioteca padrão:** `os` (para listar arquivos, criar pastas, montar caminhos e mover arquivos).
