# API-DJANGO
 I'm training my skills with Django 
# Resolução Do Teste Técnico - Desenvolvedor Frontend 

Este repositório contém a resolução do teste técnico de desenvolvimento fornt-end. Para mais informações sobre o teste, clique <a href="https://github.com/PEAL-26/frontend-development-testing">aqui</a>

## Imagens após a conclusão do projecto
<img width=100% src="https://utfs.io/f/1b4985e0-6bab-4315-bcf6-2117c79b7ee7-1tn2lb.jpg"/>

<img width=100% src="https://utfs.io/f/dec7161f-e86a-42d0-8415-d50fee859e2f-1tn2lc.jpg"/>

## Técnologias Utilizadas
* [Node](https://nodejs.org/en)
* [Next](https://nextjs.org/)
* [Tailwind](https://tailwindcss.com/)
* [Mantine UI](https://ui.mantine.dev/)
* [TanStack Query](https://tanstack.com/query/latest)
* [PNPM](https://pnpm.io/installation)

## Requisitos para rodar o projecto:

### Setup de ambiente: 
- Node versão - <a href="https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi">LTS</a>
- pnmp (Gerenciador de pacotes que foi utilizado no projecto)

## Como rodar o projeto? ✅

1 - Clone o repositório

```
git clone https://github.com/afonsodasilva1/Resolucao-Teste-Tecnico-Desenvolvimento-Frontedn.git
```

2 - Rode o seguinte comando para instalar todas as dependências necessárias: 
```
pnpm install
```

3 - Rode o seguinte comando para subir a API Fake criada: 
```
pnpm json-server -p 3333 server.json
```
4 -  E por fim, rode o seguinte código:
```
pnpm run dev
```

## Como me localizar no projecto?

- `./src`: src ou source  é a pasta onde estão os arquivos de configuração e outras pastas
- `./src/app/pages`: Pasta onde estão as páginas da aplicação
- `./src/app/api`: Pasta onde tem a base url da api
- `./src/app/components`: Pasta onde conntém os componenetes reutilizáveis, ou seja que serão usados várias vezes na aplicação
- `./src/app/@type`: Pasta onde contém as interfaces utilizadas na aplicação
- `./src/app/assets`: Pasta onde contém os arquivos de mídias utilizadas na aplicação
- `./src/app/providers`:  Pasta onde tem os providers da aplicação

## ⚠️ Problemas enfrentados

### Problema 1:
Tive problema em usar biblioteca de componentes prontos  chamada Mantine UI
* Como solucionar:  Decidi criar os meus próprios componentes. Achei melhor porque quando criamos os nossos próprios componentes, temos melhor controle das propriedades e estilização, tornando mais flexível e escaláve. Os componentes prontos ja vêm com uma estilização padrão e muitas das vezes fica difícil tirar ou extender a essa estilização


