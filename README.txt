В первом commit надо было запускать exchange_rate_parser.py что бы создать json файл,
в котором курсы крипто валют, а потом запускать бота через bot_exchange_rates.py.

Теперь надо запускать только bot_exchange_rates.py, который сам запускает
exchange_rate_parser.py, который создаёт или обновляет json файл с курсами крипты.