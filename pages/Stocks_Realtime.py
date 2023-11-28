import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

if "isverif" not in st.session_state or st.session_state.isverif == False:
    st.header("ANDA TIDAK MEMPUNYAI AKSES")
    st.subheader("Harap buat akun terlebih dahulu 😊")
else:
    
# Set page title
    st.title("Real-time Stock Analytics")

    # Input stock symbol
    stock_symbol = st.text_input("Enter Stock Symbol", "AAPL")

    # Input time frame
    time_frame = st.slider("Select Time Frame", 1, 100, 5)

    # Input stock start date
    stock_start_date = dt.datetime.now() - dt.timedelta(days=time_frame*365)

    # Function to get stock data
    def get_stock_data(symbol, start_date):
        stock_data = yf.download(symbol, start=start_date, end=dt.datetime.now())
        return stock_data

    # Function to calculate stock metrics
    def calculate_stock_metrics(stock_data):
        stock_data['RSI'] = ((stock_data['Close'].shift(1).fillna(0) - stock_data['Close']) / stock_data['Close']) * 100
        stock_data['RSI'] = stock_data['RSI'].rolling(window=14).mean()
        stock_data['BB_Upper'], stock_data['BB_Middle'], stock_data['BB_Lower'] = calculate_bollinger_bands(stock_data)
        return stock_data

    # Function to calculate Bollinger Bands
    def calculate_bollinger_bands(stock_data):
        rolling_mean = stock_data['Close'].rolling(window=20).mean()
        rolling_std = stock_data['Close'].rolling(window=20).std()
        upper_band = rolling_mean + (rolling_std * 2)
        middle_band = rolling_mean
        lower_band = rolling_mean - (rolling_std * 2)
        return upper_band, middle_band, lower_band

    # Get stock data
    stock_data = get_stock_data(stock_symbol, stock_start_date)

    # Calculate stock metrics
    stock_data = calculate_stock_metrics(stock_data)

    # Plot stock price with Bollinger Bands
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Stock Price'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Upper'], mode='lines', name='Upper Bollinger Band'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Middle'], mode='lines', name='Middle Bollinger Band'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Lower'], mode='lines', name='Lower Bollinger Band'))
    fig.update_layout(title='Stock Price with Bollinger Bands', xaxis_title='Date', yaxis_title='Price')

    # Plot RSI
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], mode='lines', name='RSI'))
    fig2.update_layout(title='Relative Strength Index (RSI)', xaxis_title='Date', yaxis_title='RSI')

    # Display plot
    st.plotly_chart(fig)
    st.plotly_chart(fig2)