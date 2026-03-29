# Notes for Nutanix Certified Professional (NCP)

## Links
```
https://www.certqueen.com/NCP-MCI-6.10-exam.html
https://www.actual4test.com/exam/NCP-MCI-6.10-questions#
https://www.daypo.com/mci-610.html#test
```
## Notes

Runway
the capacity to run current workloads for x amount of months, based on trend

Metro Availability = High Availability

Nutanix supports mixed hardware from different vendors

Compression does not affect Metro Availability

storage must be both empty to register Metro Availability

storage must have identical names to register Metro Availability

cvm = controller VM. Smtn like master node of a cluster

scale-out Prism Central deployment = multi node cluster. Load balancing and HA

runway is per resource ie. cpu, ram. Overall runway always takes the bottlenecking resource

Nutanix Guest Tools is used for application level snapshots. Important for DR

LCM = life cycle manager. Updates components in cluster

AOS = Acropolis Operating System. Similar to RHCOS. The OS that CVMs use

nutanix AOS HA will also manage start up order and priority

Acropolis Dynamic Scheduling (ADS) = load balancing

An Agent VM is a special virtual machine that is tightly bound to a specific host and provides infrastructure or platform services, rather than typical user workloads. basically infra node. It doesnt migrate as easily as other VMs because it is tied to node

prism central can manage multiple cluster. prism element manage ONE cluster only

Advertised capacity limits how big a container can grow, while reserved capacity guarantees how much space it will always have

Bully VMs = VMs consuming excessive resources and negatively impacting others

Prism Central Memory Cluster Runway Diagram red line =  effective memory capacity limit based on the cluster's current
configuration. NOT a hard limit but an indication of the available memory before potential performance
issues occur

IGMP Snooping = Tracks which VMs join multicast groups

LCM performs rolling upgrades. so single node cluster wont work

RF3 cluster = replica factor 3

RF2	2 copies	tolerates 1 node failure without data loss
RF3	3 copies	tolerates 2 node failure without data loss


Protection domain:
When you assign VMs, storage, any resources to a Protection Domain, you are saying:
✔ Take consistent snapshots of these VMs together
✔ Track changes (delta-based replication)
✔ Replicate them to another cluster
✔ Allow failover/failback as a unit


Nutanix AHV port mirroring is performed within the same node first then sent elsewhere

AHV Metro Availability with Witness = The witness ensures that only one node is active among the HA nodes. Enables split brain protection for automatic failover. If nodes cannot talk to one another, and cannot talk to witness, then system will stop

Entity Chart	Multiple metrics for ONE entity
Metric Chart	One metric across MANY entities

hybrid storage pool with SSD + HDD = SSD used for hot writing only (read cache / write buffer / metadata). HDD stores most things

Storage Policies in Nutanix are not directly assigned to VMs or Volume Groups.Instead, they work through:
Categories (policy → category → entity mapping)

agent vm cannot be used as template

storage containers cannot be categorised