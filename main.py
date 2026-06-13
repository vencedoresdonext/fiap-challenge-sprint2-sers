import time
import random

print("=== CHARGEGRID INTELLIGENCE - INICIANDO POC SPRINT 2 - SIMULAÇÃO ===")
print("Conectando ao EV Charger GoodWe GW7K-HCA-20 via Modbus/TCP... [OK]") # imaginando
print("Conectando ao sistema de telemetria predial... [OK]\n") # imaginando tmb

limite_contratado_kw = 50.0  # limite máximo do prédio
potencia_carregador_atual = 7.0 # potência máxima (7kW)

# ele funciona das 8h as 23h
# pegando a hora mais aproximada qaundo roda o código
for hora in range(8, 23):
# o consumo do prédio varia dependendo do horário (pico entre 17h e 20h)
    if 17 <= hora <= 20:
        consumo_predio = round(random.uniform(40.0, 46.0), 2)
        horario_pico = True
    else:
        consumo_predio = round(random.uniform(20.0, 30.0), 2)
        horario_pico = False
    
consumo_total_previsto = consumo_predio + potencia_carregador_atual

print(f"[{hora}:00h] Consumo Total: {consumo_predio}kW | Demanda Total: {consumo_total_previsto}kW")

# algoritmo ChargeGrid de controle de demanda
if consumo_total_previsto > limite_contratado_kw or horario_pico:
    print("[ALERTA CHARGEGRID] Risco de ultrapassagem de demanda ou Horário de Pico detectado!")
    potencia_carregador_atual = 3.5
    print(f"[AÇÃO AUTOMATIZADA] Comando via MODBUS enviado. Reduzindo Carregador GoodWe para: {potencia_carregador_atual}kW")
else:
    potencia_carregador_atual = 7.0
    print(f"[STATUS] Operação normal. Carregador GoodWe operando em potência máxima: {potencia_carregador_atual}kW")
    
print("=" * 70)
time.sleep(1.5)
