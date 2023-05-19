import imp
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_provider import IBMProvider
from qiskit.providers.aer.noise import NoiseModel, ReadoutError

# Simulate on fake Peekskill. Created due to heavy queue times


def run(qc):
    provider_info = imp.load_source("provider_info", "../provider_info")
    hub = provider_info.SPR_23_HUB
    group = provider_info.SPR_23_GRP
    project = provider_info.SPR_23_PRJ
    backend_name = "ibm_peekskill"
    provider = IBMProvider()
    backend = provider.get_backend(backend_name, instance=f"{hub}/{group}/{project}")
    noise_model = NoiseModel.from_backend_properties(backend.properties())
    qc_transpiled = transpile(qc, backend)

    sim = AerSimulator(noise_model=noise_model)
    job = sim.run(qc_transpiled, shots=1000)
    result = job.result()
    counts = result.get_counts()

    return counts
