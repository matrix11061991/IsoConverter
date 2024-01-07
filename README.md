
```sh
  _____            _____                          _            
 |_   _|          / ____|                        | |           
   | |  ___  ___ | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
   | | / __|/ _ \| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
  _| |_\__ \ (_) | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
 |_____|___/\___/ \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
```                                                               
IsoConverter is a Python library for dealing with multiple conversion.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install IsoConverter.

```bash
pip install IsoConverter
```

## Usage

```python
from IsoConverter.go import *
# returns converted 'words' and returns converted Hexadecimal 8859
x,y,z = HexaIso8859T1_to_Text("C2 6E 65 20 6F F9 20 42 EA 74 65"),Text_to_HexaIso8859T1("Enter"),decToIeee32(17.125)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## 🚀 Author
Jaurès Ratsimbazafiharivola **[Matrix Tera]**
## Link on pypi.org
https://pypi.org/project/IsoConverter/ 
## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
