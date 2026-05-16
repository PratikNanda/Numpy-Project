import numpy as np
import pandas as pd

def run_telemetry_pipeline():
    # --- 1. Data Generation Phase ---
    np.random.seed(42)
    n_rows = 1_000_000 

    cpu_usage = np.random.uniform(0, 100, n_rows)
    mem_usage = np.random.uniform(0, 64, n_rows)
    latency = np.random.uniform(0, 1000, n_rows)

    missing_indices = np.random.choice(n_rows, size=int(n_rows * 0.05), replace=False)
    cpu_usage[missing_indices] = np.nan

    telemetry_data = np.column_stack((cpu_usage, mem_usage, latency))
    
    # NEW: Export the RAW data to CSV immediately after generation
    df_raw = pd.DataFrame(telemetry_data, columns=['CPU_Usage', 'Memory_GB', 'Latency_ms'])
    df_raw.to_csv("raw_telemetry_data.csv", index=False)
    print("Exported raw data.")

    # --- 2. Preprocessing & Memory Optimization ---
    telemetry_data = telemetry_data.astype(np.float32)
    
    cpu_median = np.nanmedian(telemetry_data[:, 0]) 
    nan_mask = np.isnan(telemetry_data[:, 0])
    telemetry_data[nan_mask, 0] = cpu_median

    means = np.mean(telemetry_data, axis=0)
    stds = np.std(telemetry_data, axis=0)
    normalized_data = (telemetry_data - means) / stds

    # --- 3. Vectorized Risk Calculation ---
    weights = np.array([0.4, 0.3, 0.3], dtype=np.float32)
    risk_scores = np.dot(normalized_data, weights) 

    # --- 4. Filtering & PROCESSED CSV Export ---
    critical_threshold = np.percentile(risk_scores, 99)
    critical_mask = risk_scores > critical_threshold
    
    critical_raw_data = telemetry_data[critical_mask]
    critical_scores = risk_scores[critical_mask]
    
    df_critical = pd.DataFrame(critical_raw_data, columns=['CPU_Usage', 'Memory_GB', 'Latency_ms'])
    df_critical['Risk_Score'] = np.round(critical_scores, 4)
    df_critical['Status'] = 'Critical Alert'
    
    df_critical.to_csv("critical_anomalies_report.csv", index=False)
    print("Exported processed anomalies data.")

if __name__ == "__main__":
    run_telemetry_pipeline()