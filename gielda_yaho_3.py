import os
import pandas as pd
import matplotlib.pyplot as plt

# Ścieżka do katalogu, w którym znajdują się pliki CSV z danymi
stock_data_dir = './stock_data'

# Funkcja, która wczytuje dane z pliku CSV bez nagłówków
def load_data(file_name):
    file_path = os.path.join(stock_data_dir, file_name)

    # Zdefiniowanie nagłówków, które przypiszemy do danych
    headers = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    
    # Wczytanie danych bez nagłówków
    df = pd.read_csv(file_path, header=None, names=headers)

    # Konwersja kolumny 'Date' na format daty
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Sprawdzamy, czy kolumna 'Date' jest poprawnie przekształcona
    if df['Date'].isnull().any():
        print("Nie udało się poprawnie przekonwertować kolumny 'Date'.")
        return None

    return df

# Funkcja do rysowania wykresu na podstawie wczytanych danych
def plot_stock_data(df, stock_symbol):
    if df is None:
        print(f"Brak danych dla {stock_symbol}")
        return

    # Ustawienie daty jako indeks
    df.set_index('Date', inplace=True)

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], label=f'{stock_symbol} - Close Price', color='blue')
    plt.title(f'{stock_symbol} - Ceny Zamknięcia')
    plt.xlabel('Data')
    plt.ylabel('Cena (USD)')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Wybór pliku, który chcesz wyświetlić
stock_symbol = 'AAPL.csv'  # Przykładowy plik, zmień na odpowiedni

# Wczytanie danych z pliku
data = load_data(stock_symbol)

# Rysowanie wykresu na podstawie danych
plot_stock_data(data, stock_symbol)

