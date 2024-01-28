(FROM "../base.hy")

(SET "a" 123)
(SET "b" 1)
(SET "c" 2)
(SET 1 ["3" 123 "qwerty"])
(SET "d" (GET "nginx-" 'cloudname ".mydomain.in"))

(KEY "nested1")
(SET "nk1" 1001)
(SET "nk2" [1002 1003])

(KEY "nested2")
(SET "nkk1" 1001)
(SET "nkk2" [1002 1003])
(UNKEY)

(SET "nk3" (GET "nested-nginx-" 'cloudname ".mydomain.in"))
(UNKEY)
(SET "k5" 105)

