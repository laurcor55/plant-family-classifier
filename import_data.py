import wikipedia
import re



def get_description_section(species_name):
  result = wikipedia.search(species_name)
  pattern = '^[A-Z]+[a-z]+\s+[a-z]'
  if re.search(pattern, result[0]):
    genus_species = result[0].split(' ')
    page = wikipedia.page(result[0])
    content = page.content
    try:
      section_name = '== Description =='
      ind = content.find(section_name) + len(section_name)
      content = content[ind:]
      ind = content.find('== ')
      content = content[:ind]
      content = content.replace(genus_species[0], '')
      content = content.replace(genus_species[1], '')
      content = content.replace('\n', ' ')
      pattern = '[A-Z]+[a-z]+aceae'
      content = re.sub(pattern, '', content)
      pattern = '[A-z]+\s+family'
      content = re.sub(pattern, '', content)
    except:
      content = None
  else:
    content = None
  return content

species_file = open('family_species/solanaceae.txt')
species_names_all = species_file.read().split('\n')
species_names = []
descriptions = []
for species_name in species_names_all:
  description = get_description_section(species_name)
  if description:
    species_names.append(species_name)
    descriptions.append(description)
    if len(species_names)>5:
      break
print(species_names)
print(descriptions)