# --- IMPORTANDO O MÓDULO DA FUNÇÃO DATETIME ---
from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    # --- Informando dia e hora ---
    print(data_atual)
    # --- Informando somente o dia 'string' ---
    print(data_atual.strftime('%d/%m/%Y'))
    # --- Informando somente a hora 'string' ---
    print(data_atual.strftime('%H:%M:%S'))
    # --- Informando dia da semana, mês, ano e horário ---
    print(data_atual.strftime('%c'))
    # --- Informando o Mês ---
    print(data_atual.month)
    # --- Informando o dia da semana ---
    print(data_atual.weekday())
    tupla = ('Monday', 'Tuesday', 'Wednesday', 'Thursay', 'Friday', 'Saturday', 'Sunday')
    # print(tupla[data_atual.weekday()])
    # --- Criando uma data com 'string' ---
    data_criada = datetime(2015, 5, 20, 17, 45, 41)
    # print(data_criada.strftime('%c'))
    # --- Convertendo uma data do tipo 'string' para 'datetime' ---
    data_string = '05-10-2017 12:20:32'
    data_convertida = datetime.strptime(data_string, '%d-%m-%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    # --- Retirando um ano da data anterior e 2 horas e 15 minutos ---
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d-%m-%Y'))
    print(data_atual.strftime('%A %B %Y'))
    print(type(data_atual))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    # --- Horário em 'datetime.time'
    print(horario)
    print(type(horario))
    #--- Horário em 'string'
    horario_str = (horario.strftime('%H:%M:%S'))
    print(type(horario_str))

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()