import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from preprocess import load_data

def prepare_basket(df):
    """Convert dataset into a basket format suitable for Market Basket Analysis."""
    basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)

    # Convert to binary (0/1)
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    return basket

def apply_apriori(basket, min_support=0.01, min_threshold=1.0):
    """Apply Apriori algorithm and generate association rules."""
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
    
    return rules.sort_values(by="lift", ascending=False)

if __name__ == "__main__":
    df = load_data("../data/retail_data.csv")
    basket = prepare_basket(df)
    rules = apply_apriori(basket)

    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

