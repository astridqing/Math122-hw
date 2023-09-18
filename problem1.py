# a)
import numpy as np
import matplotlib.pyplot as plt
coefficients = [1, -16, 96, -256, 256]
x = np.arange (4.0000,4.00101,0.00001)
# Evaluate p(x) using the coefficients
p = np.polyval(coefficients, x)
# Plotting p(x) over x
plt.plot(x, p,'r')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Plot of p(x) over x')
plt.grid(True)


# b)
p_evaluate = (x-4)**4
plt.plot(x,p_evaluate,'b')
plt.show()

