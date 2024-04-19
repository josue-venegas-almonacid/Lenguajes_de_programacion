#lang scheme

(define cima
  (lambda (x)
    (let cima ( (lista x) )
      (if (equal? (length lista) 2)
       (apply + lista)
       (cima (obtener-piso lista (length lista)))
       )
      )
    )
  )

;; obtener-piso (lista, len, piso, cont)
;; es una funcion auxiliar que va calculando la suma del término i con el término i+1
;; de esta forma la lista original cambia recursivamente a estas nuevas lista
;; retorna el piso formado

(define obtener-piso
  (lambda (x y)
    (let obtener-piso( (lista x) (len y) (piso '()) (cont 1) )
      (if (eqv? cont len)
          piso
          (obtener-piso (list-tail lista 1) len (append piso (list(+ (first lista) (second lista)))) (+ cont 1) )
          )
      )
    )
  )
      
      
          