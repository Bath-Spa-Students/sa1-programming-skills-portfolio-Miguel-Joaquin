# Dictonaries

People_Info = {
    'Person_1': {
        'First_Name': 'Dawn',
        'Last_Name': 'Pinzo',
        'Age': 19,
        'City': 'Dubai'      
    },
    'Person_2': {
        'First_Name': 'Kurt',
        'Last_Name': 'Calesa',
        'Age': 18,
        'City': 'Sharjah'
    },
    'Person_3': {
        'First_Name': 'Vic',
        'Last_Name': 'Garcia',
        'Age': 19,
        'City': 'Sharjah'
    }
}

for person, info in People_Info.items():
    print(f"{person}:")
    print(f"  First name: {info['First_Name']}")
    print(f"  Last name: {info['Last_Name']}")
    print(f"  Age: {info['Age']}")
    print(f"  City: {info['City']}")
    print()
