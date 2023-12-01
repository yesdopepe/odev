#çalıştırmadan önce dependacies.bat yada dependacies.bash'i çalıştırın
import pandas as pd
import matplotlib.pyplot as plt

# xlsx oku
df = pd.read_excel('Ödev.xlsx')

# doğru
plt.hist(df['notlar'], bins='auto', alpha=0.7, color='blue', edgecolor='black')

# eksenlere ad tanımla
plt.xlabel('notlar')
plt.ylabel('kişi sayısı')
plt.title('Histogram')

# görüntüle
plt.legend()
#kaydet
plt.savefig('histogram.png')
# göster
plt.show()