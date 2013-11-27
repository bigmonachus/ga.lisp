; Cosine
;;
;; Find an aproximation to the cosine function using a set of functions.
;; SBCL:
;; (ql:quickload "swank")
;; (swank:start-server)


(defun run (fitness-func population)
  (loop for m in population collect
        (progn
          (fitness-func m))))

(defun cosine-fitness (f x)
  (abs(- (cos x) (f x))))
