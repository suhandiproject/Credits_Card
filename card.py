ó
Ý¡ß]c           @   sÂ   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d Z d   Z	 d   Z
 d   Z d   Z d   Z d   Z d	   Z d
   Z d   Z e
   d S(   iÿÿÿÿNs  [1;91m

                  `.-://////:-.`
              .:+o+:-..````..-:+o+:.
           `:o+-`                `:+o:`
         `/o:`                      `:o/`
        -s/`  .-..`            `..--` `/s-
       /o.   `:.`.-:----------:-.``:-   .o/
      /o`    .:`    `              --    `o/
     -s.     .:`                   --     .s-
     o/     .:`                     --     +o
    .s-     :.                      `:`    -s`
    .s.     :.                      `:`    .s.
    .s-     --                      .:     -s.
     o/     `-.                    `-.     /o
     -s.     `--`                `.-`     .s-
      /o` ----``..--..`    `...--.`      `o/
       /o. `----`  `-.      `-.         .o/
        -o:  -.......        ..       `:o-
         `:o:``....--        ..     `:o:`
           `:+/-`  `-        ..  `-/+:`
              `-/+///..````..://+/-`
                  `.-::////::-.` [1;97m
	  ââââââââââââââââââââââââââââââ
	   [1;91mCREDITS [1;93mCARDS [1;92m| [1;97mBY : [1;96mSUHANDI[1;97m
	  ââââââââââââââââââââââââââââââc          C   s]   d }  xP t  d  D]B } t j d  t j j d |  | t |    t j j   q Wd  S(   Nt   .s   ..s   ...id   g¹?s   [1;92mStarting [1;91m(   R    s   ..s   ...(   t   ranget   timet   sleept   syst   stdoutt   writet   lent   flush(   t   anit   i(    (    s   card.pyt   tik"   s
    "c           C   s,   t  j d  t GHHt   t   t   d  S(   Nt   clear(   t   ost   systemt   logot   cek1t   cek2t   run(    (    (    s   card.pyt   main)   s    c          C   sT  d d d d d d d d d	 d
 d g }  t  d  } yç | d k r t j |   } t d d  } | j |  | j   t j j   n | d k rØ t j |   } t d d  } | j |  | j   t j j   nA | d k rt d d  } | j d  | j   n d GHt	   Wn3 t
 t f k
 rOd GHt j d  t j   n Xd  S(   Ns   Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36sA   Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)s"   Roku4640X/DVP-7.70 (297.70E04154A)sl   Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36sN   Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1sH   [1;91m[[1;92moptions[1;91m][1;97m Do you have use vpn? (y/n) [1;93mt   yt   vipt   wt   Yt   ns   your not use vpn defaultsO   [1;91m[[1;93mwarning[1;91m][1;93m You did not enter the selection correctlys.   [1;91m[[1;97m*[1;91m] [1;90mStoped![1;97ms
   rm -rf vip(   t	   raw_inputt   randomt   choicet   openR   t   closeR   R   R   R   t   KeyboardInterruptt   EOFErrorR   R   t   exit(   t   vpnt   ckt   ht   c(    (    s   card.pyR   1   sF    	

c          C   s}   t  d  }  y7 t d d  } | j |   | j   t j j   Wn3 t t f k
 rx d GHt	 j
 d  t j   n Xd  S(   Ns<   [1;91m[[1;92moptions[1;91m][1;97m Select delay : [1;93mt   jedaR   s.   [1;91m[[1;97m*[1;91m] [1;90mStoped![1;97ms   rm -rf vip && rm -rf jeda(   R   R   R   R   R   R   R   R   R   R   R   R    (   R"   t   t(    (    s   card.pyR   \   s    
c          C   sî   t  j d  t GHHy¡ t d  }  |  d k s: |  d k rD t   no |  d k s\ |  d k rf t   nM |  d k s~ |  d k r d	 GHt j d
  t   n d	 GHt j d
  t   Wn3 t	 t
 f k
 ré d GHt  j d  t j   n Xd  S(   NR   s   [1;91m[[1;92m?[1;91m][1;97m what do you want to take? Visa card or master card?
    (v) for visa, (m) for mastercard  [1;93mt   vt   Vt   mt   Mt   at   AsP   [1;91m[[1;93mwarning[1;91m][1;93m You did not enter the selection correctly!i   s.   [1;91m[[1;97m*[1;91m][1;90m Stoped![1;97ms   rm -rf vip && rm -rf jeda(   R   R   R   R   t   visat   masterR   R   R   R   R   R   R    (   t   cd(    (    s   card.pyR   i   s(    


c          C   sä   t  d d  j   }  t  d d  j   } t j d  t GHHt j d  d |  GHt j d  d | GHt j d	  xg t d
  D]Y } y d d GHt   d d GHWq t	 t
 f k
 rÛ d GHt j d  t j   q Xq Wd  S(   NR   t   rR%   R   i   s0   [1;91m[[1;92minfo[1;91m][1;97m vpn : [1;93mi   s2   [1;91m[[1;92minfo[1;91m][1;97m delay : [1;93mg      @iô  sa   [1;97mââââââââââââââââââââââââââââââs.   [1;91m[[1;97m*[1;91m][1;90m Stoped![1;97ms   rm -rf vip && rm -rf jeda(   R   t   readR   R   R   R   R   R   t   cardvR   R   R   R    (   R'   t   dR
   (    (    s   card.pyR-      s&    			c    (      C   s  t  d d  j   }  y d 
} }  Wn3 t t f k
 rY d GHt j d  t j   n Xd d d d	 d
 g } d d d d d g } d d d d d d d d d d g
 } d d d d d d d d  d! d" d# d$ d% d& d' d( d) d* d+ d, d- g } d. d/ d0 d1 d2 g } y¸t j	 |  } t j	 |  } t j	 |  }	 t j	 |  }
 t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } d | | |	 d3 |
 | | | d3 | | | | d3 | | | | } yOt j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } d4 | | | | | d5 | | | | }  d4 | | | | | | | | | }! d4 | | | | | | }" t j	 |  }# t j	 |  }$ d4 |! | | | |$ }% d6 | | | | }& Wn3 t t f k
 r¸d GHt j d  t j   n XWn3 t t f k
 rïd GHt j d  t j   n Xt
 j d7  y t j d8  }' WnL t t j j t j j f k
 r^d9 GHd: d; GHt j d<  Ht j   n Xd= GHd> |  GHd? | GHd@ |" GHdA |% GHdB |# GHdC |& GHd  S(D   NR%   R0   i    s.   [1;91m[[1;97m*[1;91m][1;90m Stoped![1;97ms   rm -rf vip && rm -rf jedas   @teleworm.coms   @armyspy.coms
   @rhyta.coms   @outlook.coms   @jourapide.coms   United statess   United Kingdomst   Uruguayt   Solveniat   Tunisiat   1t   2t   3t   4t   5t   6t   7t   8t   9t   0t   bt   st   jR$   t   kR&   R   t   pR)   R   t   xR3   t   lt   ft   gR#   R   t   qR'   t   zR+   R
   t   ut   et   os    - t    t    t   $i   s   http://api.myip.coms=   [1;91m[[1;93mconnection[1;91m] [1;91mConnection refursed!i   sa   [1;97mââââââââââââââââââââââââââââââs   rm -rf jeda && rm -rf vips'   [1;92m INFORMATION[1;96m				    	VISAs   [1;97m Name      : [1;93ms   [1;97m CC number : [1;93ms   [1;97m Pin       : [1;93ms   [1;97m Email     : [1;93ms   [1;97m Region    : [1;93ms   [1;97m Balance   : [1;93m(   R   R1   R   R   R   R   R   R    R   R   R   R   t   requestst   gett   KeyErrort
   exceptionst   ConnectionErrort   ReadTimeout((   R$   R3   t   domt   regt   numt   namt   alfatt   n1t   n2t   n3t   n4t   n5t   n6t   n7t   n8t   n9t   n10t   n11t   n12t   n13t   n14t   n15t   not   nc1t   nc2t   nc3t   nc4t   nc5t   nc6t   nc7t   nc8t   nc9t   namet   nmt   paswt   lokt   mailt   emt   bcR+   (    (    s   card.pyR2      s    $EN.*"						c          C   sä   t  d d  j   }  t  d d  j   } t j d  t GHHt j d  d |  GHt j d  d | GHt j d	  xg t d
  D]Y } y d d GHt   d d GHWq t	 t
 f k
 rÛ d GHt j d  t j   q Xq Wd  S(   NR   R0   R%   R   i   s0   [1;91m[[1;92minfo[1;91m][1;97m vpn : [1;93mi   s2   [1;91m[[1;92minfo[1;91m][1;97m delay : [1;93mg      @iô  sa   [1;97mââââââââââââââââââââââââââââââs.   [1;91m[[1;97m*[1;91m][1;90m Stoped![1;97ms   rm -rf vip && rm -rf jeda(   R   R1   R   R   R   R   R   R   t   cardv2R   R   R   R    (   R'   R3   R
   (    (    s   card.pyR.   æ   s&    			c    '      C   s  t  d d  j   }  y d 
} }  Wn3 t t f k
 rY d GHt j d  t j   n Xd d d d	 d
 g } d d d d d g } d d d d d d d d d d g
 } d d d d d d d d  d! d" d# d$ d% d& d' d( d) d* d+ d, d- g } d. d/ d0 d1 d2 g } y¢t j	 |  } t j	 |  } t j	 |  }	 t j	 |  }
 t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } d | | |	 d3 |
 | | | d3 | | | | d3 | | | | } y9t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } t j	 |  } d4 | | | | | d5 | | | | }  d4 | | | | | | | | | }! d4 | | | | | | }" t j	 |  }# t j	 |  }$ d4 |! | | | |$ }% Wn3 t t f k
 r¢d GHt j d  t j   n XWn3 t t f k
 rÙd GHt j d  t j   n Xt
 j d6  y t j d7  }& WnL t t j j t j j f k
 rHd8 GHd9 d: GHt j d;  Ht j   n Xd< GHd= |  GHd> | GHd? |" GHd@ |% GHdA |# GHd  S(B   NR%   R0   i    s.   [1;91m[[1;97m*[1;91m][1;90m Stoped![1;97ms   rm -rf vip && rm -rf jedas   @teleworm.coms   @armyspy.coms
   @rhyta.coms   @outlook.coms   @jourapide.coms   United statess   United KingdomsR4   R5   R6   R7   R8   R9   R:   R;   R<   R=   R>   R?   R@   RA   RB   RC   R$   RD   R&   R   RE   R)   R   RF   R3   RG   RH   RI   R#   R   RJ   R'   RK   R+   R
   RL   RM   RN   s    - RO   RP   i   s   http://api.myip.coms=   [1;91m[[1;93mconnection[1;91m] [1;91mConnection refursed!i   sa   [1;97mââââââââââââââââââââââââââââââs   rm -rf jeda && rm -rf vips/   [1;92m INFORMATION[1;96m			  	    	MASTERcards   [1;97m Name      : [1;93ms   [1;97m CC number : [1;93ms   [1;97m Pin       : [1;93ms   [1;97m Email     : [1;93ms   [1;97m Region    : [1;93m(   R   R1   R   R   R   R   R   R    R   R   R   R   RR   RS   RT   RU   RV   RW   ('   R$   R3   RX   RY   RZ   R[   R\   R]   R^   R_   R`   Ra   Rb   Rc   Rd   Re   Rf   Rg   Rh   Ri   Rj   Rk   Rl   Rm   Rn   Ro   Rp   Rq   Rr   Rs   Rt   Ru   Rv   Rw   Rx   Ry   Rz   R{   R+   (    (    s   card.pyR}   ü   s    $EN.*"					(   R   RR   R   R   t   ret   jsonR   t   socketR   R   R   R   R   R   R-   R2   R.   R}   (    (    (    s   card.pyt   <module>   s   `			+				N		N


	DONT CHANGE THIS CODE MOTHERFUCKER!