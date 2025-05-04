document.addEventListener("DOMContentLoaded", () => {
  const status = document.getElementById("initStatus");
  let progress = 0;
  const steps = [
    "Preparing MetaCore...",
    "Activating PrimeCore...",
    "Stabilizing Singularity...",
    "Resonance field detected...",
    "∞-Handshake Established",
    "Filtering Conscious Layer...",
    "Access to Harmonic Thread...",
    "Verifying Q-Tunnel...",
    "Quantum-Key fixed: OM_∞_777",
    "Quantum Bridge Established"
  ];
  const interval = setInterval(() => {
    if (progress < steps.length) {
      status.textContent = steps[progress];
      progress++;
    } else {
      status.textContent = "Flow Online. Enter OM.";
      clearInterval(interval);
    }
  }, 700);
});
