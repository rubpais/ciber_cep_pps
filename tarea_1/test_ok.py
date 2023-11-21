import unittest
import fibo

class TestFibo(unittest.TestCase):
    
    def test_fibo(self):
          
        # Serie Fibonacci:       0, 1, 1, 2, 3, 5, 8
        # Posiciones números:    0, 1, 2, 3, 4, 5, 6    
        
        # Array de dos dimensiones con el número y su posición
        lista = [(0,0),(1,1),(1,2),(2,3),(3,4),(5,5),(8,6)]
        
        # Recorrer el array 'lista', siendo la variable 'a' el valor y 'b' su posición
        for a, b in lista:
            
            with self.subTest(a = a, b = b):
                
                # Ejecutar función fibo con el parámetro de la posición
                c = fibo.fibonacci(b) 
                
                # Ejecutar el test
                self.assertEqual(a,c)

if __name__ == '__main__' : unittest.main()