SimpleRSA
=========
This program is a Cython version of the previously created SimpleRSA. As seen in the code, 
data types for variables have been declared and cython spcific class model has been used.

The purpose of this implementation is to acquire faster computation for implmenting
public-key/private-key for large numbers.

I used sage-notebook to time my python vs cython results, the links for which
can be found here ---> [Python run worksheet](http://www.sagenb.org/home/pub/5039), [Cython run worksheet](http://www.sagenb.org/home/pub/5038). 

Since the links may go bogus or sometimes public viewing of the worksheet is disabled
I have made a direct note of the statistics below.


###Python run
`````Sage

timeit("test(3,3243524634634234642,3)")

       	
---------TEST1---------
Limit = 9730573903902703926
-------
('public key', (331952589637151160763879304196608792928L,
266215717769350224296471097214838017487L))
('private key', (331952589637151160763879304196608792928L,
311233166920449679259460214372193210155L))
-------
Time(seconds): 0.0784330368042
---------TEST1---------


---------TEST2---------
Limit = 29191721711708111778
-------
('public key', (2079914322757846194559738496003140389747L,
1939140487188183879722825978824089838081L))
('private key', (2079914322757846194559738496003140389747L,
821164300145348097870708784846592592721L))
-------
Time(seconds): 0.0769691467285
---------TEST2---------


---------TEST3---------
Limit = 87575165135124335334
-------
('public key', (17314312269908527919940081823819384653760L,
9218536254616444276568380784360045130673L))
('private key', (17314312269908527919940081823819384653760L,
4379715223728159317987009176334796727468L))
-------
Time(seconds): 0.0785570144653
---------TEST3---------


CPU time: 0.23 s,  Wall time: 0.24 s
5 loops, best of 3: 210 ms per loop


`````



###Cython run

`````Sage 
	
%timeit
test(3,3243524634634234642,3)
       	
---------TEST1---------
Limit = 9730573903903926
-------
('public key', (14141557691648328706L, 4630939218726267357L))
('private key', (14141557691648328706L, 1926730060681417057L))
-------
Time(seconds): 0
---------TEST1---------


---------TEST2---------
Limit = 29191721711711778
-------
('public key', (9295157568235870136L, 6334617999918854103L))
('private key', (9295157568235870136L, 5648631316216411919L))
-------
Time(seconds): 0
---------TEST2---------


---------TEST3---------
Limit = 87575165135135334
-------
('public key', (12660957379041249769L, 12299823140815331973L))
('private key', (12660957379041249769L, 3605631755539055437L))
-------
Time(seconds): 0
---------TEST3---------



CPU time: 0.04 s,  Wall time: 0.04 s
5 loops, best of 3: 45.8 ms per loop


`````


As visible, the total taken to compute 3 different sizes of public-key/private-key is 
0.23 s CPU time, 0.24 s Wall time in Python and 0.04 s CPU time, 0.04 Wall time in Cython,

Hence, Cython gives 0.24/0.4 = 6x faster computation time. 

Since it takes neglible time to compute the public-key/private-key in the Cython run, 
the "Time(seconds)" field dsplays 0 for it. 

