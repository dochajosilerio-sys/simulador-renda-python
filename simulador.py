def calcular_simulador_social():
    print("\n" + "="*40)
    print("--- SIMULADOR DE RENDA E VIABILIDADE v2.0 ---")
    print("="*40)

<<<<<<< HEAD
    # 1. Parâmetros e Auxílios Estudantis (IFMG/SENAI/CEFET)
=======
    # 1. Parâmetros e Auxílios Estudantis (Ex: IFMG/SENAI/CEFET)
>>>>>>> 592a4ff (feat: adiciona lógica do simulador e estrutura de dados)
    bolsa_familia_base = 600.00
    ajuda_custo_estudante = 440.00 
    
    # 2. Entradas de Renda
    salario_estagio = float(input("\nDigite o valor do estágio (ou 0): "))
    meses_empregado = int(input("Meses desde que conseguiu o estágio: "))
    
    # 3. Lógica: Regra de Proteção (Bolsa Família)
    if salario_estagio > 218.00 and meses_empregado <= 24:
        bolsa_familia = bolsa_familia_base / 2
<<<<<<< HEAD
        status_protecao = "Ativa (50% mantido)"
    elif meses_empregado > 24:
        bolsa_familia = 0.0
        status_protecao = "Encerrada (Prazo expirado)"
=======
        status_protecao = "Ativa (50%)"
    elif meses_empregado > 24:
        bolsa_familia = 0.0
        status_protecao = "Encerrada (Fim do Prazo)"
>>>>>>> 592a4ff (feat: adiciona lógica do simulador e estrutura de dados)
    else:
        bolsa_familia = bolsa_familia_base
        status_protecao = "Integral"

<<<<<<< HEAD
    # 4. Módulo de Tarifas e Utilidades (Lei 14.203/2021)
    print("\n--- Descontos Tarifa Social ---")
    conta_luz = float(input("Valor da conta de LUZ (sem desconto): "))
    conta_agua = float(input("Valor da conta de ÁGUA (sem desconto): "))
=======
    # 4. Módulo de Tarifas e Utilidades (Estimativa Lei 14.203)
    print("\n--- Descontos Tarifa Social ---")
    conta_luz = float(input("Valor da conta de LUZ (cheia): "))
    conta_agua = float(input("Valor da conta de ÁGUA (cheia): "))
>>>>>>> 592a4ff (feat: adiciona lógica do simulador e estrutura de dados)
    economia = (conta_luz * 0.65) + (conta_agua * 0.50)

    # 5. Programa Acredita (Microcrédito MEI)
    tem_mei = input("\nVocê possui MEI? (s/n): ").lower()
    limite_acredita = 21000.00 if tem_mei == 's' else 0.0

<<<<<<< HEAD
    # 6. Investimento e ROI (Terreno/Aluguel)
    print("\n--- Investimento Imobiliário ---")
    custo_obra = float(input("Valor total da obra: "))
    aluguel_previsto = float(input("Aluguel mensal previsto: "))
=======
    # 6. Investimento e ROI (Terreno/Obra)
    print("\n--- Investimento Imobiliário ---")
    custo_obra = float(input("Valor total da obra: "))
    aluguel_previsto = float(input("Valor de aluguel estimado: "))
>>>>>>> 592a4ff (feat: adiciona lógica do simulador e estrutura de dados)
    roi_anual = ((aluguel_previsto * 12) / custo_obra) * 100 if custo_obra > 0 else 0

    # EXIBIÇÃO DOS RESULTADOS
    total_mensal = bolsa_familia + ajuda_custo_estudante + salario_estagio
    
    print("\n" + "="*40)
    print("      RESULTADO DO SIMULADOR")
    print("="*40)
    print(f"Status Bolsa Família: {status_protecao}")
    print(f"Renda Mensal Total:   R$ {total_mensal:.2f}")
    print(f"Economia Tarifas:     R$ {economia:.2f}")
    print(f"Crédito 'Acredita':   R$ {limite_acredita:.2f}")
    print(f"Retorno Obra (ROI):   {roi_anual:.2f}% ao ano")
    print("="*40)

if __name__ == "__main__":
    try:
        calcular_simulador_social()
    except ValueError:
<<<<<<< HEAD
        print("\nErro: Por favor, insira apenas números para valores financeiros.")

=======
        print("\nErro: Por favor, insira apenas números nos campos de valores.")
>>>>>>> 592a4ff (feat: adiciona lógica do simulador e estrutura de dados)

