import csv
import datetime

class Rekins:
    def__init__( self, klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials
      self.laiks = datetime.datetime.now()

    def aprekins(self):
        result = self.size[0] * self.size[1] * self.size[2] * self.materials
  return result

def print0(self):
  print("Klients:", self.klients)
  print("Veltijums:", self.veltijums)
  print("Izmers:", self.izmers)
  print("Materials:", self.materials)
  print("Laiks:", self.laiks.strftime)
  print("Payment amount:", self.aprekins())

def save0(self):
  filename + f"{self.klients}_{datetime.date.today()}.csv"
  with open(filename,mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Klients", "Veltijums", "Izmers", "Materials", "Laiks", "Payment amount"])
    writer.writerow([self.klients, self.veltijums,self.size, self.materials, self.laiks, self.aprekins()])
