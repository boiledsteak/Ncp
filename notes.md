# Notes for Nutanix Certified Professional (NCP)

## Links
```
https://www.certqueen.com/NCP-MCI-6.10-exam.html
https://www.actual4test.com/exam/NCP-MCI-6.10-questions#
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