import csv
import xml.etree.ElementTree as ET


tree = ET.parse('FeagriTeste01.kml')

ns = {'kml': "http://www.opengis.net/kml/2.2"}

root = tree.getroot()
documents = root.findall('kml:Document', ns)

for document in documents:
  placemarks = document.findall("kml:Placemark", ns)

dados = []

for placemark in placemarks:
  name = placemark.find("kml:name",ns)
  tipo = ""
  coordenadas = ""
  
  point = placemark.find('kml:Point', ns)
  if point is not None:
    coords = point.find('kml:coordinates', ns)
    tipo = "Ponto"
    coordenadas = coords.text.strip()
  polygon = placemark.find('kml:Polygon', ns)
  if polygon is not None:
    coords = polygon.find('.//kml:coordinates', ns)
    tipo = "Polígono"
    coordenadas = coords.text.strip()
  dados.append([name.text, tipo, coordenadas])

with open("saida.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Tipo", "Coordenadas"])
    writer.writerows(dados)




