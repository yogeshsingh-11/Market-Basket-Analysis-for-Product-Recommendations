# Market Basket Analysis for Product Recommendation

## 📌 Project Overview
This project implements **Market Basket Analysis (MBA)** and **RFM (Recency, Frequency, Monetary) Analysis** to generate **product recommendations** based on customer purchasing behavior. The dataset consists of transaction records, including invoice numbers, stock codes, product descriptions, quantities, and customer IDs.

## 🏗️ Directory Structure
```
market-basket-analysis/
│── data/
│   ├── online_retail.csv  # Dataset
│
│── notebooks/
│   ├── data_preprocessing.ipynb  # Cleaning and preprocessing
│   ├── market_basket_analysis.ipynb  # Applying MBA (Apriori algorithm)
│   ├── rfm_analysis.ipynb  # Customer segmentation using RFM
│
│── src/
│   ├── data_loader.py  # Loads and preprocesses data
│   ├── mba_model.py  # Apriori-based Market Basket Analysis
│   ├── rfm_model.py  # RFM segmentation implementation
│
│── app/
│   ├── app.py  # Flask-based web interface for recommendations
│
│── README.md
│── requirements.txt  # Dependencies
```

## 🔧 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/market-basket-analysis.git
   cd market-basket-analysis
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run Jupyter Notebook** (optional for interactive exploration)
   ```sh
   jupyter notebook
   ```

## 📊 Data Preprocessing
- **Handling missing values**: Removed rows with null CustomerID.
- **Filtering data**: Kept only valid transactions (positive quantity & unit price).
- **Encoding transactions**: Transformed data into a format for association rule mining.

## 🛒 Market Basket Analysis (MBA)
- **Algorithm Used**: Apriori
- **Key Steps**:
  - Created transactional datasets grouped by invoices.
  - Applied **Apriori** algorithm to find frequent itemsets.
  - Generated **association rules** using **support, confidence, and lift**.
- **Output**: Product recommendations based on frequently bought items together.

## 🎯 RFM Analysis for Customer Segmentation
- **Metrics Used**:
  - **Recency (R)**: Days since last purchase.
  - **Frequency (F)**: Total transactions.
  - **Monetary (M)**: Total amount spent.
- **Clustering**: Customers were segmented into groups based on RFM scores.
- **Use Case**: Personalized recommendations for different customer segments.


## 📜 License
This project is **MIT licensed**. Feel free to use and modify it.
