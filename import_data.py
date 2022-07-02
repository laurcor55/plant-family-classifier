import wikipedia
import re

def get_description_section(species_name):
  result = wikipedia.search(species_name)
  page = wikipedia.page(result[0])
  content = page.content
  try:
    section_name = '== Description ==\n\n'
    ind = content.find(section_name) + len(section_name)
    content = content[ind:]
    ind = content.find('\n\n\n== ')
    content = content[:ind]
  except:
    content = ''
  return content

species_names = ["prunus americana", "Erica carnea", '']
for species_name in species_names:
  content = get_description_section(species_name)
  print(content)
  print('_________')