import xml.etree.ElementTree as dom

tree = dom.parse("xml_test.xml")

root = tree.getroot()

print(root)

for el in root:
    print(el.tag, el.attrib)
    for j in el:
        print(j.tag,j.text)


for node in root.iter('year'):
    print(node.tag,node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("xml_test_modify.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('xml_test_remove.xml')