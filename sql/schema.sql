-- Bluestock Mutual Fund Analytics Schema

CREATE TABLE IF NOT EXISTS nav_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    nav REAL NOT NULL,
    scheme_name TEXT NOT NULL,
    scheme_code INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS fund_scorecard (
    scheme TEXT PRIMARY KEY,
    CAGR_3yr REAL,
    Sharpe_Ratio REAL,
    Alpha REAL,
    Max_Drawdown REAL,
    score_100 REAL
);

CREATE TABLE IF NOT EXISTS alpha_beta (
    scheme TEXT PRIMARY KEY,
    Alpha REAL,
    Beta REAL,
    Max_Drawdown_pct REAL
);

CREATE TABLE IF NOT EXISTS var_cvar (
    scheme TEXT PRIMARY KEY,
    VaR_95 REAL,
    CVaR_95 REAL
);