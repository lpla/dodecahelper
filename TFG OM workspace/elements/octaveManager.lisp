(defun gestionOctavas (listaNotas threshold maxoctava minoctava)
  
  (setq trigger (+ minoctava (random (+ 1 (- (+ 1 maxoctava) (+ 1 minoctava))))))

  (loop for x in listaNotas do
      (if (= 0 (random threshold))
          (if(= 0 (random 2)) ; 0 significa que cambiamos de octava hacia arriba, 1 que bajamos
              (if (and (= 0 trigger) (= maxoctava 1))
                  (setq trigger 1)
                (if (and (= -1 trigger) (>= maxoctava 0))
                    (setq trigger 0)
                  )
                )

            (if (and (= 0 trigger) (= minoctava -1))
                (setq trigger -1)
              (if (and (= 1 trigger) (<= minoctava 0))
                  (setq trigger 0)
                )
              )
            )
        )
      collect (+ x (* 1200 trigger))
  )
)