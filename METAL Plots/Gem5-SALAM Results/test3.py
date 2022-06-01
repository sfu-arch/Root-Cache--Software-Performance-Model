import matplotlib.pyplot as plt
   
Year = [32,64,128,256,512,1024]
AddressBasedCache = [730670, 696743, 654331, 502799, 463410, 424477]
Indexcache = [871248, 702411, 643178, 460211, 310420, 241270]
  
line1, = plt.plot(Year, AddressBasedCache, 'x-')
line2, = plt.plot(Year, Indexcache, '+-')
plt.title('Index Cache Vs Address Based Cache')
plt.xlabel('Cache Size in ')
plt.ylabel('Latency (in cycles)')
plt.legend(["Address Cache", "Index Cache"])
plt.savefig('ICvAC_seq.png')
plt.show()
