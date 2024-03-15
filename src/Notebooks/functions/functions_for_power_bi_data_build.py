def group_region_code(df):
    
    mapeo = {1.0: "PV", 2.0: "CM",  3.0: "VC",  4.0: "AN",  5.0: "CL",  6.0: "EX", 7.0: "IB",  8.0: "CT",  9.0: "CL", 10.0: "EX", 11.0: "AN", 
          12.0: "VC", 13.0: "CM", 14.0: "AN", 15.0: "GA", 16.0: "CM", 17.0: "CT", 18.0: "AN", 19.0: "CM", 20.0: "PV", 21.0: "AN", 22.0: "AR", 
          23.0: "AN", 24.0: "CL", 25.0: "CT", 26.0: "RI", 27.0: "GA", 28.0: "MD", 29.0: "AN", 30.0: "MC", 31.0: "NC", 32.0: "GA", 33.0: "AS", 34.0: "CL", 
          35.0: "CN", 36.0: "GA", 37.0: "CL", 38.0: "CN", 39.0: "CB", 40.0: "CL", 41.0: "AN",  42.0: "CL", 43.0: "CT", 44.0: "AR", 45.0: "CM", 46.0: "VC", 
          47.0: "CL", 48.0: "PV",  49.0: "CL", 50.0: "AR", 51.0: "CE", 52.0: "ML"}
    
    mapeo_2 = {1.0: "País Vasco", 2.0: "Castilla la Mancha",  3.0: "Comunidad Valenciana",  4.0: "Andalucía",  5.0: "Castilla y León",  6.0: "Extremadura", 7.0: "Islas Baleares",  
               8.0: "Cataluña",  9.0: "Castilla y León", 10.0: "Extremadura", 11.0: "Andalucía", 12.0: "Comunidad Valenciana", 13.0: "Castilla la Mancha", 14.0: "Andalucía", 15.0: "Galicia", 
               16.0: "Castilla la Mancha", 17.0: "Cataluña", 18.0: "Andalucía", 19.0: "Castilla la Mancha", 20.0: "País Vasco", 21.0: "Andalucía", 22.0: "Aragón", 23.0: "Andalucía", 24.0: "Castilla y León", 
               25.0: "Cataluña", 26.0: "La Rioja", 27.0: "Galicia", 28.0: "Madrid", 29.0: "Andalucía", 30.0: "Murcia", 31.0: "Navarra", 32.0: "Galicia", 33.0: "Asturias", 34.0: "Castilla y León", 35.0: "Canarias", 
               36.0: "Galicia", 37.0: "Castilla y León", 38.0: "Canarias", 39.0: "Cantabria", 40.0: "Castilla y León", 41.0: "Andalucía",  42.0: "Castilla y León", 43.0: "Cataluña", 44.0: "Aragón", 45.0: "Castilla la Mancha", 
               46.0: "Comunidad Valenciana", 47.0: "Castilla y León", 48.0: "País Vasco",  49.0: "Castilla y León", 50.0: "Aragón", 51.0: "Ceuta", 52.0: "Melilla"}
    
    df['regions_ca_id'] = ''
    df['regions_ca_id'] = df['region_code'].apply(lambda x: mapeo.get(float(x)) if x != 'Extranjero' else x)
    
    df['regions_ca_id_2'] = ''
    df['regions_ca_id_2'] = df['region_code'].apply(lambda x: mapeo_2.get(float(x)) if x != 'Extranjero' else x)
    
    df.drop('region_code', axis='columns', inplace=True)
    df.drop('country_id', axis='columns', inplace=True)
    
    return df

def create_products_family(df):
    
    list_products = ['short_term_deposit', 'loans', 'mortgage', 'funds', 'securities', 'long_term_deposit', 'em_account_pp', 'credit_card',
                     'payroll', 'pension_plan', 'payroll_account', 'emc_account', 'debit_card', 'em_account_p', 'em_acount']

    # Agrupación de productos por naturaleza 

    list_debt = ['loans', 'mortgage']
    list_investments = ['short_term_deposit', 'funds', 'securities', 'long_term_deposit', 'pension_plan']
    list_account = ['em_account_pp', 'emc_account', 'em_account_p',  'em_acount', 'payroll_account', 'payroll']
    list_cards = ['credit_card', 'debit_card']

    # Relaciones de debitos o indicativos de fidelización
    list_fidel = ['payroll', 'payroll_account','loans', 'mortgage', 'pension_plan']

    list_financing_60 = list_debt+list_cards
    list_invest_savings_40 = list_investments
    list_account_10= list_account

    # Verificación
    len(list_debt + list_investments + list_account + list_cards ) == len(list_products)

    df['nr_account_10'] = 0
    df['nr_account_10'] = df[list_account_10].sum(axis = 1)
    
    df['nr_invest_savings_40'] = 0
    df['nr_invest_savings_40'] = df[list_invest_savings_40].sum(axis = 1)
    
    df['nr_financing_60'] = 0
    df['nr_financing_60'] = df[list_financing_60].sum(axis = 1)