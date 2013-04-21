SimpleRSA
=========
This program is a Cython version of the previously created SimpleRSA. As seen in the code, 
data types for variables have been declared and cython spcific class model has been used.

The purpose of this implementation is to acquire faster computation for implmenting
public and private key for large numbers.

I used sage-notebook to time my python vs cython results

![Here is the time statistics for the Python run](http://www.sagenb.org/home/pub/5039) 

![Here is the time statistics for the Cython run](http://www.sagenb.org/home/pub/5038)
`````Python
>>> import SimpleRSA
>>> enc =SimpleRSA.SimpleRSA(23)
>>> enc.compute()
public key (1472, 29)
private key (1472, 914)

>>> import SimpleRSA
>>> enc =SimpleRSA.SimpleRSA(1000000)
>>> enc.compute()
public key (2104893971370, 308193614463)
private key (2104893971370, 699515598545)


>>> enc =SimpleRSA.SimpleRSA() 
>>> enc.compute()
public key (10468427810168432640, 9554926832143394029)
private key (10468427810168432640, 15581655766859127013)

`````

Notice that, in the third example, we do not supply an upper bound for indiividual integers that make the public 
and private key. In this case, the program simply uses `````Python sys.maxsize````` which is equal to 2147483647


