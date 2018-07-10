from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from math import pi

qp = QuantumProgram()

nq = 5  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['testQ']
testQ = qp.create_circuit(circuits[0], [q], [c])

# Apply H gate
testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])

##### CCCZ start #####
# CCX
testQ.h(q[2]) 
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.tdg(q[3])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.tdg(q[3])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.s(q[3])
testQ.t(q[4])

# CZ^(-1/2)
testQ.cx(q[2],q[1])
testQ.t(q[1])
testQ.cx(q[2],q[1])
testQ.tdg(q[1])
testQ.tdg(q[2])

# CCX
testQ.h(q[2])
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.tdg(q[3])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.tdg(q[3])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.s(q[3])
testQ.t(q[4])

# CZ^(1/2)
testQ.cx(q[2],q[1])
testQ.tdg(q[1])
testQ.cx(q[2],q[1])
testQ.t(q[1])
testQ.t(q[2])

# CX
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])

# CZ^(-1/4)
## Swap
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])

## CZ^(-1/4)
testQ.cx(q[3],q[2])
testQ.u1((pi/8), q[2])
testQ.cx(q[3],q[2])
testQ.u1((-pi/8), q[2])
testQ.u1((-pi/8), q[3])

# CX
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])

## CZ^(1/4)
testQ.cx(q[3],q[2])
testQ.u1((-pi/8), q[2])
testQ.cx(q[3],q[2])
testQ.u1((pi/8), q[2])
testQ.u1((pi/8), q[3])

## CZ^(1/4)
testQ.cx(q[4],q[2])
testQ.u1((-pi/8), q[2])
testQ.cx(q[4],q[2])
testQ.u1((pi/8), q[2])
testQ.u1((pi/8), q[4])

## Swap
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])
##### CCCZ end #####

##### Diffusion start #####
testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])

testQ.x(q[1])
testQ.x(q[2])
testQ.x(q[3])
testQ.x(q[4])


### CCCZ inside diffusion start ###
# CCX
testQ.h(q[2]) 
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.tdg(q[3])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.tdg(q[3])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.s(q[3])
testQ.t(q[4])

# CZ^(-1/2)
testQ.cx(q[2],q[1])
testQ.t(q[1])
testQ.cx(q[2],q[1])
testQ.tdg(q[1])
testQ.tdg(q[2])

# CCX
testQ.h(q[2])
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.cx(q[3],q[2])
testQ.tdg(q[2])
testQ.cx(q[4],q[2])
testQ.t(q[2])
testQ.tdg(q[3])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.tdg(q[3])
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])
testQ.s(q[3])
testQ.t(q[4])

# CZ^(1/2)
testQ.cx(q[2],q[1])
testQ.tdg(q[1])
testQ.cx(q[2],q[1])
testQ.t(q[1])
testQ.t(q[2])

# CX
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])

# CZ^(-1/4)
## Swap
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])

## CZ^(-1/4)
testQ.cx(q[3],q[2])
testQ.u1((pi/8), q[2])
testQ.cx(q[3],q[2])
testQ.u1((-pi/8), q[2])
testQ.u1((-pi/8), q[3])

# CX
testQ.h(q[3])
testQ.h(q[4])
testQ.cx(q[3],q[4])
testQ.h(q[3])
testQ.h(q[4])

## CZ^(1/4)
testQ.cx(q[3],q[2])
testQ.u1((-pi/8), q[2])
testQ.cx(q[3],q[2])
testQ.u1((pi/8), q[2])
testQ.u1((pi/8), q[3])

## CZ^(1/4)
testQ.cx(q[4],q[2])
testQ.u1((-pi/8), q[2])
testQ.cx(q[4],q[2])
testQ.u1((pi/8), q[2])
testQ.u1((pi/8), q[4])

## Swap
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])
testQ.h(q[1])
testQ.h(q[2])
testQ.cx(q[2],q[1])
### CCCZ inside diffusion end ###

testQ.x(q[1])
testQ.x(q[2])
testQ.x(q[3])
testQ.x(q[4])

testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])
##### Diffusion end #####


# Measurement
testQ.measure(q[1], c[1])
testQ.measure(q[2], c[2])
testQ.measure(q[3], c[3])
testQ.measure(q[4], c[4])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
plot_histogram(results.get_counts(circuits[0]))

#circuit_drawer(testQ)