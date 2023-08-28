import streamlit as st
import yfinance as yf
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def perform_sentiment_analysis(ticker_symbol):
    # Fetch stock-related news headlines using yfinance
    stock = yf.Ticker(ticker_symbol)
    news_df = pd.DataFrame(stock.news)
    
    
    # Perform sentiment analysis on each news headline
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for headline in news_df['title']:
        sentiment = analyzer.polarity_scores(headline)
        sentiments.append(sentiment)
    
    # Calculate average sentiment scores
    avg_sentiment = {}
    for sentiment in sentiments:
        for key, value in sentiment.items():
            if key in avg_sentiment:
                avg_sentiment[key] += value
            else:
                avg_sentiment[key] = value
    num_headlines = len(sentiments)
    for key in avg_sentiment:
        avg_sentiment[key] /= num_headlines
    
    return avg_sentiment

def plot_major_holders(ticker_symbol):
    # Retrieve data using yfinance
    stock = yf.Ticker(ticker_symbol)
    holders = stock.institutional_holders
    
    # Create a Plotly bar chart
    fig2 = px.bar(holders, x='Holder', y='Shares')
    
    # Customize the chart layout
    fig2.update_layout(
        title=f"Major Institutional Holders of {ticker_symbol}",
        xaxis_title="Holder",
        yaxis_title="Positions",
    )

    # Display the chart
    return fig2





def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    
    # Get today's financial data
    today_data = stock.history(period='1d')
    today_open = today_data['Open'][0]
    today_high = today_data['High'][0]
    today_low = today_data['Low'][0]
    today_volume = today_data['Volume'][0]
    data=yf.download(ticker_input,start=start_date,end=end_date)

    # Draw figure for given date
    fig=px.line(data,x=data.index,y=data['Adj Close'],title=ticker_input)
    fig.update_layout(width=950)

    # mmajor holders
    bar=plot_major_holders(ticker)

    # Get market cap, P/E ratio, and dividend yield
    info = stock.info
    market_cap = info.get('marketCap', 'N/A')
    pe_ratio = info.get('trailingPE', 'N/A')
    div_yield = info.get('dividendYield', 'N/A')
    sector = info.get('sector','N/A')
    industry=info.get('industry','N/A')
    de=info.get('debtToEquity','N/A')
    em=info.get('ebitdaMargins','N/A')
    w=info.get('website','N/A')
    emp=info.get('fullTimeEmployees','N/A')
    ab=info.get('longBusinessSummary','N/A')
    c=info.get('country','N/A')

    #for retriving top employes 
    officer= info.get('companyOfficers', 'N/A')
    officers=pd.DataFrame(officer)

    # Sentiment Analysis 
    sentiment_scores = perform_sentiment_analysis(ticker)

    # Calculate CAGR (Compound Annual Growth Rate)
    data2 = stock.history(period='1y')
    start_price = data2['Close'].iloc[0]
    end_price = data2['Close'].iloc[-1]
    num_periods = len(data2) / 252  # Assuming 252 trading days in a year
    cagr = (end_price / start_price) ** (1 / num_periods) - 1

    # Get recent news headlines
    news = stock.news[:5]
    
    return today_open, today_high, today_low, today_volume, market_cap, pe_ratio, div_yield, news, fig,cagr,sector,sentiment_scores,industry,officers,de,em,bar,w,emp,ab,c



# Start of page Setup
st.set_page_config(
    page_title="Stock Analysis",
    page_icon=":chart:",
    layout="wide",
)

st.title("Stock Analysis")

# Input field for company ticker
ticker_input = st.text_input("Enter Company Ticker (e.g., AAPL)").upper()
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')
msft = yf.Ticker(ticker_input)
button = st.button('Go')

# Retrieve and display stock data
if button:
     # Check if the start date is greater than or equal to the end date
    if start_date >= end_date:
        st.error("Error: Start date must be earlier than the end date.")
    else:
        today_open, today_high, today_low, today_volume, market_cap, pe_ratio, div_yield, news, fig ,cagr,sector,sentiment_scores,industry,officers,de,em,bar,w,emp,ab,c= get_stock_data(ticker_input)
    if start_date == end_date:
            st.error("Error: Start date and end date for the graph cannot be the same.")
    else:        
        st.subheader("Graph")
        st.plotly_chart(fig)
        with st.expander("About"):
        
            st.write("Ticker:", ticker_input)
            st.write("Sector:",sector)
            st.write("Industry:",industry)
            st.write("Country:",c)
            st.write("Website:",w)
            st.write("Full time Employees:",emp)
            st.subheader("summary")
            st.write(ab)
        st.write("--------------------------")
        st.subheader("Today's Financial Data")
        st.write("Today's Open:", today_open)
        st.write("Today's High:", today_high)
        st.write("Today's Low:", today_low)
        st.write("Today's Volume:", today_volume)
        st.write("--------------------------")
        st.subheader("Total Analysis")
        st.write("Market Cap:", market_cap)
        st.write("P/E Ratio:", pe_ratio)
        st.write("Dividend Yield:", div_yield)
        st.write("One Year CAGR:",cagr)
        st.write("Debt To Equity Ratio:",de)
        st.write("Ebidta Margin:",em)
        st.write("--------------------------")
        st.subheader("Sentiment Analysis")
        st.write("Sentiment Scores for", ticker_input + ":")
        for key, value in sentiment_scores.items():
            st.write(key + ":", value)
   
    # To create tabs
        actions,newss,officerss,holder = st.tabs(["Actions"," RecentNews"," TopEmployees"," Holders"])

    # Perform operation on tabs
        with actions:
            st.subheader("Actions")
            st.write("", msft.actions)

        with newss:
            st.subheader("Recent News")
            for article in news:
                st.write("Headline:", article.get('title'))
                st.write("Publisher:", article.get('publisher'))
                st.write("URL:", article.get('link'))
                st.write("---")
    
        with officerss:
            st.subheader("Top employees")
            st.write(officers)
    
        with holder:
            st.subheader("MAJOR HOLDERS")
            st.write(bar)
