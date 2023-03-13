import my_funcionts_1
import functools

def get_total(orders):
  # Tu código aquí 👇
  lista_costos = my_funcionts_1.get_totals(orders)
  suma_costos = my_funcionts_1.calc_total(lista_costos)
  #otra froma de hacerlo:
  sumatoria = functools.reduce(lambda contador , item : contador + item["total"], orders , 0)
  return suma_costos 

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)