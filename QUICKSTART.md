# 🚀 QUICK START GUIDE

## ✅ System Status Check

Run this to verify everything is set up:
```bash
python test_features.py
```

Expected output: "🎉 ALL TESTS PASSED!"

---

## 🎯 Running the System

### Method 1: Automated Start (Recommended)
```bash
./run_system.sh
```

This will:
1. Start the transaction generator
2. Start the Pathway streaming pipeline
3. Launch the Streamlit dashboard

### Method 2: Manual Start (For Development)

**Terminal 1: Start Pipeline**
```bash
python pipeline/main_pipeline.py
```

Expected output:
```
🚀 STARTING CONTINUOUS PROCESSING
Pipeline is now running...
• New transactions will be processed automatically
• Output files update in real-time
```

**Terminal 2: Start Dashboard**
```bash
streamlit run dashboard/app.py
```

**Terminal 3: Add Test Transactions (Optional)**
```bash
# Add a normal transaction
echo "txn_TEST1,u_001,500,USD,US,grocery,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv

# Add a high-risk transaction (large amount)
echo "txn_TEST2,u_001,5000,USD,RU,electronics,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv

# Wait 2-3 seconds and check the dashboard!
```

---

## 📊 Dashboard Features to Verify

### 1️⃣ **Live Risk Score Meter**
- Look for the circular gauge chart at the top
- Color should change based on risk:
  - Green (0-0.4)
  - Yellow (0.4-0.7)
  - Red (0.7-1.0)

### 2️⃣ **Risk Score Breakdown Table**
- Shows latest transaction's feature triggers
- Three rows: Large Amount, Rapid Transactions, Location Change
- ✅ or ❌ in "Triggered" column
- Weight and Description columns

### 3️⃣ **Real-Time Fraud Trend Graph**
- Two charts side-by-side:
  - Left: Risk score over time (line chart)
  - Right: Fraud count per minute (bar chart)
- Color-coded points based on risk level
- Threshold line at 0.7

---

## 🧪 Testing Streaming Behavior

### Test 1: Verify Auto-Detection
```bash
# While pipeline is running, add a transaction:
echo "txn_999,u_001,8888,USD,RU,gaming,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv

# Check the pipeline log (should see within 1 second):
tail -f logs/pipeline.log
```

Expected: `FileSystem(data/transactions.csv): 1 entries have been sent to the engine`

### Test 2: Verify Dashboard Updates
1. Open dashboard in browser
2. Add transaction using command above
3. Wait 2-3 seconds
4. Dashboard should show new data (auto-refresh every 2s)

### Test 3: Verify Stateful Computation
```bash
# Add 3 transactions for same user rapidly:
echo "txn_T1,u_TEST,100,USD,US,gaming,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv
sleep 0.5
echo "txn_T2,u_TEST,200,USD,US,gaming,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv
sleep 0.5
echo "txn_T3,u_TEST,300,USD,US,gaming,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv

# Check alerts (should trigger rapid-fire detection):
tail -3 data/alerts.csv
```

---

## 📈 Pathway Requirements Verification

### ✅ A. Streaming Ingestion
```bash
# Verify mode="streaming" in code:
grep -A 3 "mode=" ingestion/stream_ingestion.py
```

### ✅ B. Pathway Transformations
```bash
# Verify no pandas operations in pipeline:
grep -r "pd\." pipeline/ features/ scoring/ | grep -v "__pycache__" | wc -l
```
Expected: 0 (no pandas in streaming code)

### ✅ C. Stateful Computation
```bash
# Verify reducers usage:
grep "reducers\." features/feature_engineering.py
```
Expected: `pw.reducers.avg` and `pw.reducers.count`

### ✅ D. Continuous Output
```bash
# Verify pw.run() is called:
grep "pw.run()" pipeline/main_pipeline.py
```

---

## 🐛 Troubleshooting

### Pipeline not starting?
```bash
# Check logs:
cat logs/pipeline.log

# Common issues:
# - CSV file has wrong format → Check headers match schema
# - Port already in use → Kill existing processes: pkill -f pipeline
```

### Dashboard not showing data?
```bash
# Verify output files exist and have data:
ls -lh data/*.csv
head -2 data/scored_transactions.csv

# Verify pipeline is running:
ps aux | grep pipeline
```

### Changes not reflected?
```bash
# Dashboard auto-refreshes every 2 seconds
# Or click "Refresh Now" button manually

# Verify pipeline is processing:
tail -f logs/pipeline.log
```

---

## 📝 Key Files

- **Pipeline:** `pipeline/main_pipeline.py`
- **Dashboard:** `dashboard/app.py`
- **Config:** `config/settings.py`
- **Tests:** `test_features.py`
- **Logs:** `logs/pipeline.log`

---

## 🎬 Demo Script for Judges

1. **Show Setup:**
   ```bash
   python test_features.py
   ```

2. **Start System:**
   ```bash
   python pipeline/main_pipeline.py &
   streamlit run dashboard/app.py
   ```

3. **Demonstrate Streaming:**
   ```bash
   # Add high-risk transaction:
   echo "txn_DEMO,u_001,9999,USD,RU,gaming,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv
   
   # Show dashboard updates (within 2-3 seconds)
   # Point out:
   # - Risk Score Meter turns RED
   # - Breakdown Table shows "Large Amount" ✅
   # - Trend Graph shows new spike
   # - Alert appears in alerts table
   ```

4. **Highlight Features:**
   - 🎯 **Gauge Meter:** Visual risk indicator
   - 🔍 **Breakdown Table:** Explainability
   - 📈 **Trend Graph:** Streaming behavior

5. **Show No Restart Needed:**
   ```bash
   # Pipeline still running from step 2
   echo "txn_DEMO2,u_002,7777,USD,IN,gaming,$(date -u +%Y-%m-%dT%H:%M:%S)" >> data/transactions.csv
   # Automatically processed! No restart!
   ```

---

## ✨ What Makes This Submission Stand Out

### 1. **Full Pathway Compliance**
- ✅ Streaming mode CSV connector
- ✅ All transformations in Pathway (no pandas)
- ✅ Stateful/incremental computation
- ✅ Continuous auto-updating output

### 2. **Three New Features**
- 🎯 **Visual Risk Meter:** Intuitive gauge chart
- 🔍 **Explainable AI:** Feature breakdown table
- 📈 **Live Trends:** Real-time visualization

### 3. **Professional Quality**
- Clean architecture
- Comprehensive documentation
- Easy to test and demonstrate
- Production-ready patterns

### 4. **Judge-Friendly**
- Quick start scripts
- Automated testing
- Clear verification steps
- Demo-ready

---

## 🏆 Hackathon Checklist

- [x] Real-time streaming ingestion (Pathway CSV connector)
- [x] Streaming transformations (No pandas in pipeline)
- [x] Stateful/incremental computation (reducers)
- [x] Continuous output (auto-updating files)
- [x] Live Risk Score Meter (NEW)
- [x] Risk Score Breakdown Table (NEW)
- [x] Real-Time Fraud Trend Graph (NEW)
- [x] Documentation & testing
- [x] Demo-ready system

---

**Ready to impress the judges! 🚀**
