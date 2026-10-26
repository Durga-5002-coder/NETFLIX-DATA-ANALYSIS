# Netflix Streaming Content: Exploratory Data Analysis (EDA)

## Project Overview

This project performs an end-to-end Exploratory Data Analysis (EDA) on the Netflix Movies and TV Shows dataset using Python. The objective is to analyze content patterns, country-level production hubs, and multi-decade release trajectories using data manipulation and statistical visualization libraries.

## Key Highlights & Insights

* **Content Distribution:** Analyzed the proportion between Movies and TV Shows, identifying the strategic balance of streaming titles across the platform.

* **Global Footprint:** Pinpointed top content-producing nations (led by the United States, India, and the United Kingdom), highlighting geographical content concentrations.

* **Growth Trends:** Mapped historical release patterns from 2000 onwards, capturing explosive catalog expansion during the mid-to-late 2010s.

## Tech Stack & Libraries

* **Language:** Python

* **Data Processing & Wrangling:** Pandas, NumPy

* **Data Visualization:** Matplotlib, Seaborn

## Data Cleaning & Pipeline

1. **Handling Missing Metadata:** Applied contextual imputation for missing values across categorical variables (`country`, `rating`).

2. **Data Consistency:** Removed corrupted and null date entries to ensure accurate time-series trend plotting.

3. **Automated Visualization:** Built automated scripts to generate and save high-resolution distribution plots and categorical bar charts (`.png`).

## Generated Visualizations

* `content_distribution.png`: Comparative volume between Movies and TV Shows.

* `top_countries.png`: Top 10 leading countries by title count.

* `release_trends.png`: Stacked histogram tracking release volume from 2000 to present.

## How to Run Locally

1. **Clone the repository:**

   ```
   git clone https://github.com/[your-username]/netflix-eda-python.git
   cd netflix-eda-python
   
   ```

2. **Install dependencies:**

   ```
   pip install pandas numpy matplotlib seaborn
   
   ```

3. **Execute the analysis script:**

   ```
   python eda.py
   
   ```