**RAID 0** — Striping | Min 2 drives | No fault tolerance | Speed only

**RAID 1** — Mirroring | Min 2 drives | 1 drive can fail | Identical copies on each drive

**RAID 5** — Striping with parity | Min 3 drives | 1 drive can fail | Data rebuilt from parity

**RAID 6** — Striping with double parity | Min 4 drives | Up to 2 drives can fail

**RAID 10** — Stripe of mirrors (RAID 1+0) | Min 4 drives | 1 drive per mirrored pair can fail

---

**Cold Site** — Just a physical space and power. No hardware or data. Cheapest, slowest to recover (days/weeks)

**Warm Site** — Has hardware and connectivity, but data needs to be restored. Middle ground on cost and recovery time (hours/days)

**Hot Site** — Fully operational duplicate of your environment, live data synced. Most expensive, fastest recovery (minutes/hours)

**Mirror Site** — Identical real-time copy, always live. Even faster than hot site, essentially instant fail-over

**COOP (Continuity of Operations Plan)** — The overarching plan that defines how an organization keeps essential functions running during and after a disruption. The umbrella that the sites above fall under

Which of the following is the primary function of clustering?
- Groups servers together to provide high availability and fault tolerance

Which of the following terms refers to a backup strategy that relies on creating and maintaining copies of data in real-time or near real-time on a separate system?
- Replication