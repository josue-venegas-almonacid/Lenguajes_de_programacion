#lang scheme
(define (abundante x)
  (cond 
    ((= x 0) #f)
    ((= x 1) #f)
    ((> (apply +(divisores x)) (doble x)) #t)
    (else #f)
    )
  )

(define (doble x) (* x 2))

(define (divisores x)
  (cond
    ((= x 1) '(1))
    (else (cons 1 (divisores-aux x 2)))
    )
  )

(define (divisores-aux x y)
  (cond
    ((= x y) (list x))
    ((zero? (remainder x y)) (cons y (divisores-aux x (+ y 1))))
    (else (divisores-aux x (+ y 1))))
)

; Casos de prueba no exhaustivos
; Deberían todos retornar #t
(equal? (abundante 8)   #f)
(equal? (abundante 12)  #t)
(equal? (abundante 13)  #f)
(equal? (abundante 24)  #t)
(equal? (abundante 945) #t)