import pandas as pd
import xml.etree.ElementTree as ET


tree = ET.parse('FeagriTeste01.kml')

ns = {'kml': "http://www.opengis.net/kml/2.2"}

root = tree.getroot()
documents = root.findall('kml:Document', ns)

for document in documents:
  placemarks = document.findall("kml:Placemark", ns)

for placemark in placemarks:
  name = placemark.find("kml:name",ns)
  print(f'Nome: {name.text}')
  
  point = placemark.find('kml:Point', ns)
  if point is not None:
    coords = point.find('kml:coordinates', ns)
    print(f'Tipo: Ponto')
    print(f'Coordenadas {coords.text.strip()}')
  polygon = placemark.find('kml:Polygon', ns)
  if polygon is not None:
    coords = polygon.find('.//kml:coordinates', ns)
    print('Tipo: Poligono')
    print(f'Coordenadas {coords.text.strip()}')
  print('---')




