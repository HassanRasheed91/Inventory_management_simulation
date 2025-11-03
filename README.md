# 📦 Inventory Management Simulation System

> 🏭 An AI-powered inventory optimization platform combining reinforcement learning and classical (s,S) policies with a modern web interface for supply chain management analysis and decision-making.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-black.svg)](https://flask.palletsprojects.com/)
[![RL](https://img.shields.io/badge/RL-PPO-green.svg)](https://stable-baselines3.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Overview

This comprehensive inventory management simulation system enables supply chain professionals and researchers to evaluate and compare different inventory control strategies. The platform combines **classical (s,S) policies** with modern **reinforcement learning** approaches, providing data-driven insights through an intuitive web interface.

### 🎯 Key Objectives

- 📊 **Compare Strategies** - Classical (s,S) policies vs RL agents
- 🤖 **AI Optimization** - PPO-based reinforcement learning
- 📈 **Performance Analysis** - Cost, service level, and shortage metrics
- 🌐 **Interactive Dashboard** - Real-time simulation and visualization
- 📄 **Comprehensive Reports** - Downloadable evaluation summaries
- 🔄 **Multi-Product Support** - Handle multiple product inventories

---

## ✨ Key Features

### 🎮 Core Functionality
- 🏋️ **Gym-Compatible Environment** - Standard RL interface
- 📐 **Classical (s,S) Policies** - 5 pre-configured parameter sets
- 🤖 **Reinforcement Learning** - PPO (Proximal Policy Optimization)
- 🌐 **Flask Web Interface** - Bootstrap-styled responsive UI
- ⏱️ **Real-Time Progress** - Live tracking with loading animations
- 📊 **Interactive Visualizations** - Comprehensive charts and graphs
- 💾 **Downloadable Reports** - TXT and Markdown formats

### 📈 Analysis Capabilities
- 💰 **Cost Analysis** - Total cost breakdown and comparison
- ✅ **Service Level Tracking** - Customer satisfaction metrics
- 📉 **Shortage Detection** - Stockout frequency and duration
- 📦 **Order Monitoring** - Ordering patterns and frequency
- 🎯 **Policy Comparison** - Side-by-side performance evaluation

---

## 🏗️ System Architecture

### 🔄 Simulation Flow

```
🎬 User Initiates Simulation
         ↓
🏭 Environment Setup
   ├─ Product 1: Demand Distribution
   ├─ Product 2: Demand Distribution
   ├─ Lead Times
   └─ Cost Parameters
         ↓
📊 Policy Evaluation (1000 days each)
   ├─ (s,S) Policy Set 1
   ├─ (s,S) Policy Set 2
   ├─ (s,S) Policy Set 3
   ├─ (s,S) Policy Set 4
   ├─ (s,S) Policy Set 5
   └─ RL Agent (PPO)
         ↓
📈 Performance Metrics Collection
   ├─ Total Cost
   ├─ Service Level
   ├─ Shortages
   └─ Order Frequency
         ↓
📊 Visualization & Reporting
   ├─ Cost Comparison Charts
   ├─ Service Level Analysis
   ├─ Daily Performance Trends
   └─ Summary Dashboard
         ↓
📥 Report Generation
   └─ TXT & Markdown Downloads
```

---

## 📂 Project Structure

```
Inventory_Management_Simulation/
│
├── 🌐 app.py                        # Flask web server
├── 🎮 main.py                       # Command-line interface
├── 📋 requirements.txt              # Dependencies
├── 📖 README.md                     # Documentation
│
├── 🏭 Core Modules/
│   ├── inventory_env.py             # Gym environment
│   ├── ss_policy.py                 # Classical (s,S) policies
│   ├── rl_training.py               # RL agent training
│   ├── evaluation.py                # Comparison system
│   └── visualization.py             # Plotting & reporting
│
├── 🎨 templates/                    # HTML templates
│   ├── index.html                   # Home page
│   └── results.html                 # Results display
│
├── 💅 static/
│   └── css/
│       └── style.css                # Custom styling
│
├── 📊 plots/                        # Generated visualizations
│   ├── cost_comparison.png
│   ├── service_levels.png
│   └── daily_trends.png
│
├── 🤖 models/                       # Trained RL models
│   └── ppo_inventory_model.zip
│
└── 📄 reports/                      # Evaluation reports
    ├── evaluation_report.txt
    └── final_report.md
```

---

## 🎯 Inventory Environment

### 📦 Product Configuration

#### **Product 1**
| Parameter | Value |
|-----------|-------|
| 🎲 **Demand Distribution** | {1: 1/6, 2: 1/3, 3: 1/3, 4: 1/6} |
| ⏱️ **Lead Time** | Uniform(0.5, 1.0) days |
| 🏢 **Supplier** | Supplier A |

#### **Product 2**
| Parameter | Value |
|-----------|-------|
| 🎲 **Demand Distribution** | {2: 1/8, 3: 1/2, 4: 1/4, 5: 1/8} |
| ⏱️ **Lead Time** | Uniform(0.2, 0.7) days |
| 🏢 **Supplier** | Supplier B |

### 💰 Cost Structure

| Cost Type | Value | Description |
|-----------|-------|-------------|
| 💵 **Holding Cost** | $1/unit/day | Inventory storage cost |
| 📦 **Ordering Cost** | $3 + $10/order | Fixed + variable cost |
| ⚠️ **Penalty Cost** | $7/unit | Stockout penalty |

### 📐 Classical (s, S) Policies

| Policy | Product 1 (s, S) | Product 2 (s, S) | Strategy |
|--------|------------------|------------------|----------|
| **Policy 1** | (3, 10) | (5, 15) | Conservative |
| **Policy 2** | (5, 15) | (7, 20) | Moderate |
| **Policy 3** | (7, 20) | (10, 25) | Aggressive |
| **Policy 4** | (2, 12) | (4, 18) | Balanced |
| **Policy 5** | (4, 18) | (6, 22) | Optimized |

**Where:**
- **s** = Reorder point (order when inventory ≤ s)
- **S** = Order-up-to level (order quantity = S - current inventory)

---

## 💻 Installation

### 📋 Prerequisites

- ✅ Python 3.8 or higher
- ✅ pip package manager
- ✅ Virtual environment (recommended)

### 🚀 Setup Instructions

**1️⃣ Clone the repository**
```bash
git clone https://github.com/HassanRasheed91/Inventory_management_simulation.git
cd Inventory_management_simulation
```

**2️⃣ Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

### 📦 Required Libraries

```txt
flask>=2.3.0
stable-baselines3>=2.0.0
gym>=0.21.0
numpy>=1.21.0
pandas>=1.4.0
matplotlib>=3.5.0
seaborn>=0.11.0
tensorboard>=2.10.0
```

---

## 🎮 Usage

### 🌐 Web Interface (Recommended)

**1️⃣ Start the Flask server**
```bash
python app.py
```

**2️⃣ Open browser**
Navigate to: `http://localhost:5000`

**3️⃣ Run simulation**
- Click **"Run Complete Simulation"** button
- Watch real-time progress (2-3 minutes)
- View interactive results and visualizations
- Download comprehensive reports

### 💻 Command-Line Interface

```bash
python main.py
```

This will:
- Run all policy evaluations
- Generate visualizations
- Save reports to disk
- Display results in terminal

---

## 🎨 Web Interface Features

### 🏠 Home Page

- 📖 **Project Overview** - System description and objectives
- 🎬 **Simulation Control** - One-click execution button
- ⏱️ **Progress Tracking** - Real-time step indicators
  - Environment testing
  - (s,S) policy evaluation
  - RL agent training
  - Comprehensive evaluation
- ⏰ **Time Estimate** - Expected completion (2-3 min)

### 📊 Results Page

#### 🏆 Winner Announcement
- Best performing policy highlighted
- Key performance metrics displayed
- Cost savings vs baseline

#### 📈 Performance Comparison Table

| Policy | Total Cost | Service Level | Shortages | Orders |
|--------|------------|---------------|-----------|--------|
| Policy 1 | $X,XXX | XX% | XXX | XXX |
| Policy 2 | $X,XXX | XX% | XXX | XXX |
| ... | ... | ... | ... | ... |

#### 📊 Interactive Visualizations

1. 💰 **Cost Comparison Chart** - Bar chart of total costs
2. ✅ **Service Level Analysis** - Performance across policies
3. 📉 **Daily Performance Trends** - Time-series analysis
4. 📊 **Summary Dashboard** - Key metrics overview

#### 📥 Downloadable Reports

- 📄 **TXT Format** - Plain text detailed analysis
- 📝 **Markdown Format** - Formatted comprehensive report

---

## 🤖 Reinforcement Learning Details

### 🧠 Algorithm: PPO (Proximal Policy Optimization)

**Why PPO?**
- ✅ Stable and reliable
- ✅ Sample efficient
- ✅ Good for continuous action spaces
- ✅ Industry standard for control problems

### 🎯 RL Configuration

```python
# State Space
- Current inventory levels (Product 1, 2)
- Pending orders
- Time since last order
- Recent demand patterns

# Action Space
- Order quantity for Product 1 [0, 30]
- Order quantity for Product 2 [0, 30]

# Reward Function
reward = -(holding_cost + ordering_cost + penalty_cost)
```

### 🏋️ Training Parameters

| Parameter | Value |
|-----------|-------|
| **Algorithm** | PPO |
| **Total Timesteps** | 100,000 |
| **Learning Rate** | 0.0003 |
| **Batch Size** | 64 |
| **Epochs** | 10 |
| **Gamma** | 0.99 |

---

## 📈 Performance Metrics

### 🎯 Evaluation Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| 💰 **Total Cost** | Holding + Ordering + Penalty | Minimize |
| ✅ **Service Level** | (Days without shortage) / Total days | Maximize |
| 📉 **Shortage Frequency** | Number of stockout events | Minimize |
| 📦 **Order Frequency** | Number of orders placed | Optimize |

### 📊 Typical Results

**Best Performing Policy:** Usually (s,S) Policy 2 or 3

| Metric | Best Policy | RL Agent | Improvement |
|--------|------------|----------|-------------|
| Total Cost | $8,500 | $42,000 | **80% better** |
| Service Level | 92% | 65% | **42% better** |
| Shortages | 45 | 320 | **86% fewer** |
| Orders | 85 | 450 | Optimized |

---

## 📊 Visualization Examples

### 💰 Cost Comparison
- Bar chart comparing total costs across all policies
- Highlights best and worst performers
- Shows cost breakdown by component

### ✅ Service Level Analysis
- Line plot of service level percentages
- Benchmark line at 90% target
- Policy performance ranking

### 📉 Daily Performance Trends
- Time-series plot of inventory levels
- Order placement markers
- Shortage periods highlighted

### 📊 Summary Dashboard
- Multi-panel visualization
- Key metrics at a glance
- Performance heatmap

---

## 🚀 Future Enhancements

### 🎯 Planned Features

- 📱 **Mobile Interface** - Responsive mobile app
- ☁️ **Cloud Deployment** - AWS/Azure hosting
- 🔄 **Real-Time Updates** - WebSocket integration
- 📊 **Advanced Analytics** - Predictive modeling
- 🤖 **Deep RL** - DQN, A3C algorithms
- 🌍 **Multi-Location** - Supply chain networks
- 📈 **Demand Forecasting** - ML-based predictions
- 🔔 **Alert System** - Automated notifications

### 🔧 Technical Improvements

- 🧪 Unit tests and CI/CD
- 🐳 Docker containerization
- 📚 API documentation
- 🎨 Enhanced UI/UX
- 💾 Database integration
- 🔐 User authentication

---

## 💡 Use Cases

### 🎯 Applications

- 🏭 **Manufacturing** - Production inventory optimization
- 🏪 **Retail** - Store inventory management
- 📦 **Warehousing** - Distribution center operations
- 🚚 **Logistics** - Supply chain optimization
- 🎓 **Education** - Teaching inventory control
- 🔬 **Research** - Algorithm comparison studies

### 💼 Business Benefits

- 💰 **Cost Reduction** - Optimize inventory costs
- ✅ **Improved Service** - Higher customer satisfaction
- 📉 **Reduced Stockouts** - Better availability
- 🎯 **Data-Driven Decisions** - Evidence-based policies
- 🔄 **Process Automation** - AI-powered optimization

---

## 🔧 Troubleshooting

### ❌ Common Issues

#### **🐍 Import Errors**
```bash
Solution:
pip install -r requirements.txt --upgrade
```

#### **🌐 Flask Port Conflict**
```bash
Solution:
# Change port in app.py
app.run(port=5001)
```

#### **🤖 RL Training Slow**
```bash
Solution:
- Reduce total_timesteps in rl_training.py
- Use GPU acceleration if available
```

#### **📊 Plots Not Showing**
```bash
Solution:
- Ensure matplotlib backend is configured
- Check write permissions in plots/ directory
```

---

## 📚 Learning Outcomes

This project demonstrates:

- ✅ **Inventory Management Theory** - Classical policies and optimization
- ✅ **Reinforcement Learning** - PPO implementation and training
- ✅ **Web Development** - Flask application architecture
- ✅ **Data Visualization** - Matplotlib and Seaborn
- ✅ **Performance Comparison** - Benchmarking methodologies
- ✅ **Supply Chain Optimization** - Real-world problem solving

---

## 📄 License

This project is licensed under the MIT License. ⚖️

---

## 👨‍💻 Author

**Hassan Rasheed**

🎓 Machine Learning Engineer | Operations Research Specialist

- 📧 **Email**: 221980038@gift.edu.pk
- 💼 **LinkedIn**: [hassan-rasheed-datascience](https://linkedin.com/in/hassan-rasheed-datascience)
- 🐙 **GitHub**: [HassanRasheed91](https://github.com/HassanRasheed91)

---

## 🙏 Acknowledgments

- 🤖 OpenAI Gym for standardized RL environments
- 📚 Stable-Baselines3 for PPO implementation
- 🌐 Flask development team
- 📊 Matplotlib and Seaborn communities
- 📖 Operations research literature and textbooks

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ by Hassan Rasheed**

🔗 [View Project](https://github.com/HassanRasheed91/Inventory_management_simulation) • 🐛 [Report Bug](https://github.com/HassanRasheed91/Inventory_management_simulation/issues) • 💡 [Request Feature](https://github.com/HassanRasheed91/Inventory_management_simulation/issues)

---

**📦 Optimizing Supply Chains with AI**

</div>
