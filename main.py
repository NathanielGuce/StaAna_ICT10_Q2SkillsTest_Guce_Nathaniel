from pyscript import display, document

def elementchecker(e):
    elements = {
    "H": ("hydrogen",1, 1.000),
    "He" : ("helium", 2, 4.0026),
    "Li" : ("lithium", 3, 6.94),
    "Be" : ("beryllium", 4, 9.0122),
    "B" : ("boron", 5, 10.81),
    "C" : ("carbon", 6, 12.01),
    "N" : ("nitrogen", 7, 14.01),
    "O" : ("oxygen", 8, 16.00),
    "F" : ("fluorine", 9, 19.00),
    "Ne" : ("neon", 10, 20.18),
    "Na" : ("sodium", 11, 22.99),
    "Mg" : ("magnesium", 12, 24.31),
    "Al" : ("aluminum", 13, 26.98),
    "Si" : ("silicon", 14, 28.09),
    "P" : ("phosphorus", 15, 30.97),
    "S" : ("sulfur", 16, 32.07),
    "Cl" : ("chlorine", 17, 35.45),
    "Ar" : ("argon", 18, 39.95),
    "K" : ("potassium", 19, 39.10),
    "Ca" : ("calcium", 20, 40.08),
    }

    document.getElementById("result").innerHTML = " "
    elementname = document.getElementById('elementname').value.strip().title()
    elementdesc = elements.get(
        elementname, ("Element not found", "N/A", "N/A")
        )
    document.getElementById("result").innerHTML = f"""
    Symbol: {elementname}<br>
    Name: {elementdesc[0]}<br>
    Atomic Number: {elementdesc[1]}<br>
    Atomic Mass: {elementdesc[2]}<br>
    """