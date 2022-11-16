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