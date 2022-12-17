import ipaddress

def Separate(n,y):
	"""function which takes as argument a character string representing a number in binary, and formats it as a block of bytes.
    :param string text: two character strings.
    :returns: decimal number stored as a string .
    :rtype: string
    """
	sep,j,x = " ",y,len(n)
	print(x%y)
	if x%y != 0:
		n = "0"*(y-x%y) + n
	print(len(n))
	L = [(n[i:i+j]) for i in range(0, len(n), j)]
	return sep.join(L)

def DeltaEncode(t):
    """Fonction delta qui  renvoie un tableau contenant les valeurs entières compressées à l’aide du delta encoding "
    Entrée: un tableau non vide de nombres entiers
    Sortie : un tableau contenant les valeurs entières compressées """
    n,f = [t[0]],len(t)
    [n.append(t[i]-t[i-1]) for i in range(1,f)]
    return n 

IdentifIdentificationication de classe de réseau à partir d'une adresse IP avec python

Pour identifier la classe de réseau à partir d'une adresse IP avec Python, vous pouvez utiliser la bibliothèque ipaddress qui fait partie de la bibliothèque standard de Python. Voici comment cela peut être fait:

Copy code


def get_network_class(ip):
    # Créez un objet IPv4Address à partir de l'adresse IP
    ip_obj = ipaddress.IPv4Address(ip)

    # Obtenez le premier octet de l'adresse IP
    first_octet = int(ip.split('.')[0])
    
    # Vérifiez la classe de réseau en fonction du premier octet
    if first_octet in range(1, 128):
        return "Classe A"
    elif first_octet in range(128, 192):
        return "Classe B"
    elif first_octet in range(192, 224):
        return "Classe C"
    elif first_octet in range(224, 240):
        return "Classe D"
    elif first_octet in range(240, 256):
        return "Classe E"


 



