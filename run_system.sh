#!/bin/bash
# Run the complete fraud detection system

echo "🛡️  Starting Fraud Detection System"
echo "=================================="
echo ""

# Check if data file exists
if [ ! -f "data/transactions.csv" ]; then
    echo "📝 Initializing transactions.csv..."
    python -c "
import csv
with open('data/transactions.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['transaction_id', 'user_id', 'amount', 'currency', 'location', 'merchant', 'timestamp'])
    writer.writeheader()
"
fi

echo "✓ Data files ready"
echo ""

# Start transaction generator in background
echo "📊 Starting transaction generator..."
python data/sample_transactions_generator.py > /dev/null 2>&1 &
GENERATOR_PID=$!
echo "✓ Generator running (PID: $GENERATOR_PID)"
echo ""

# Wait a moment for initial data
sleep 2

# Start Pathway pipeline in background
echo "🔄 Starting Pathway streaming pipeline..."
python pipeline/main_pipeline.py > logs/pipeline.log 2>&1 &
PIPELINE_PID=$!
echo "✓ Pipeline running (PID: $PIPELINE_PID)"
echo ""

# Wait for pipeline to initialize
sleep 3

# Start dashboard
echo "🎨 Starting Streamlit dashboard..."
echo ""
echo "=================================="
echo "✅ System is running!"
echo "=================================="
echo "• Transaction Generator: PID $GENERATOR_PID"
echo "• Pathway Pipeline: PID $PIPELINE_PID"  
echo "• Dashboard: Starting now..."
echo ""
echo "To stop: Press Ctrl+C"
echo ""

streamlit run dashboard/app.py
