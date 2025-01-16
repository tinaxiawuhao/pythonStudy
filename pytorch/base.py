from __future__ import print_function
import torch

# 创建一个没有初始化的 5 * 3 矩阵：

x = torch.empty(5, 3)
print(x)

# 创建一个随机初始化矩阵：
x = torch.rand(5, 3)
print(x)

# 构造一个填满 0 且数据类型为 long 的矩阵：

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

#直接从数据构造张量：

x = torch.tensor([5.5, 3])
print(x)

x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)

x = torch.randn_like(x, dtype=torch.float)    # 重载 dtype!
print(x)   

print(x.size())

x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(x + y)
print(torch.add(x, y))

result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

# adds x to y
y.add_(x)
print(y)

print(x)
print(x[:, 1])

x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x)
print(y)
print(z)
print(x.size(), y.size(), z.size())

x = torch.randn(1)
print(x)
print(x.item())

# 当GPU可用时,我们可以运行以下代码
# 我们将使用`torch.device`来将tensor移入和移出GPU
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # 直接在GPU上创建tensor
    x = x.to(device)                       # 或者使用`.to("cuda")`方法
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # `.to`也能在移动时改变dtype