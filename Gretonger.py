ó
Øü.]c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e j   Z e  j	 e  j
 d k r{ d n d  d   Z d   Z d   Z d d	 d
  Z d d d  Z d e f d     YZ d e j f d     YZ d   Z e d k r	e   n  d S(   iÿÿÿÿNt   ntt   clst   clearc         C   s    t  j j t  j j t   |  S(   N(   t   ost   patht   dirnamet   abspatht   __file__(   t	   file_name(    (    s   /sdcard/Gretonger.pyt	   real_path   s    c         C   sn   xN t  t |    D]: } |  | j   |  | <|  | j d  r d |  | <q q Wg  |  D] } | rX | ^ qX S(   Nt   #t    (   t   ranget   lent   stript
   startswith(   t   arrayt   it   x(    (    s   /sdcard/Gretonger.pyt   filter_array   s
    c         C   sd   i d d 6d d 6d d 6d d 6d	 d
 6d d 6} x- | D]% } |  j  d j |  | |  }  q7 W|  S(   Ns   [31;1mt   R1s   [31;2mt   R2s   [32;1mt   G1s   [33;1mt   Y1s   [35;1mt   P1s   [0mt   CCs   [{}](   t   replacet   format(   t   valuet   patternst   code(    (    s   /sdcard/Gretonger.pyt   colors   s    #s   SETING DI PSIPHONs   [CC]c      
   C   sR   t  d j d t j j   j d  d |  d | d |   }  t 
 |  GHWd  QXd  S(   Ns?   {color}[G1][{time}] [P1] {color}{status} [R1]{color}{value}[CC]t   timeR   R   t   colort   status(   R   R   t   datetimet   nowt   strftimet   lock(   R   R"   R!   (    (    s   /sdcard/Gretonger.pyt   log"   s     t   INFOs   [Y1]c         C   sI   t  d j | | |    }  t " t j j |   t j j   Wd  QXd  S(   Ns   {}{} ({})        [CC](   R   R   R&   t   syst   stdoutt   writet   flush(   R   R"   R!   (    (    s   /sdcard/Gretonger.pyt   log_replace+   s    t   injectc           B   s&   e  Z d    Z d d  Z d   Z RS(   c         C   s5   t  t |   j   t |  |  _ t |  |  _ d  S(   N(   t   superR.   t   __init__t   strt   inject_hostt   intt   inject_port(   t   selfR2   R4   (    (    s   /sdcard/Gretonger.pyR0   2   s    s   [R1]c         C   s   t  | d | d  S(   NR!   (   R'   (   R5   R   R!   (    (    s   /sdcard/Gretonger.pyR'   8   s    c         C   s,  yí t  j  t  j t  j  } | j |  j |  j f  | j d  t t d   j	   } t
 |  } t |  d k r |  j d d d d  S|  j d j |  j |  j   x< t rë | j   \ } } | j d  t | |  j   q° WWn8 t k
 r'} |  j d j |  j |  j  d d	 n Xd  S(
   Ni   s	   /Nur.ehili    s1   Frontend Domains not found. Please check Nur.ehilR!   s   [Y1]s
   {} PORT {}iÿÿ  s   [R1](   t   sockett   AF_INETt   SOCK_STREAMt   bindR2   R4   t   listent   openR	   t	   readlinesR   R   R'   R   t   Truet   acceptt   recvt   domain_frontingt   startt	   Exception(   R5   t   socket_servert   frontend_domainst   socket_clientt   _t	   exception(    (    s   /sdcard/Gretonger.pyRA   ;   s     	(   t   __name__t
   __module__R0   R'   RA   (    (    (    s   /sdcard/Gretonger.pyR.   1   s   	R@   c           B   s2   e  Z d    Z d d d  Z d   Z d   Z RS(   c         C   sV   t  t |   j   | |  _ t j t j t j  |  _ | |  _ d |  _	 t
 |  _ d  S(   Niÿÿ  (   R/   R@   R0   RD   R6   R7   R8   t   socket_tunnelRE   t   buffer_sizeR=   t   daemon(   R5   RE   RD   (    (    s   /sdcard/Gretonger.pyR0   N   s    			t   GRATISANs   [G1]c         C   s   t  | d | d | d  S(   NR"   R!   (   R'   (   R5   R   R"   R!   (    (    s   /sdcard/Gretonger.pyR'   W   s    c         C   sè   | | g } d } xÏ t  rã | d 7} t j | g  | d  \ } } } | rP Pn  | rÐ xw | D]l }	 y[ |	 j |  }
 |
 s Pn8 |	 | k r | j |
  n |	 | k r· | j |
  n  d } Wq] Pq] Xq] Wn  | d k r Pq q Wd  S(   Ni    i   i   i   (   R=   t   selectR?   t   sendall(   R5   RJ   RE   RK   t   socketst   timeoutt	   socket_ioRF   t   errorst   sockt   data(    (    s   /sdcard/Gretonger.pyt   handlerZ   s,    	
!  
  c         C   sv  yt  j |  j  j d  |  _ |  j d |  _ t |  j  d k r` |  j d r` |  j d n d |  _ |  j d j	 |  j |  j   |  j
 j t |  j  t |  j  f  |  j j d  |  j |  j
 |  j |  j  |  j j   |  j
 j   |  j d j	 |  j |  j  d	 d
 WnS t k
 rB|  j d d	 d n0 t k
 rq|  j d j	 |  j  d	 d n Xd  S(   Nt   :i    i   i   t   80t   MENGKONEKANs   HTTP/1.1 200 OK

s   CONNECTED[R1]R!   s   [CC]s   Connection errors   [R1]s   {} not responding(   t   randomt   choiceRD   t   splitt   proxy_host_portt
   proxy_hostR   t
   proxy_portR'   R   RJ   t   connectR1   R3   RE   RO   RV   RK   t   closet   OSErrort   TimeoutError(   R5   (    (    s   /sdcard/Gretonger.pyt   runo   s    8()(   RH   RI   R0   R'   RV   Rd   (    (    (    s   /sdcard/Gretonger.pyR@   M   s   			c           C   sF   t  d j d d d d d d d d d g	   GHt d	 d
  j   d  S(   Ns   
R   s   [R1][NUR[P1] HIDAYAT]s!   [CC][G1]===JGN BUAT NONTON JAV===s   [CC][P1]Free Internet Indonesias.   [CC][CC]>>>JIKA ADA YG GRATIS NGAPAIN BAYAR<<<s*   [CC][Y1]===JADILAH ORANG YG RENDAH HATI===sS   [R2]JGN LUPA LNGSUNG BUKA PSIPHON DAN SET PSIPHONYA,EXLUDE APPS DAN STEALTH SETTINGs	   127.0.0.1s   3128 (   R   t   joinR.   RA   (    (    (    s   /sdcard/Gretonger.pyt   main   s    	t   __main__(   R   R)   RZ   R6   RN   R#   t	   threadingt   RLockR&   t   systemt   nameR	   R   R   R'   R-   t   objectR.   t   ThreadR@   Rf   RH   (    (    (    s   /sdcard/Gretonger.pyt   <module>   s$    "				3	