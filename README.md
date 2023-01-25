# fourier_series_visualize
This small project shows how partial sums of fourier series approximate given function. <br>
Also this project provides Function class, which presents intuitive and easy way to handle functions. <br>
```
sin = Function( math.sin, label = 'sin' )
cos = Function( math.cos, label = 'cos' )
x = Function( lambda t: t, label = 'x' )

f = sin(cos(x*x)) + sin(x) + 3 # f(x) = sin(cos(x^2)) + sin(x) + 3
print(f(2))                    # sin(cos(2*2)) + sin(2) + 3 ≈ sin(-0.654) + 0.909 + 3 ≈ 3.3012144171849163
# also it has __str__ method, it uses "label" field as function name
print( f )                     # sin(cos(x*x)) + sin(x) + 3
```
## Some samples
### f(x) = x
For N = 4 <br>
 ![x_4](https://user-images.githubusercontent.com/99137907/210859403-2b461626-e8a2-403b-8400-04fcdc32bdd3.png)
 <br>
For N = 20 <br>
 ![x_20](https://user-images.githubusercontent.com/99137907/210859572-c2b62b65-9209-4dac-b4b6-27f2ba5da7b2.png)
 <br>
<br>
### f(x) = x + sin(x^2)
For N = 4 <br>
 ![x_sinxx_4](https://user-images.githubusercontent.com/99137907/210859805-79b4a75c-af61-4f3e-9303-49c5122d1bfb.png)
 <br>
For N = 20 <br>
 ![x_sinxx_20](https://user-images.githubusercontent.com/99137907/210859021-549289d5-ff6e-4331-8181-864dd1efa63f.png)
 <br>
### f(x) = |x| ^ sin(x)
 ![image](https://user-images.githubusercontent.com/99137907/214660857-605cd238-7013-4fee-8110-db4368011dd8.png)
 <br>
 
## Interaction
On start, there is a list of functions to work with. You can extend this list by adding functions to `funcs` list in `cli/function_catalogue.py` file. <br>
By providing N - top bound of partial fourier sum, you'll get graphs of initial function and partial fourier sum on top of it. By closing graph you'll be able to enter N again. <br> 
![image](https://user-images.githubusercontent.com/99137907/210856382-d64759b4-1fcb-4fd3-8e24-ac27cd09db43.png) <br>
