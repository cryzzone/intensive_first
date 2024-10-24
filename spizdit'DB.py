import cianparser
import pandas

moscow_parser = cianparser.CianParser(location="Москва")
data = moscow_parser.get_flats(deal_type="sale", rooms=(1, 2, 3, 4, 5), with_saving_csv=True, additional_settings={"start_page":1, "end_page":54}, with_extra_data=True)


print(data[0,'%'])