#lang scheme

(define maymecola
  (lambda (x)
    (let maymecola ( (ls x) (cabeza (caar x)) (cola (cdr (car x))) (minimo +inf.0) (maximo -inf.0) (min 0) (max 0) (cont 1))
      (if (equal? cont (length ls))
          (list max min) 
          (if (> (apply + cola) maximo)
              (maymecola ls (cadr ls) (caadr ls) minimo (apply + cola) min cabeza (+ cont 1))
              (if (< (apply + cola) minimo)
                  (maymecola ls (cadr ls) (caadr ls) (apply + cola) maximo cabeza max (+ cont 1))
                  (maymecola ls (cadr ls) (caadr ls) minimo maximo min max (+ cont 1))
                  )
              )
          )
      )
    )
  )
