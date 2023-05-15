#Setting up the base image. This is the compiler for the c program
FROM gcc

#Creating a new directory called "example" in the "/home" directory 
RUN mkdir -p /home/example

#Setting the working directory for the rest of the commands
WORKDIR /example

#Copying everything inside the current directory of the host pc and pasting into the workdir of the container
COPY . .

#Compiling the program
RUN gcc -o example example.c

#Executing the program
CMD ["./example"]

#Setting the listening port
EXPOSE 3000


