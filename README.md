# How to run C code with Python interpreter

**TL;DR:** Use `make` to build and run the example.

Compile:

```bash
gcc -c -fPIC c_ode.c -o c_ode.o
```

Generate the shared object:

```bash
gcc c_ode.o -shared -o libc_ode.so
```


## Reference

- https://www.csestack.org/calling-c-functions-from-python/
