# UKOL - Signálové operace a grafy
import matplotlib.pyplot as plt


# načtení signálu
def load_signal_from_txt(path):
    values = []   # seznam pro hodnoty
    file = open(path, "r")   # čtení
    for line in file:
        line = line.strip()
        if line != "":   # ignoruju řádky, kde nic není
            number = float(line)
            values.append(number)
    file.close()
    return values


# výpočet minima
def signal_min(values):
    minimum = values[0]
    for i in range(len(values)):
        if values[i] < minimum:
            minimum = values[i]
    return minimum


# výpočet maxima
def signal_max(values):
    maximum = values[0]
    for i in range(len(values)):
        if values[i] > maximum:
            maximum = values[i]
    return maximum


# výpočet průměru
def signal_avg(values):
    total = 0
    for i in range(len(values)):
        total = total + values[i]
    avg = total / len(values)   # vydělím všema prvkama
    return avg   # průměr


# vykreslení grafu signálu
def plot_signal(values):
    x = []   # seznam pro osuX
    for i in range(len(values)):
        x.append(i)

    plt.plot(x, values)   # vykreslím graf
    plt.xlabel("Vzorek")   # popisy os a názvu, něco jak v matlabu
    plt.ylabel("Hodnota")
    plt.title("Signal")
    plt.show()   # zobrazení


# hlavní testování
if __name__ == "__main__":
    signal = load_signal_from_txt("ekg_signal.txt")
    print("Minimum:", signal_min(signal))
    print("Maximum:", signal_max(signal))
    print("Průměr:", signal_avg(signal))
    plot_signal(signal)