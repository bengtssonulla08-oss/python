from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "A213", "+79346473633"),
    Smartphone("Honor", "400", "+79675453423"),
    Smartphone("Huawei", "Pura 80", "+79896547689")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
