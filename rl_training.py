import numpy as np
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold
from stable_baselines3.common.monitor import Monitor
import os
from typing import Dict, Any
from inventory_env import InventoryEnv


def train_ppo_agent(env: InventoryEnv, total_timesteps: int = 10000, 
                   save_path: str = "models/ppo_inventory") -> PPO:
    """
    Train a PPO agent for inventory management
    
    Args:
        env: Inventory environment
        total_timesteps: Number of training timesteps
        save_path: Path to save the trained model
        
    Returns:
        Trained PPO agent
    """
    print("Training PPO agent...")
    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=1e-4,        
        n_steps=2048,             
        batch_size=128,          
        n_epochs=10,             
        gamma=0.995,           
        gae_lambda=0.95,
        clip_range=0.2,
        ent_coef=0.05,          
        vf_coef=0.5,
        max_grad_norm=0.5,
        policy_kwargs=dict(
            net_arch=[256, 256, 128]  
        )
    )
    
    save_dir = os.path.dirname(save_path)
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
    
    model.learn(total_timesteps=total_timesteps)
    model.save(save_path)
    print(f"PPO model saved to {save_path}")
    
    return model




def evaluate_agent(model, env: InventoryEnv, days: int = 1000) -> Dict[str, Any]:
    """
    Evaluate a trained agent
    
    Args:
        model: Trained RL model
        env: Inventory environment
        days: Number of days to evaluate
        
    Returns:
        Dictionary containing evaluation metrics
    """
    print(f"Evaluating agent for {days} days...")
    obs, _ = env.reset()
    
    # Track metrics
    daily_costs = []
    daily_shortages = []
    daily_orders = []
    daily_stock_levels = []
    total_reward = 0
    
    # Track enhanced reward components
    daily_base_rewards = []
    daily_service_bonuses = []
    daily_shortage_penalties = []
    daily_ordering_bonuses = []
    daily_total_rewards = []
    
    # Per-product tracking
    daily_costs_product1 = []
    daily_costs_product2 = []
    daily_shortages_product1 = []
    daily_shortages_product2 = []
    daily_orders_product1 = []
    daily_orders_product2 = []
    
    for day in range(days):
        # Get action from model
        action, _ = model.predict(obs, deterministic=True)
        
        # Execute action
        obs, reward, done, truncated, info = env.step(action)
        total_reward += reward
        
        # Track overall metrics
        daily_costs.append(info['daily_cost'])
        daily_shortages.append(info['shortage1'] + info['shortage2'])
        daily_orders.append(info['order1'] + info['order2'])
        daily_stock_levels.append(obs.copy())
        
        # Track enhanced reward components
        daily_base_rewards.append(info['base_reward'])
        daily_service_bonuses.append(info['service_level_bonus'])
        daily_shortage_penalties.append(info['shortage_penalty'])
        daily_ordering_bonuses.append(info['ordering_bonus'])
        daily_total_rewards.append(info['total_reward'])
        
        # Track per-product metrics
        daily_costs_product1.append(info['daily_cost_product1'])
        daily_costs_product2.append(info['daily_cost_product2'])
        daily_shortages_product1.append(info['shortage1'])
        daily_shortages_product2.append(info['shortage2'])
        daily_orders_product1.append(info['order1'])
        daily_orders_product2.append(info['order2'])
        
        if (day + 1) % 100 == 0:
            print(f"Day {day + 1}: Stock={obs}, Action={action}, "
                  f"Cost={info['daily_cost']:.2f}, Reward={info['total_reward']:.2f}, "
                  f"ServiceBonus={info['service_level_bonus']:.2f}, OrderBonus={info['ordering_bonus']:.2f}")
    
    # Calculate summary metrics
    total_cost = sum(daily_costs)
    average_daily_cost = np.mean(daily_costs)
    total_shortages = sum(daily_shortages)
    average_shortages = np.mean(daily_shortages)
    total_orders = sum(daily_orders)
    average_orders = np.mean(daily_orders)
    
    # Calculate per-product metrics
    total_cost_product1 = sum(daily_costs_product1)
    total_cost_product2 = sum(daily_costs_product2)
    average_daily_cost_product1 = np.mean(daily_costs_product1)
    average_daily_cost_product2 = np.mean(daily_costs_product2)
    total_shortages_product1 = sum(daily_shortages_product1)
    total_shortages_product2 = sum(daily_shortages_product2)
    total_orders_product1 = sum(daily_orders_product1)
    total_orders_product2 = sum(daily_orders_product2)
    
    # Calculate service level
    service_level = (days - sum(1 for s in daily_shortages if s > 0)) / days * 100
    service_level_product1 = (days - sum(1 for s in daily_shortages_product1 if s > 0)) / days * 100
    service_level_product2 = (days - sum(1 for s in daily_shortages_product2 if s > 0)) / days * 100
    
    return {
        'total_cost': total_cost,
        'average_daily_cost': average_daily_cost,
        'total_shortages': total_shortages,
        'average_shortages': average_shortages,
        'total_orders': total_orders,
        'average_orders': average_orders,
        'service_level': service_level,
        'total_reward': total_reward,
        'days_simulated': days,
        'daily_costs': daily_costs,
        'daily_shortages': daily_shortages,
        'daily_orders': daily_orders,
        'daily_stock_levels': daily_stock_levels,
        
        # Enhanced reward components
        'daily_base_rewards': daily_base_rewards,
        'daily_service_bonuses': daily_service_bonuses,
        'daily_shortage_penalties': daily_shortage_penalties,
        'daily_ordering_bonuses': daily_ordering_bonuses,
        'daily_total_rewards': daily_total_rewards,
        
        # Per-product metrics
        'total_cost_product1': total_cost_product1,
        'total_cost_product2': total_cost_product2,
        'average_daily_cost_product1': average_daily_cost_product1,
        'average_daily_cost_product2': average_daily_cost_product2,
        'total_shortages_product1': total_shortages_product1,
        'total_shortages_product2': total_shortages_product2,
        'total_orders_product1': total_orders_product1,
        'total_orders_product2': total_orders_product2,
        'service_level_product1': service_level_product1,
        'service_level_product2': service_level_product2,
        'daily_costs_product1': daily_costs_product1,
        'daily_costs_product2': daily_costs_product2,
        'daily_shortages_product1': daily_shortages_product1,
        'daily_shortages_product2': daily_shortages_product2,
        'daily_orders_product1': daily_orders_product1,
        'daily_orders_product2': daily_orders_product2
    }


