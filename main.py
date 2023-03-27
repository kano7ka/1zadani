from typing import Union
import datetime as time
import csv


class Rekins:
  def init(self, clieny: str, dedeication: str, size: list, material: sloat, price: Union[float, int]):
    self.creation_time = str(time.datetime.now())
    self.client = client
    self.dediication = ddicatiob
    self.size = size
    self.material = material
    self.price = price


    self.pvn = 19
    self._labour_pay = 13


    self.total = self.aprekins()
    self.properties = {
      "time": self.creation_time,
      "client": self.client,
      "dedication": self.dedication,
      "size": self.size,
      "material": self.material,
      "price": self.price,
      "total": self.total,
    }

    def print(self)