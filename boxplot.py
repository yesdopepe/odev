#çalıştırmadan önce dependacies.bat yada dependacies.bash'i çalıştırın
import pandas as pd
import matplotlib.pyplot as plt

# xlsx oku
df = pd.read_excel('Ödev.xlsx')

# doğru
plt.boxplot(df['notlar'])

# eksenlere ad tanımla
plt.xlabel('')
plt.ylabel('notlar')
plt.title('Boxplot')

# görüntüle
plt.legend()
#kaydet
plt.savefig('boxplot')
# göster
plt.show()