import string

from .common import STYLE_ROOT

FILE = STYLE_ROOT / "vectors.sty"


def get_english_alphabet():
    # string.ascii_lowercase -> 'abcdefghijklmnopqrstuvwxyz'
    # string.ascii_uppercase -> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_letters = list(string.ascii_lowercase + string.ascii_uppercase)
    return all_letters


def get_standard_greek_latex_dict():
    greek_letters_latex = {
        # alpha
        "alpha": r"\alpha",
        "Alpha": "A",
        # beta
        "beta": r"\beta",
        "Beta": "B",
        # gamma
        "gamma": r"\gamma",
        "Gamma": r"\Gamma",
        # delta
        "delta": r"\delta",
        "Delta": r"\Delta",
        # epsilon
        "epsilon": r"\epsilon",
        "Epsilon": "E",
        # zeta
        "zeta": r"\zeta",
        "Zeta": "Z",
        # eta
        "eta": r"\eta",
        "Eta": "H",
        # theta
        "theta": r"\theta",
        "Theta": r"\Theta",
        # iota
        "iota": r"\iota",
        "Iota": "I",
        # kappa
        "kappa": r"\kappa",
        "Kappa": "K",
        # lambda
        "lambda": r"\lambda",
        "Lambda": r"\Lambda",
        # mu
        "mu": r"\mu",
        "Mu": "M",
        # nu
        "nu": r"\nu",
        "Nu": "N",
        # xi
        "xi": r"\xi",
        "Xi": r"\Xi",
        # omicron
        # (no special command in LaTeX; rendered like 'o'/'O' in math mode)
        "omicron": "o",
        "Omicron": "O",
        # pi
        "pi": r"\pi",
        "Pi": r"\Pi",
        # rho
        "rho": r"\rho",
        "Rho": "P",
        # sigma
        "sigma": r"\sigma",
        "Sigma": r"\Sigma",
        # tau
        "tau": r"\tau",
        "Tau": "T",
        # upsilon
        "upsilon": r"\upsilon",
        "Upsilon": r"\Upsilon",
        # phi
        "phi": r"\phi",
        "Phi": r"\Phi",
        # chi
        "chi": r"\chi",
        "Chi": "X",
        # psi
        "psi": r"\psi",
        "Psi": r"\Psi",
        # omega
        "omega": r"\omega",
        "Omega": r"\Omega",
    }

    return greek_letters_latex


def write():
    english_alphabet = get_english_alphabet()
    with open(FILE, "w") as f:
        s = "\\usepackage{amsmath}"
        f.write(f"{s}\n")
        for ll in english_alphabet:
            s = "\\newcommand{\\vec%s}{\\mathbf{%s}}" % (ll, ll)
            f.write(f"{s}\n")
        for k, v in get_standard_greek_latex_dict().items():
            cmd = "mathbf" if v in english_alphabet else "boldsymbol"
            s = "\\newcommand{\\vec%s}{\\%s{%s}}" % (k, cmd, v)
            f.write(f"{s}\n")
