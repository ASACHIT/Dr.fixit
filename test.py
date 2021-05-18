import distro
x = distro.linux_distribution(full_distribution_name=False)[0]
print(x)