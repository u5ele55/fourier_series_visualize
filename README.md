# fourier_series_visualize
This small project shows how partial sums of fourier series approximate given function.<br>
Also this project provides Function class, which presents intuitive and easy way to handle functions. <br>
```
sin = Function( math.sin )
cos = Function( math.cos )
x = Function( lambda t: t )

f = sin(cos(x*x)) + sin(x) + 3 # f(x) = sin(cos(x^2)) + sin(x) + 3
print(f(2))            # sin(cos(2*2)) + sin(2) + 3 ≈ sin(-0.654) + 0.909 + 3 ≈ 3.3012144171849163
```
## Some samples
### f(x) = x
For N = 3 <br>
![image](https://user-images.githubusercontent.com/99137907/209999525-f5494757-5049-4339-bac5-5954e5197843.png) <br>
For N = 20<br>
![image](https://user-images.githubusercontent.com/99137907/209999551-bac9642c-3d9b-45e5-aa0a-2e021bd01cca.png) <br>
### f(x) = { x^2 if x < 0 else 1 }
For N = 4 <br>
![image](https://user-images.githubusercontent.com/99137907/210000414-1c36567b-6d59-4e4e-99d2-bba52d4d5975.png) <br>
For N = 20 <br>
![image](https://user-images.githubusercontent.com/99137907/210000557-c88ee98b-3291-48a7-8d9a-ec9082e7c3c7.png) <br>

