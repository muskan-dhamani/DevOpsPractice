# Step 1: Use openjdk image to compile and package the JAR
FROM openjdk:17-alpine as builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Java source code into the container
COPY AdditionProgram.java .

# Compile the Java program
RUN javac AdditionProgram.java

# Package the compiled Java program into a JAR file
RUN jar cfe AdditionProgram.jar AdditionProgram AdditionProgram.class

# Step 2: Use a distroless image to run the JAR file
FROM gcr.io/distroless/java17

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file from the builder stage to the distroless image
COPY --from=builder /app/AdditionProgram.jar .

# Set the entry point for the Java application
ENTRYPOINT ["java", "-jar", "AdditionProgram.jar"]

