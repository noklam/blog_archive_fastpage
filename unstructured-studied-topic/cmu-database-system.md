# CMU Database System - Lec 03 Database Storage

### Summary 

* Database is like a dict of dict of dict of dict with hierarchy 
  * Pages Directory  \(A Special page to track address of other pages\)
  * Pages  \(Slotted or just append\)
  * Slot 
  * Tuple

### Notes

* The closest you are to the CPU, the faster you are \(L1 cache &lt;-&gt; HDD/Network Storage\)
* New hardware like Non-Volatile Memory is like persistent memory that getting the pro from both sides.
* Non-volatile storage \(SSD/HDD\) is good at sequential access. They like continuous blocks of data.

### Storage Hierarchy

![](../.gitbook/assets/image%20%289%29.png)

![](../.gitbook/assets/image%20%285%29.png)

### Sequential VS Random Access

![](../.gitbook/assets/image%20%287%29.png)

![](../.gitbook/assets/image%20%282%29.png)

## Database Internal

* Files Storage
  * A Collection of Pages - Database manages its own files. You can see those file in your  filesystem, but it is only meaningful to the database.
  * Database Heap
    * Page Directory -  Pointers to Page. i.e. Where can I find an empty page?
* Page Layout
  * 4 KB / 8KB / 16 KB, it represents a block of storage
  * Page Header \( Checksum / DBMS Version/ Page Size\) - Metadata about the Page 
  * Tuple -oriented
    * Slot + Tuple \(Slotted Pages\)
    * Why not append sequentially and track offset? \(As there are delete operation and tuple size varies, many vacuum created and requires moving  a lot of data.\)
  * Log-structured
* Tuple Layout
  * Tuple Header
    * Header + Data
    * Header - Column name, usually in order of the DDL
    * Denormalized Tuple
      * Pre-join data and store directly within the Page, similar to MongoDB

![](../.gitbook/assets/image%20%284%29.png)

![](../.gitbook/assets/image%20%2810%29.png)

![](../.gitbook/assets/image%20%2811%29.png)

