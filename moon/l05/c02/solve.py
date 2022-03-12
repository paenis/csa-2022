#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node
# that have name attributes, the third node should be Panama.
#

import xml.etree.ElementTree as ET


root = ET.Element('root')

country = ET.SubElement(root, 'country')
country.attrib['name'] = 'foo'

country = ET.SubElement(root, 'country')
country.attrib['name'] = 'bar'

country = ET.SubElement(root, 'country')
country.attrib['name'] = 'Panama'

ET.dump(root)

tree = ET.ElementTree()
tree._setroot(root)

tree.write('/tmp/vulnerable-countries.xml')
