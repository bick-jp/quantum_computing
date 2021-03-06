# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_circuit
from math import pi

backend = "local_qasm_simulator"

qp = QuantumProgram()

nq = 3  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create superposition
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# Grover iteration
iteration = 2
for num in range(iteration):
    # Oracle
    qc.cx(q[1],q[0])
    qc.tdg(q[0])
    qc.cx(q[2],q[0])
    qc.t(q[0])
    qc.cx(q[1],q[0])
    qc.tdg(q[0])
    qc.cx(q[2],q[0])
    qc.t(q[0])
    qc.t(q[1])
    qc.cx(q[2],q[1])
    qc.tdg(q[1])
    qc.cx(q[2],q[1])
    qc.t(q[2])

    # Diffusion operator
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])

    qc.cx(q[1],q[0])
    qc.tdg(q[0])
    qc.cx(q[2],q[0])
    qc.t(q[0])
    qc.cx(q[1],q[0])
    qc.tdg(q[0])
    qc.cx(q[2],q[0])
    qc.t(q[0])
    qc.t(q[1])
    qc.cx(q[2],q[1])
    qc.tdg(q[1])
    qc.cx(q[2],q[1])
    qc.t(q[2])

    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

# Measurement
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1) 

# Show result
# data = results.get_counts(circuits[0])
# plot_histogram(data)
# plot_circuit(qc)
# print(results.get_data(circuits[0]))