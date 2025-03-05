'''
Certain materials are recognized as eco-friendly due to their low environmental impact. 
You need to track which materials are used by various brands and count how many times each material appears across all brands. 
This will help identify the most commonly used eco-friendly materials.

Write the count_material_usage() function, which takes a list of brands (each with a list of materials) and returns the material names and the number of times 
each material appears across all brands.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def count_material_usage(brands):
    myDict={}
    for brand in brands:
        for material in brand['materials']:
            myDict[material] = myDict.get(material,0) + 1
    return myDict

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))