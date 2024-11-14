"""
Vérifie si une chaine de caractère est un palindrome
"""
import string
def nettoyerchaine(p):
    """
    Retourne la chaine de caractère sans accent, sans espace, sans ponctuation et en minuscules
    """
    p = p.lower()
    accents = str.maketrans("àâäéèêëùûüîïôöç","aaaeeeeuuuiiooc")
    p = p.translate(accents)
    p = p.translate(str.maketrans("","",string.whitespace + string.punctuation))
    return p


def ispalindrome(p):
    """
    Vérifie si une cahine de caractère est un palindrome
    """
    p = nettoyerchaine(p)
    return p[::-1]==p

#### Fonction principale


def main():
    """
    appelle la fonction ispalindrome
    """
    # vos appels à la fonction secondaire ici
    print(ispalindrome("faker"))
    print(ispalindrome("hello"))
    print(ispalindrome("ici"))
    print(ispalindrome("ressasser"))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
