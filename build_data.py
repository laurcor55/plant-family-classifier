import pywikibot
import re
import wikitextparser as wtp

def clean_description(description, genus_species):
  description =  description.replace(genus_species[0], '')
  description =  description.replace(genus_species[1], '')
  description =  description.replace('\n', ' ')
  pattern = '[A-Z]+[a-z]+aceae'
  description = re.sub(pattern, '',  description)
  pattern = '[A-z]+\s+family'
  description = re.sub(pattern, '',  description)
 # pattern = '\[\[+.+\]\]'
 # description = re.sub(pattern, '',  description)
  pattern = '\{+.+\}'
  description = re.sub(pattern, '',  description)
  return  description


def export_descriptions(descriptions, family_name):
  file_name = 'family_descriptions/' + family_name + '.txt'
  with open(file_name, 'w') as f:
    for description in descriptions:
      f.write("%s\n" % description)
  f.close()

def get_description(species_name):
  try:
    site = pywikibot.Site('en', 'wikipedia')
    page = pywikibot.Page(site, species_name)
    genus_species = species_name.split(' ')
    sections = wtp.parse(page.text).sections
    description = ' '
    for section in sections:
      if section.title=="Description":
        description = section.string
    description = clean_description(description, genus_species)
  except:
    description = ' '
  return description

def get_species(family_name):
  file_name = 'family_species/' + family_name + '.txt'
  f = open(file_name, "r")
  content = f.read()
  species = content.split('\n')
  species = [specie for specie in species if len(specie)>3]
  return species


#specie = 'Viola tricolor'
#description = get_description(specie)
family_names = ['brasicaceae']
for family_name in family_names:
  species = get_species(family_name)
  descriptions = []
  for specie in species:
    print(specie)
    description = get_description(specie)
    if len(description) > 100:
      descriptions.append(description)
    #if len(descriptions)>3:
    #  break
  export_descriptions(descriptions, family_name)
