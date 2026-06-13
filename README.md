# ChargeGrid Intelligence - Gestão Automatizada de Eletropostos

## Integrantes
| Nome | RM |
| :--- | :--- |
| Enzo Seiji Delgado Tabuchi | 573156 |
| Henrique Almeida Lucareli | 569183 |
| Leonardo Scotti Tobias | 573305 |
| Luca Almeida Lucareli | 569061 |
| Natan Silva da Costa | 573100 |

---

## Prova de Conceito (PoC) — Sprint 2

Para esta sprint, desenvolvemos uma **Simulação Computacional e Preditiva Baseada em Dados Reais** (usando Python), que demonstra o motor de tomada de decisão do ChargeGrid operando sob os princípios de eficiência energética e sustentabilidade.

### Funcionalidade Operacional Demonstrada:
* **Controle Dinâmico de Demanda:** O sistema monitora a carga do edifício em tempo real e, ao detectar a proximidade do horário de pico, reduz dinamicamente a potência injetada no carregador GoodWe GW7K-HCA-20 (de 7kW para 3.5kW), evitando multas contratuais e quedas de energia.
* **Simulação de Tarifação Ociosa:** Monitoramento do fim da carga com simulação de gatilho para liberação da cancela ou aplicação de taxa de ociosidade.

### Arquitetura da Solução e Fluxo de Dados
1. **Telemetria (MODBUS/OCPP):** Coleta os dados em que o prédio consume e o status do carregador.
2. **Processamento (Python):** Algoritmo para analisar o limite de demanda e calcula o "Smart Charging".
3. **Persistência (SQL):** Armazenamento do histórico de sessões para alimentar umaa futura IA preditiva.

---

## Sustentabilidade e Fundamentação SERS

Nossa solução aplica diretamente os conceitos de **Soluções Em Energias Renováveis e Sustentáveis (SERS)** através de três pilares:

1. **Gerenciamento do Lado da Demanda (DSM):** Evitamos o estresse da rede elétrica pública em horários de pico comercial, achatando a curva de consumo sem a necessidade de obras civis ou sobredimensionamento de cabos.
2. **Sincronização Fotovoltaica:** O algoritmo prioriza o carregamento de alta potência nos momentos de pico de geração solar (calculados via irradiação local), garantindo que a matriz do abastecimento seja predominantemente limpa.
3. **Eficiência Operacional:** A penalização por ociosidade de vaga aumenta a rotatividade do eletroposto, permitindo que mais veículos elétricos sejam carregados por dia no mesmo espaço urbano.

---

## Tecnologias
* **Core Engine & Simulação:** Python 3.x (Bibliotecas: Pandas, NumPy, Time)
* **Banco de Dados:** MySQL (Estruturação das tabelas de logs de recarga)
* **FrontEnd:** React/JS (Mockups de interface de monitoramento)
* **BackEnd (Target):** NestJS / GoLang
