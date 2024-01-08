# WebScraping - Fundamentus

Este projeto tem como objetivo realizar Web Scraping no site Fundamentus, uma plataforma online que fornece informações financeiras e fundamentais de empresas e fundos imobiliários listados na B3.

## ETL - Extração, Transformação e Carga
O projeto implementa um processo ETL para coletar dados da plataforma Fundamentus. Esse processo inclui:

- **Extração**: Coleta de dados brutos diretamente do site.
- **Transformação**: Processamento e limpeza dos dados extraídos para prepará-los para análise.
- **Load**: Carregamento dos dados transformados em um formato adequado, como um banco de dados ou arquivo.

## Tecnologias Utilizadas:

- **Python** (`^3.12`): Linguagem de programação principal para o desenvolvimento do projeto.
- **Requests** (`^2.31.0`): Biblioteca para realizar solicitações HTTP durante o processo de scraping.
- **Sqlalchemy** (`^2.0.25`): Ferramenta SQL para interagir com bancos de dados relacionais.
- **PyODBC** (`^5.0.1`): Driver ODBC para se conectar a bancos de dados.
- **Pandas** (`^2.1.4`): Biblioteca para manipulação e análise de dados.
- **Beautiful Soup (bs4)** (`^0.0.1`): Biblioteca para extrair dados HTML e XML.