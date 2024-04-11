{
    "name": "Real Estate Ads",
    "version": "1.0",
    "website": "https://www.theodo.com",
    "author": "DucHM",
    "description": """
        Real Estate Module to show available properties
    """, 
    "license": "LGPL-3",
    "application":True,
    "installable":True,
    "data": [
        "security/ir.model.access.csv",
        "views/property_type_view.xml",
        "views/property_view.xml",
        "views/property_tag_view.xml",
        "views/menu_items.xml",

        # Datas files
        # 'data/property_type.xml'
        'data/estate.property.type.csv',
    ],
    
    "depends": ["base"],
    "category": "Sales"
}