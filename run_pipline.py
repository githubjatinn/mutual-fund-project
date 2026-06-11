"""
run_pipeline.py
Master execution script for Bluestock MF Analytics
Run this to execute the full pipeline end to end.
"""
import subprocess
import sys

def run_step(script, description):
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print('='*50)
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"✓ {description} complete!")

if __name__ == "__main__":
    run_step("live_nav_fetch.py", "Step 1: Fetch live NAV data")
    run_step("data_ingestion.py", "Step 2: Data ingestion")
    run_step("clean_data.py", "Step 3: Clean data")
    run_step("load_to_sqlite.py", "Step 4: Load to SQLite")
    print("\n✓ Full pipeline complete!")