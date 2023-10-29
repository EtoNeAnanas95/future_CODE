# Собственные запреты

class MoneyError(Exception):

  def __init__(self, amount: int, sender: str, recipient: str) -> None:
    super().__init__(
        f"Невозможно передать негативное кол-во денег ({amount}) от {sender} к {recipient}"
    )

def transfer_money(sender: str, recipient: str, amount: int) -> None:
  if amount < 0:
    raise MoneyError(amount, sender, recipient)

  # Тут дальше должна быть реализация передачи

# Проверка работы ошибки
try:
  sender = "Дмитрий"
  recipient = "Даниил"
  amount = -100
  transfer_money(sender, recipient, amount)
except MoneyError as e:
  print(f"Не удалось перевести деньги. Ошибка: {e}")
