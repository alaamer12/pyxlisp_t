import py4cl
"""
It looks it needs special installation
"""
lisp = py4cl.open_lisp()

@lisp.defun
def my_lisp_function(arg):
    return lisp.list(arg, lisp.length(arg))

result = lisp.eval('(my-lisp-function "argument")')
print(result)
