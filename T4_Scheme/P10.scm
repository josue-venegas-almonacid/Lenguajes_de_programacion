#lang scheme

(define serie
  (lambda (x y)
    (let serie ( (funcion x) (entero y) (suma 0) (cont 1))
      (if (> cont entero)
          suma
          (serie funcion entero (+ suma (funcion cont)) (+ cont 1))
          )
      )
    )
  )
          