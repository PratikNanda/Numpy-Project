import numpy as np
import pandas as pd
import time

def run_telemetry_pipeline():
    print("--- 1. Data Generation Phase ---")
    # We are using 1,000,000 rows so the CSV exports quickly and is easy to open on your machine.
    np.random.seed(42)
    n_rows = 1_000_000 

    # Generate CPU (0-100), Memory (0-64GB), and Latency (0-1000ms)
    cpu_usage = np.random.uniform(0, 100, n_rows)
    mem_usage = np.random.uniform(0, 64, n_rows)
    latency = np.random.uniform(0, 1000, n_rows)

    # Inject 5% missing data (NaN) into CPU
    missing_indices = np.random.choice(n_rows, size=int(n_rows * 0.05), replace=False)
    cpu_usage[missing_indices] = np.nan

    telemetry_data = np.column_stack((cpu_usage, mem_usage, latency))
    print(f"Raw Dataset Shape generated: {telemetry_data.shape}")
    
    # ---------------------------------------------------------
    print("\n--- 2. Preprocessing & Memory Optimization ---")
    
    # Downcast to float32 to save RAM
    telemetry_data = telemetry_data.astype(np.float32)
    
    # Impute missing values with the median
    cpu_median = np.nanmedian(telemetry_data[:, 0]) 
    nan_mask = np.isnan(telemetry_data[:, 0])
    telemetry_data[nan_mask, 0] = cpu_median
    print(f"Cleaned {np.sum(nan_mask)} missing CPU values.")

    # Z-Score Normalization (Standard Scaling)
    means = np.mean(telemetry_data, axis=0)
    stds = np.std(telemetry_data, axis=0)
    normalized_data = (telemetry_data - means) / stds

    # ---------------------------------------------------------
    print("\n--- 3. Vectorized Risk Calculation ---")
    # Risk Score Formula: 40% CPU, 30% Memory, 30% Latency
    weights = np.array([0.4, 0.3, 0.3], dtype=np.float32)
    
    start_time = time.time()
    # Matrix Multiplication for instant calculation
    risk_scores = np.dot(normalized_data, weights) 
    vectorized_time = time.time() - start_time
    print(f"Calculated 1 Million risk scores in: {vectorized_time:.5f} seconds")

    # ---------------------------------------------------------
    print("\n--- 4. Filtering & CSV Export ---")
    # Find the 99th percentile (Top 1% most critical alerts)
    critical_threshold = np.percentile(risk_scores, 99)
    
    # Boolean Masking to filter out normal operations
    critical_mask = risk_scores > critical_threshold
    critical_raw_data = telemetry_data[critical_mask]
    critical_scores = risk_scores[critical_mask]
    
    # Convert ONLY the critical alerts to Pandas for the CSV export
    df_critical = pd.DataFrame(
        critical_raw_data, 
        columns=['CPU_Usage', 'Memory_GB', 'Latency_ms']
    )
    
    # Add the calculated risk score to the final output
    df_critical['Risk_Score'] = np.round(critical_scores, 4)
    df_critical['Status'] = 'Critical Alert'
    
    # Export to CSV
    export_path = "critical_anomalies_report.csv"
    df_critical.to_csv(export_path, index=False)
    
    print(f"Isolated {len(df_critical)} critical alerts.")
    print(f"SUCCESS: Exported data to '{export_path}' in your current folder.")

if __name__ == "__main__":
    run_telemetry_pipeline()