from datetime import datetime
import psycopg2
connection = psycopg2.connect(
    host = "localhost", 
    port="5432", 
    database="postgres", 
    user="postgres", 
    password="mysecretpassword")

cur = connection.cursor()

print('''Hoşgeldin!
Randevu oluşturmak bazı bilgilerine ihtiyacımız var.
Sırayla bilgilerini girebilir misin?
''')

name = input('İsim: ')
surname = input('Soyad: ')
phone = input('Telefon: ')
email = input('Email: ')

insert_customer_script = 'INSERT INTO customers (customer_name, customer_surname, phone, email) VALUES (%s, %s, %s, %s)'
insert_customer_value = (name, surname, phone, email)

cur.execute(insert_customer_script, insert_customer_value)

connection.commit() #commitlemezsen db'e gitmez

print()




print('Merhaba %s hangi tarihte randevu istersin?' % name)
date = input('Tarih (YYYY-AA-GG): ')

cur.execute("SELECT max(customer_id) FROM customers")
customer_id = cur.fetchone()
if customer_id:
    # Extract the value from the tuple
    customer_id = int(customer_id[0])
else:
    print("Öncelikle müşteri kaydını tamamlamalısın.")

available_intervals_query = f"""SELECT * FROM appointments WHERE appointment_date = '{date}'""" #Uc tirnak kullanarak string 
cur.execute(available_intervals_query, (date, ))
nonavailable_intervals = cur.fetchall()

'''available_intervals_query = 'SELECT * FROM appointments WHERE appointment_date = %s'
cur.execute(available_intervals_query, (date, ))
nonavailable_intervals = cur.fetchall()'''

print('Seçtiğiniz tarihde şu saatler doludur: ')
for i in nonavailable_intervals:
    print(i[3])

time_interval = input('\n Zaman aralığı girin: ') #varolan bir zaman araliginda girerse hata ver ve yeniden girdir

cur.execute("SELECT * FROM product_type") 
product_types = cur.fetchall()
for i in product_types:
    print(i[0],'.',i[1])
product_type_selection = input('Hangi tipte ürün denemek istersin?  ')

insert_appointment_script = 'INSERT INTO appointments (customer_id, appointment_date, time_interval, product_type_selection) VALUES (%s, %s, %s, %s)'
insert_appointment_value = (customer_id, date, time_interval, product_type_selection)

cur.execute(insert_appointment_script, insert_appointment_value)

connection.commit() #commitlemezsen db'e gitmez

print('''
Randevunuz başarıyla oluşturulmuştur.
Görüşmek üzere...''')


'''cur.execute("SELECT max(customer_id) FROM customers")
last_customer_id = cur.fetchone()
print(last_customer_id)'''

#cur.execute("SELECT * FROM customers")

#rows = cur.fetchall()

#for r in rows:
#    print(r)

cur.close()
connection.close()