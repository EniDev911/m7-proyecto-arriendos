import os,time,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_site.settings")
django.setup()

from arrienda_ya.models import Inmueble, Region

def get_list_inmuebles(name, descr):
  list_inmuebles = Inmueble.objects.filter(nombre_inmueble__contains=name).filter(descripcion__contains=descr)

  xfile = open("datos.txt", "w")
  for inmueble in list_inmuebles.values():
      xfile.write(str(inmueble))
      xfile.write("\n")
  xfile.close()
  return list_inmuebles

# resultado = get_list_inmuebles("Providencia", "Cocina")
def get_list_inmuebles_by_comuna(comuna):
  select = f"""
  SELECT inmueble.id, inmueble.nombre_inmueble, inmueble.descripcion
  FROM public.arrienda_ya_inmueble AS inmueble
  INNER JOIN public.arrienda_ya_region AS region
  ON inmueble.id_region_id = region.id
  INNER JOIN public.arrienda_ya_comuna AS comuna
  ON inmueble.id_comuna_id = comuna.id
  WHERE comuna.comuna LIKE '%%{str(comuna)}%%'
  """
  
  results = Inmueble.objects.raw(select)

  xfile = open("datos.txt", "w")

  for result in results:
    xfile.write(result.nombre_inmueble+','+result.descripcion)
    xfile.write("\n")
  xfile.close()

get_list_inmuebles_by_comuna("Bernardo")
