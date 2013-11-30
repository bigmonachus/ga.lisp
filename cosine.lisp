; Cosine
;;
;; Find an aproximation to the cosine function using a set of functions.
;; SBCL:
;; (ql:quickload "swank")
;; (swank:start-server)
;(proclaim '(optimize (speed 3) (space 0) (safety 0)))

(defun run (fitness-func population)
  (loop for m in population collect
        (funcall fitness-func m)))

(defun cosine-fitness (func)
  (declare (optimize (speed 3) (safety 0) (space 0) (debug 0)))
  (let ((sum 0.0))
    (declare (type float sum))
    (loop for x float from 0.0 below 3.1416 by 0.1
          do (let ((res (funcall func x)))
               (declare (type float res))
               (setf sum (+ sum
                            (abs (- (cos x) res))))))
    sum))

(cosine-fitness #'cos)

(let ((functions (list #'(lambda (x) x) #'cos)))
  (mapcar #'list
          functions
          (run #'cosine-fitness functions)))

(defun my-make ()
  )
