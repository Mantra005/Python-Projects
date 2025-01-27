import yfinance as yf
import pandas as pd
import numpy as np
import talib
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from tkinter import messagebox, filedialog

# Fetch stock data from yfinance
def fetch_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date, progress=False)
        if data.empty:
            print(f"No data found for {symbol} in the specified date range.")
            return None
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Detect technical patterns using TA-Lib
def detect_patterns(data):
    patterns = {}

    # Detect Engulfing Pattern
    engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
    patterns['Engulfing'] = engulfing.iloc[-1]

    # Detect Hammer Pattern
    hammer = talib.CDLHAMMER(data['Open'], data['High'], data['Low'], data['Close'])
    patterns['Hammer'] = hammer.iloc[-1]

    # Detect Shooting Star Pattern
    shooting_star = talib.CDLSHOOTINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])
    patterns['Shooting Star'] = shooting_star.iloc[-1]

    return patterns

# AI-based Buy/Sell recommendations
def generate_recommendation(patterns):
    recommendations = []
    for pattern, value in patterns.items():
        if value > 0:
            recommendations.append(f"{pattern} detected. Suggest BUY.")
        elif value < 0:
            recommendations.append(f"{pattern} detected. Suggest SELL.")
    
    if not recommendations:
        return "No strong patterns detected. Hold or wait."
    
    return "\n".join(recommendations)

# Use Selenium to observe TradingView charts
def open_tradingview_chart(url):
    try:
        # Set up the Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Open the TradingView chart
        driver.get(url)
        print("TradingView chart opened successfully.")
        driver.implicitly_wait(10)

        # Take a screenshot of the chart
        screenshot_path = "tradingview_chart.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}.")

        driver.quit()
    except Exception as e:
        print(f"Error with TradingView chart: {e}")

# GUI for the application
def main_gui():
    def analyze_stock():
        symbol = symbol_entry.get()
        days = int(days_entry.get())

        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days)

        # Fetch stock data
        data = fetch_stock_data(symbol, start_date, end_date)
        if data is None:
            messagebox.showerror("Error", "No data available for the selected symbol and date range.")
            return

        # Detect patterns
        patterns = detect_patterns(data)

        # Generate recommendation
        recommendation = generate_recommendation(patterns)
        result_text.set(recommendation)

    def open_chart():
        url = chart_url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid TradingView URL.")
            return
        open_tradingview_chart(url)
        messagebox.showinfo("Info", "TradingView chart screenshot saved as 'tradingview_chart.png'.")

    # Initialize GUI window
    window = tk.Tk()
    window.title("Stock Pattern Detector")
    window.geometry("400x400")

    # Symbol input
    tk.Label(window, text="Enter Stock Symbol:").pack(pady=5)
    symbol_entry = tk.Entry(window, width=30)
    symbol_entry.pack(pady=5)

    # Days input
    tk.Label(window, text="Enter Number of Past Days to Analyze:").pack(pady=5)
    days_entry = tk.Entry(window, width=10)
    days_entry.pack(pady=5)

    # Analyze button
    analyze_button = tk.Button(window, text="Analyze", command=analyze_stock)
    analyze_button.pack(pady=10)

    # Results display
    result_text = tk.StringVar()
    result_label = tk.Label(window, textvariable=result_text, wraplength=350, justify="left")
    result_label.pack(pady=10)

    # TradingView URL input
    tk.Label(window, text="Enter TradingView Chart URL (optional):").pack(pady=5)
    chart_url_entry = tk.Entry(window, width=50)
    chart_url_entry.pack(pady=5)

    # Open chart button
    chart_button = tk.Button(window, text="Open Chart", command=open_chart)
    chart_button.pack(pady=10)

    # Run the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    main_gui()
