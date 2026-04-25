from address import Address
from mailing import Mailing


address_from = Address("765678", "Москва", "Казанская", "10", "5")
address_to = Address("190000", "Санкт-Петербург", "Невский", "25", "12")
mailing = Mailing(to_address=address_to, from_address=address_from,
                  track="RU5678765467", cost=350
                  )
print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street},"
      f"{mailing.from_address.house} - {mailing.from_address.apartment}"
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
