#lang scheme

(define armar
  (lambda (x y)
    (let armar ( (resultado x) (lista y) )
      (obtener-sumas resultado lista (length lista))
      )
    )
  )

;; obtener-sumas (resultado, lista, len, sumas, cont)
;; funcion auxiliar que suma los elementos de la lista para comprobar si cumple lo solicitado
;; retorna la lista con los numeros que cumplen la condición
(define obtener-sumas
  (lambda (x y z)
    (let obtener-sumas( (resultado x) (lista y) (len z) (sumas '()) (cont 1) )
      (if (eqv? cont len)
          (if (null? sumas)
              #f
              sumas
              )
          (if (equal? (+ (first lista) (second lista)) resultado)
              (obtener-sumas resultado (list-tail lista 2) len (append (list (first lista) (second lista)) sumas) (+ cont 1))
              0)
              
          )
      )
    )
  )
