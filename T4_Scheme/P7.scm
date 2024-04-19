#lang scheme

(define fpi
  (lambda (f u i)
    (let ( (funcion f) (umbral u) (inicial i))
      (calcular funcion umbral inicial)
      )
    )
  )

;; calcular (funcion, umbral, inicial, iteraciones)
;; es una funcion auxiliar que va calculando los f(x) y cuenta las iteraciones
;; retorna la cantidad de iteraciones hasta resolver el problema
(define calcular
  (lambda (f u i)
    (let calcular ( (funcion f) (umbral u) (inicial i) (iteraciones 0))
      (if (<= (abs(- (funcion inicial) inicial)) umbral)
          iteraciones
          (calcular funcion umbral (funcion inicial) (+ iteraciones 1))
          )
      )
    )
  )