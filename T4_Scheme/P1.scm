#lang scheme

(define gemelos
  (lambda (x y)
    (let gemelos ( (arbol1 x) (arbol2 y) )
      (if (and (null? arbol1) (null? arbol2))
          #t
          0)
      )
    )
  )