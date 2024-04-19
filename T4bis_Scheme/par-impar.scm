#lang Scheme
(define par-impar
  (lambda (ls)
    (let distribuir((l ls)(pares '())(impares '()))
      (if (null? l)
          (list pares impares)
          (if (= (modulo (car l) 2) 0)
              (distribuir (cdr l) (append pares (list(car l))) impares)
              (distribuir (cdr l) pares (append impares (list(car l))))
          )
      )
    )
   )
)

; Casos de prueba no exhaustivos
; Deberían todos retornar #t
(equal? (par-impar '(1 2 3 4 5 6 7 8 9)) '((2 4 6 8) (1 3 5 7 9)))
(equal? (par-impar (list 1 2 3 4 5 6 7 8 9)) (list (list 2 4 6 8) (list 1 3 5 7 9)))
(equal? (par-impar '()) '(() ()))
(equal? (par-impar '(1 3 5)) '(() (1 3 5)))
(equal? (par-impar '(2 4 6)) '((2 4 6) ()))