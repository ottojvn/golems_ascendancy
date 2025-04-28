# Golems Ascendancy

Golems Ascendancy é uma simulação de construção e gerenciamento de golems em um mundo fantástico. Ele permite controlar recursos, produzir golems de diferentes materiais e evoluir sua colônia ao longo do tempo, com suporte completo a múltiplos idiomas via i18n.

## Objetivo
Desenvolver um protótipo flexível e modular onde:
- A lógica de jogo (estado, data, recursos e população) está separada da interface.
- Toda string de interface é traduzível, centralizada em `interface/i18n.py`.
- A estrutura de pastas facilita a manutenção e evolução do projeto.

## Estrutura do Repositório
```
golems_ascendancy/
├── game/                 # Lógica de jogo (estado, data, constantes, enums)
├── interface/            # Camada de apresentação (painéis, elementos, i18n, assets)
├── main.py               # Ponto de entrada da aplicação
├── requirements.txt      # Dependências do Python
└── README.md             # Documentação do projeto
```

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/golems_ascendancy.git
   ```
2. Acesse a pasta:
   ```bash
   cd golems_ascendancy
   ```
3. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

```bash
python main.py
```

Use o mouse para interagir e pressione ESC para sair.

## Internacionalização (i18n)
Todas as strings de UI estão em `interface/i18n.py`. Para adicionar ou ajustar idiomas:
1. Insira ou altere as chaves em `TRANSLATIONS`.
2. Ajuste `cfg['locale']` no arquivo de configuração (`interface/config.py`).

## Convenções de Commit
Usamos [Conventional Commits](https://www.conventionalcommits.org/) para manter histórico claro e organizado.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.