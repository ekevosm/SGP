<img src="logo_SGP.jpg" width=200 align=right>

# SGP - Smart Green Plug

## ΣΚΟΠΟΣ ΤΟΥ ΕΡΓΟΥ
Στόχος της κατασκευής είναι η εφαρμογή τεχνολογιών του Διαδικτύου των Πραγμάτων (ΙοΤ) για την παρακολούθηση της κατανάλωσης ενέργειας από ηλεκτρικές συσκευές και κατ’ επέκταση η καλλιέργεια συνήθειών και πρακτικών φιλικότερων προς το περιβάλλον για την αποδοτική διαχείριση και εξοικονόμηση ηλεκτρικής ενέργειας. 

Με την ΙοΤ συσκευή και εφαρμογή που θα κατασκευάσουμε θα γίνεται μέτρηση και καταγραφή της ηλεκτρικής ενέργειας που καταναλώνει μία συσκευή. Και αυτό γιατί υπάρχουν ορισμένες συσκευές, όπως υπολογιστές, φορτιστές κ.α.  που καταναλώνουν ποικίλες ποσότητες ενέργειας και ορισμένες συσκευές, όπως λαμπτήρες, οθόνες κ.λπ. που καταναλώνουν σταθερή ενέργεια. Υπάρχουν πολλοί λόγοι για τους οποίους η ισχύς πρέπει να παρακολουθείται σε κάθε δεδομένη κατάσταση, είτε αυτό πρόκειται για ασφάλεια, είτε για τη διαχείριση του κόστους της καταναλώσιμης  ενέργειας ή ακόμα και την διάγνωση προβλημάτων των συσκευών.

Το έργο μας εντάσσεται στην κατηγορία της εξοικονόμησης πόρων καθώς στοχεύει στην εξοικονόμηση ηλεκτρικής ενέργειας. Ποιο συγκεκριμένα, η συσκευή μας θα μπορεί να ελέγχει τις ηλεκτρικές συσκευές και αν η χρήση τους είναι αρκετά ενεργοβόρα  ή έχει διαγνωστεί κάποιο πρόβλημα, η συσκευή θα μπορεί να στέλνει μήνυμα στον χρήστη ώστε το πρόβλημα να αντιμετωπιστεί. Κάνοντας αυτόν τον έλεγχο και την καταγραφή των μετρήσεων το ίδιο το άτομο θα καταλαβαίνει τι κατανάλωση έχουν οι συσκευές του και πως λειτουργούν. Με αυτόν τον τρόπο θα μπορεί να έχει γνώση του τι γίνεται στο χώρο του. Έτσι θα εξοικονομείται ενέργεια και θα γίνεται οικονομία.

Γενικότερα, η εξοικείωση με τη λειτουργία των έξυπνων συσκευών για τον έλεγχο και τη μείωση της κατανάλωσης ηλεκτρικής ενέργειας, αναμένεται να συμβάλει στην αλλαγή ενεργειακών συμπεριφορών των εμπλεκομένων μαθητών και εκπαιδευτικών αλλά και ολόκληρης της σχολικής κοινότητας. 

Σε επόμενα στάδια υλοποίησης, το έργο μπορεί να επεκταθεί ώστε να γίνονται συγκριτικές μετρήσεις της κατανάλωσης διαφορετικών συσκευών ή της ίδιας συσκευής σε διαφορετικές συνθήκες λειτουργίας.

## ΤΕΧΝΙΚΑ ΧΑΡΑΚΤΗΡΙΣΤΙΚΆ – ΠΕΡΙΓΡΑΦΗ ΤΟΥ ΕΡΓΟΥ

Για την πιλοτική εφαρμογή του έργου  SGP, θα γίνεται καταμέτρηση της ηλεκτρικής ενέργειας που καταναλώνει ένας ηλεκτρονικός υπολογιστής σε εργαστήριο πληροφορικής του σχολείου.

Για την μέτρηση θα χρησιμοποιηθεί ο αισθητήρας **AC Current Sensor SEN0211**. Ο συγκεκριμένος αισθητήρας προσαρμόζεται στη γραμμή AC και διαθέτει μονάδα μετατροπής σήματος ώστε να μετριέται η τρέχουσα τιμή του ρεύματος. Η έξοδος την μονάδας είναι αναλογική.

Η αναλογική έξοδος της μονάδας μετατροπής του αισθητήρα συνδέεται σε μικροελεγκτή **ESP32**. Επιλέξαμε να χρησιμοποιήσουμε τον μικροελεγκτή ESP32 επειδή είναι ένα πολύ οικονομικό ολοκληρωμένο κύκλωμα που χρησιμοποιείται σε ένα μεγάλο εύρος ΙοΤ εφαρμογών. Υποστηρίζει συνδέσεις Wifi και Bluetooth για αποστολή και λήψη των δεδομένων, καθώς και ενσύρματα πρωτόκολλα σειριακής επικοινωνίας.

To **Raspberry Pi** θα χρησιμοποιηθεί ως εξυπηρετητής για την αποθήκευση, επεξεργασία και οπτικοποίηση των δεδομένων. Η πρόσβαση στον εξυπηρετητή θα γίνεται μέσω του δικτύου Wifi του σχολείου.

Ως γλώσσα προγραμματισμού έχει επιλεγεί η **Python** και πιο συγκεκριμένα η έκδοση mPython που υποστηρίζεται από το ESP32. 

Για την διαχείριση των ΙοΤ συσκευών, την αποθήκευση και οπτικοποίηση των δεδομένων θα αξιοποιηθούν οι παρακάτω τεχνολογίες ελεύθερου/ανοιχτού λογισμικού:
- **NodeRed** για την επικοινωνία του συστήματος μέτρησης με τον εξυπηρετητή για την αρχική απεικόνιση και την αποθήκευση των δεδομένων, καθώς και την αποστολή μηνυμάτων ηλεκτρονικού ταχυδρομείου σε περίπτωση έκτακτης ανάγκης.
- **InfluxDB** ως σύστημα διαχείρισης βάσης δεδομένων
- **Grafana** για την οπτικοποίηση των δεδομένων

Τα υλικά που θα απαιτηθούν καθώς και το αντίστοιχο κόστος καταγράφονται αναλυτικά στον παρακάτω πίνακα:

|Απαιτούμενος εξοπλισμός |	Ποσότητα |	Ενδεικτικό Κόστος (€) |
| ----------- | ----------- | ----------- | 
| Raspberry Pi 4 Model B |	<div align="center">1 </div> |	<div align="right"> 70,0</div> |
| Analog AC Current Sensor (SEN0211) |	<div align="center">1  </div> |	<div align="right"> 27,0</div> |
|	ESP32 with Battery Holder	|	<div align="center">1 </div> |	<div align="right"> 14,0 </div> |
|	Καλώδιο USB to micro-USB	|	<div align="center">1 </div> |	<div align="right"> 7,0</div> |
|	Κουτί διακλάδωσης	|	<div align="center">1 </div> |	<div align="right"> 2,0</div> |
| <div align="right">**ΣΥΝΟΛΟ** </div> ||	 	 	<div align="right"> **120,0**</div> |