def train_and_evaluate_agents():
    """
    Train PPO agent and evaluate its performance
    """
    print("Starting RL Agent Training and Evaluation")
    print("="*50)
    
    # environment
    env = InventoryEnv()
    
    training_timesteps = 15000  
    
    # PPO agent
    print("\n1. Training PPO Agent")
    print("-" * 30)
    ppo_model = train_ppo_agent(env, training_timesteps)
    
    print("\n2. Evaluating PPO Agent")
    print("-" * 30)
    ppo_metrics = evaluate_agent(ppo_model, env, days=1000)
    
    # summary
    print("\n3. Performance Summary")
    print("-" * 30)
    print(f"{'Metric':<20} {'PPO':<15}")
    print("-" * 35)
    print(f"{'Total Cost':<20} {ppo_metrics['total_cost']:<15.2f}")
    print(f"{'Avg Daily Cost':<20} {ppo_metrics['average_daily_cost']:<15.2f}")
    print(f"{'Total Shortages':<20} {ppo_metrics['total_shortages']:<15}")
    print(f"{'Service Level %':<20} {ppo_metrics['service_level']:<15.1f}")
    print(f"{'Total Orders':<20} {ppo_metrics['total_orders']:<15}")
    
    # Per-product analysis
    print(f"\nPer-Product Analysis:")
    print(f"{'Metric':<20} {'PPO':<15}")
    print("-" * 35)
    print(f"{'Product 1 Cost':<20} {ppo_metrics['total_cost_product1']:<15.2f}")
    print(f"{'Product 2 Cost':<20} {ppo_metrics['total_cost_product2']:<15.2f}")
    print(f"{'Product 1 Service %':<20} {ppo_metrics['service_level_product1']:<15.1f}")
    print(f"{'Product 2 Service %':<20} {ppo_metrics['service_level_product2']:<15.1f}")
    
    print(f"\nPPO Agent Performance Summary:")
    print(f"Total Cost: {ppo_metrics['total_cost']:.2f}")
    print(f"Service Level: {ppo_metrics['service_level']:.1f}%")
    
    # Save the PPO model 
    ppo_model.save("inventory_agent")
    print("PPO model saved as 'inventory_agent.zip'")
    
    return {
        'ppo_model': ppo_model,
        'ppo_metrics': ppo_metrics,
        'best_model': ppo_model,
        'best_metrics': ppo_metrics,
        'best_name': 'PPO'
    }

def test_trained_agent():
    """Test a trained agent with a short simulation"""
    print("Testing Trained Agent...")
    
    env = InventoryEnv()
    
    # Load the PPO model
    try:
        model = PPO.load("models/ppo_inventory")
        print("Loaded PPO model")
    except:
        print("No trained model found. Training a quick model...")
        model = train_ppo_agent(env, total_timesteps=1000)
    
    # Run short test
    obs, _ = env.reset()
    print(f"Initial state: {obs}")
    
    for i in range(10):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, truncated, info = env.step(action)
        print(f"Step {i+1}: Action={action}, State={obs}, Reward={reward:.2f}")
    
    print("Agent test completed!")


if __name__ == "__main__":
    results = train_and_evaluate_agents()
    print("\n" + "="*50)
    print("Training and evaluation completed!")
    print("Models saved in 'models/' directory")
    print("Best model saved as 'inventory_agent.zip'")
