import numpy as np

# 定义多个路径
paths = [
    "./results/TD3_BC_halfcheetah-expert-v0_0.npy",
    "./results/TD3_BC_halfcheetah-expert-v0_1.npy",
    # "./results/TD3_BC_hopper-medium-v0_0.npy",
    # "./results/TD3_BC_walker2d-medium-v0_0.npy",
    # "./results/TD3_BC_halfcheetah-expert-v0_0.npy",
    # "./results/TD3_BC_hopper-expert-v0_0.npy",
    # "./results/TD3_BC_walker2d-expert-v0_0.npy"
    # 可以添加更多路径
]

means = []
# 遍历处理每个路径
for path in paths:
    try:
        # 加载数据
        scores = np.load(path)
        
        # 获取最后五个值的均值
        mean = np.mean(scores[-10:])
        means.append(mean)
        
        print(f"路径: {path} 最后5个值的均值: {mean:.4f}")
        
    except FileNotFoundError:
        print(f"错误: 文件 {path} 不存在")
    except Exception as e:
        print(f"错误: 处理文件 {path} 时出错: {e}")

# 计算所有均值的总均值和方差
if means:
    overall_mean = np.mean(means)
    variance = np.var(means)
    print(f"{overall_mean:.1f} $\pm$ {variance:.1f}")
else:
    print("没有有效的数据文件")