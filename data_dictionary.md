\# Data Dictionary — Mutual Fund Analytics



\## Table: nav\_history (all scheme tables)



| Column | Type | Description |

|--------|------|-------------|

| date | TEXT | NAV date in DD-MM-YYYY format |

| nav | FLOAT | Net Asset Value in INR |

| scheme\_name | TEXT | Name of the mutual fund scheme |

| scheme\_code | INT | Unique AMFI scheme code |



\## Schemes Covered

\- Axis\_Bluechip (119092)

\- HDFC\_Top100\_Direct (125497)

\- ICICI\_Bluechip (120503)

\- Kotak\_Bluechip (120841)

\- Nippon\_LargeCap (118632)

\- SBI\_Bluechip (119551)



\## Source

\- API: mfapi.in

\- Cleaned: duplicates removed, dates parsed, NAV validated

