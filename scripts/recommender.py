import pandas as pd

def recommend_funds(risk_appetite, scorecard_path, var_path):
    scores = pd.read_csv(scorecard_path)
    var = pd.read_csv(var_path)
    merged = scores.merge(var, on='scheme')
    
    if risk_appetite.lower() == 'low':
        result = merged.nlargest(3, 'VaR_95%')
    elif risk_appetite.lower() == 'high':
        result = merged.nlargest(3, 'Sharpe_Ratio')
    else:
        result = merged.nlargest(3, 'score_100')
    
    print(f"\nTop 3 funds for {risk_appetite} risk:")
    print(result[['scheme','score_100','Sharpe_Ratio','VaR_95%']].to_string(index=False))

if __name__ == "__main__":
    s = r"reports\fund_scorecard.csv"
    v = r"reports\var_cvar_report.csv"
    recommend_funds('Low', s, v)
    recommend_funds('Moderate', s, v)
    recommend_funds('High', s, v)