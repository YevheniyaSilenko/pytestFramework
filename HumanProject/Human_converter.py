import json
import xml.etree.ElementTree as ET
import sys

class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        data = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'birth_year': self.birth_year
        }
        return json.dumps(data, indent=2)

    def convert_to_xml(self):
        human_element = ET.Element('Human')
        name_element = ET.SubElement(human_element, 'Name')
        name_element.text = self.name

        age_element = ET.SubElement(human_element, 'Age')
        age_element.text = str(self.age)

        gender_element = ET.SubElement(human_element, 'Gender')
        gender_element.text = self.gender

        birth_year_element = ET.SubElement(human_element, 'BirthYear')
        birth_year_element.text = str(self.birth_year)

        xml_str = ET.tostring(human_element, encoding='utf-8').decode('utf-8')
        return xml_str

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [json/xml]")
        sys.exit(1)

    output_format = sys.argv[1].lower()

    human_instance = Human("Pears Brosnan", 25, "Male", 1998)

    if output_format == 'json':
        json_data = human_instance.convert_to_json()
        print(json_data)
        with open('output.json', 'w') as json_file:
            json_file.write(json_data)
    elif output_format == 'xml':
        xml_data = human_instance.convert_to_xml()
        print(xml_data)
        with open('output.xml', 'w') as xml_file:
            xml_file.write(xml_data)
    else:
        print("Invalid format. Please use 'json' or 'xml'.")

