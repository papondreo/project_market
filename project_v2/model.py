# Структура покупателей
# CUSTOMER_PROPORTION = {"одиночка": 165000,
#      "семья (2 человека)": 59675,
#      "семья (3 человека)": 50600,
#      "семья (4 человека)": 21725,
#      "семья (5 человек)": 4070,
#      "семья (6 человек)": 733,
#      "семья (7 человек и более)": 314}

# Структура покупателей (доля от реального объема покупателей)
# На сокращение структуры пришлось пойти из-за длительности расчетов
CUSTOMER_PROPORTION = {"одиночка": 1650,
                       "семья (2 человека)": 597,
                       "семья (3 человека)": 506,
                       "семья (4 человека)": 217,
                       "семья (5 человек)": 40,
                       "семья (6 человек)": 1,
                       "семья (7 человек и более)": 1}

# Число человек в семье
CUSTOMER_NUMBER_PEOPLE = {"одиночка": 1,
                          "семья (2 человека)": 2,
                          "семья (3 человека)": 3,
                          "семья (4 человека)": 4,
                          "семья (5 человек)": 5,
                          "семья (6 человек)": 6,
                          "семья (7 человек и более)": 7}

# Структура уровня финансового благосостояния покупателей
CUSTOMER_FINANCIAL_WEALTH = {"высокий": 1, "средний": 3, "низкий": 6}

# Список выбора текущего запаса сыра у покупателя
CUSTOMER_CURRENT_STOCK_CHEESE = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Среднее потребление сыра на одного человека в день в  граммах
CUSTOMER_AVG_CHEESE_CONSUMPTION = 15

# Структура потребление различных видов сыров
CUSTOMER_KIND_CHEESE = {"сыр твердый": 24,
                        "сыр полутвердый": 19,
                        "сыр мягкий": 17,
                        "прочие сыры": 16,
                        "продукты сырные": 24}

# Отношение к маркетинговым акциям
CUSTOMER_SENSITIVITY_MARKETING_CAMPAIGN = {"да": 3, "нет": 1}

# Готовность отказаться на время от потребления сыра
CUSTOMER_STOP_EATING_CHEESE = {"да": 2, "нет": 1}

# Готовность переключиться на более дешевый вид сыра
CUSTOMER_SWITCHING_ANOTHER_CHEESE = {"да": 1, "нет": 2}

# Готовность искать сыр по старой цене в других продуктовых сетях
CUSTOMER_LOOKING_CHEESE = {"да": 2, "нет": 1}

# Чувствительный порог изменения старой цены на сыр
CUSTOMER_SIGNIFICANT_PRICE_CHANGE = [5, 7.5, 10, 15, 20]

# Список выбора объема покупки
BUY_VALUE_CHEESE = [200, 300, 400, 500, 600, 700, 800, 900, 1000]

# ----------------------------------------------------------------------------------------------------------------------
# Структура продуктовых сетей города
RETAILER_PROPORTION = {"A1": 33, "A2": 26, "A3": 16, "A4": 17, "A5": 8}
# Список ритейлеров для поиска аналогичного товара по более доступной цене.
RETAILER_TOP = ['A1', 'A2', 'A3', 'A4', 'A5']

# -----------------------------------------------------------------------------------------------------------------------
# Дата с базовыми ценами
DATE_BASE = '31.12.2019'
# Дата начала моделирования
DATE_START = '01.01.2020'
# Дата конца моделирования
DATE_FINISH = '31.01.2020'

# -----------------------------------------------------------------------------------------------------------------------
# Список рабочих моделей
LIST_MODEL_WORK = [0, 1, 2]
# ----------------------------------------------------------------------------------------------------------------------
# Паттерны для формирования имен файлов
FILE_NAME_PATTERN_PRICES = 'prices_model_{}.csv'
FILE_NAME_PATTERN_SALES = 'sales_model_{}.csv'
FILE_NAME_PATTERN_CUSTOMERS_INFO = 'customers_info_{}.csv'

# ----------------------------------------------------------------------------------------------------------------------
# Номер первой модели для A/B тестирования
AB_TEST_NUMBER_FIRST_MODEL = 0
# Номер второй модели для A/B тестирования
AB_TEST_NUMBER_SECOND_MODEL = 1
# Номер третьей модели для A/B тестирования
AB_TEST_NUMBER_THIRD_MODEL = 2
# Наименование ритейлера, который участвует в A/B тестировании
AB_TEST_NAME_RETAILER = 'A1'
