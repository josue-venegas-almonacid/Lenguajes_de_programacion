#lang scheme

(define camino '())

(define (voy nodo grafo)
  (begin (set! camino '())
         (let voy ((i nodo) (grafo grafo) (lista '()))
           (if (null? (ady i grafo))
               (cam-mas-largo (append lista (list i)))
               (if (= (length (ady i grafo)) 1) (voy (car (ady i grafo)) grafo (append lista (list i)))
                   (do ((n 0 (+ n 1))) ((= n (length (ady i grafo))))
                     (voy (elem-lista (ady i grafo) n) grafo (append lista (list i))))))
           )
         camino)
  )

;;(cam-mas-largo) (lista)
;;funcion auxiliar que reemplaza una lista por una lista mayor
;;retorna la nueva lista con mayor camino
(define (cam-mas-largo lista)
    (if (> (length lista) (length camino))
        (set! camino lista)
        (set! camino camino)
        )
  )

;;(elem-lista) (lista n)
;;busca elementos de una lista
;;retorna un elemento de la lista de adyacencia del nodo
(define (elem-lista lista n)
  (let mini-ene ((lista lista) (n n) (contador 0))
    (if (= contador n)
        (car lista)
        (mini-ene (cdr lista) n (+ contador 1))
        )
    )
  )

;;(ady) (n grafo)
;;función auxiliar que retorna lista de adyacencia de un nodo
;;retorna la lista de adyacencia de un nodo
(define (ady n grafo)
  (let recorrer((n n) (grafo grafo))
    (if (null? grafo)
        "elemento no encontrado"
        (if (= n (caar grafo))
            (cadar grafo)
            (recorrer n (cdr grafo))
            )
        )
    )
  )