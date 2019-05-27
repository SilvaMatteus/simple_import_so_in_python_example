all: libc_ode.so python_code
	@echo FINISHED!

libc_ode.so:
	gcc -shared -o libc_ode.so -fPIC c_ode.c
	@echo COMPILE c_ode.c >> libc_ode.so

python_code:
	python py_code.py
	@echo RUN python...

clean:
	$(RM) libc_ode.so c_ode.o 2>/dev/null
