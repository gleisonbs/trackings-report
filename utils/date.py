
import sys

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
def get_month_from_date(date):
    date = str(date)
    numeric_month = int(date.split('-')[1])
    return (numeric_month, months[numeric_month-1])

def get_date_period():
    try:
        from_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
        to_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
        return (from_date, to_date)
    except:
        print("É necessário passar uma data inicial e uma data final, no formato mes/dia/ano")
        return (None, None)