# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'
# from pytz import timezone

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
data = datetime.now()
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1670849077))
# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)


###################################################################################################################

#  Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)


###################################################################################################################


# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)


###################################################################################################################

# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela


#  RESOLUÇÃO

# from datetime import datetime

# from dateutil.relativedelta import relativedelta     tava dando

# valor_total = 1_000_000
# data_emprestimo = datetime(2020, 12, 20)
# delta_anos = relativedelta(years=5)
# data_final = data_emprestimo + delta_anos

# data_parcelas = []
# data_parcela = data_emprestimo
# while data_parcela < data_final:
#     data_parcelas.append(data_parcela)
#     data_parcela += relativedelta(months=+1)

# numero_parcelas = len(data_parcelas)
# valor_parcela = valor_total / numero_parcelas

# for data in data_parcelas:
#     print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# print()
# print(
#     f'Você pegou R$ {valor_total:,.2f} para pagar '
#     f'em {delta_anos.years} anos '
#     f'({numero_parcelas} meses) em parcelas de '
#     f'R$ {valor_parcela:,.2f}.'
# )